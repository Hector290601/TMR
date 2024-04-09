# Imports {{{
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
import math
from std_msgs.msg import Float64MultiArray, UInt8MultiArray
import os
# }}}

#upper_color = [130, 254, 255]        
#lower_color = [0, 195, 0] 
upper_color = [179, 114, 121]
lower_color = [0, 25, 0]

rho_delta = 10
theta_delta = 0.25

average_rho_left= 0
average_theta_left= 0

average_rho_right= 0
average_theta_right= 0

left_rho_min = 0
left_rho_max = 0
left_theta_min = average_theta_left - theta_delta
left_theta_max = average_theta_left + theta_delta

right_rho_min= 0
right_rho_max= 0
right_theta_max= average_theta_right - theta_delta
right_theta_min= average_theta_right + theta_delta

variance_rho = 50
variance_theta = 0.12
delta = 5

upper = -1000
lower = 1000
lefter = 1000
righter = -1000

frame = []

# to_normal_form {{{
def to_normal_form(x1, y1, x2, y2):
    A = y2 - y1
    B = x1 - x2
    C = A*x1 + B*y1
    theta = math.atan2(B,A)
    rho   = C/math.sqrt(A*A + B*B)
    if rho < 0:
        theta += math.pi
        rho = -rho
    return np.asarray([rho, theta])
#}}}

# mouse_callback {{{
def mouse_callback(event, x, y, flags, param):
    global where, upper_color, lower_color
    if event == cv2.EVENT_LBUTTONDOWN:
        hu, su, vu = upper_color
        hl, sl, vl = lower_color
        hc, sc, vc = where[y, x]
        if hu < hc:
            hu = int(hc)
        if su < sc:
            su = int(sc)
        if vu < vc:
            vu = int(vc)
        if hc < hl:
            hl = int(hc)
        if sc < sl:
            sl = int(sc)
        if vc < vl:
            vl = int(vc)
        upper_color = [hu, su, vu]
        lower_color = [hl, sl, vl]
    elif event == cv2.EVENT_RBUTTONDOWN:
        upper_color = [0, 0, 0]
        lower_color = [255, 255, 255]
    elif event == cv2.EVENT_MOUSEWHEEL:
        print("upper_color = {}\nlower_color = {}".format(
            upper_color, lower_color
            )
            )
#}}}


class ImageSubscriber(Node):
  # Init {{{
  def __init__(self):
    super().__init__('image_subscriber')
    self.subscription = self.create_subscription(
      Image, 
      '/raw_rgb', 
      self.listener_callback, 
      1
      )
    self.left_lane_publisher = self.create_publisher(Float64MultiArray, '/lines/left', 1)
    self.right_lane_publisher = self.create_publisher(Float64MultiArray, '/lines/right', 1)
    self.subscription
    self.br = CvBridge()
    # }}}

  # range_finder {{{
  def range_finder(self):
    global lower_color, upper_color, where
    band_filter = cv2.inRange(
                where,
            np.array(lower_color),
            np.array(upper_color)
        )
    return band_filter
  #}}}

  # process_image {{{
  def process_image(self):
      global frame, where
      hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
      where = hsv
      return hsv
  #}}}
  
  # two_dots_line {{{
  def two_dots_line(self, rho, theta, frame):
      if rho == 0 or theta == 0:
          return
      a = math.cos(theta)
      b = math.sin(theta)
      x0 = a * rho
      y0 = b * rho
      pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
      pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
      return pt1[0], pt1[1], pt2[0], pt2[1]
  # }}}

  # line_finder {{{
  def line_finder(self):
      global band_pass, frame, dst
      global right_theta_min, right_theta_max, right_rho_min, right_rho_max
      global left_theta_min, left_theta_max, left_rho_min, left_rho_max
      global lower, upper, lefter, righter, upper_color, lower_color, color_delta
      global average_rho_left, average_rho_right, average_theta_left, average_theta_right
      kernel = np.ones((6, 6), np.uint8) 
      band_pass = cv2.morphologyEx(band_pass, cv2.MORPH_OPEN, kernel, iterations=1)
      dst = cv2.Canny(band_pass, 100, 100, 10, None)
      lines = cv2.HoughLinesP(dst, 3, np.pi/90, 80, minLineLength=25, maxLineGap=1)
      if lines is not None:
          lines = lines[:, 0]
      if lines is not None:
          sum_theta_left = 0
          sum_rho_left = 0
          sum_theta_right = 0
          sum_rho_right = 0
          count_left = 0
          count_right = 0
          h = 0
          s = 0
          counter_color = 0
          for i in range(0, len(lines)):
              l = lines[i]
              rho, theta = to_normal_form(l[0], l[1], l[2], l[3])
              if (average_rho_right == 0
                  and average_theta_right == 0
                  and (
                      (
                          (
                              (450 <= l[0] <= 590)
                              and (140 <= l[1] <= 240)
                          )
                          or (
                              (450 <= l[2] <= 590)
                              and (140 <= l[3] <= 240)
                             )
                     )
                  )
                 ):
                  sum_theta_right += theta
                  sum_rho_right += rho
                  count_right += 1
              elif (average_rho_left == 0
                    and average_theta_left == 0
                  and (
                      (
                          (
                              (50 <= l[0] <= 190)
                              and (140 <= l[1] <= 240)
                          )
                          or (
                              (50 <= l[2] <= 190)
                              and (140 <= l[3] <= 240)
                             )
                     )
                  )
                ):
                  sum_theta_left += theta
                  sum_rho_left += rho
                  count_left += 1
              elif (
                      (right_theta_min <= theta <= right_theta_max)
                      and (right_rho_min <= rho <= right_rho_max)
                 ):
                  sum_theta_right += theta
                  sum_rho_right += rho
                  count_right += 1
                  print("rho:{}\ttheta:{}\tpassed as right".format(
                      rho,
                      theta
                      ))
              elif (
                      (left_theta_min <= theta <= left_theta_max)
                      and (left_rho_min <= rho <= left_rho_max)
                   ):
                  sum_theta_left += theta
                  sum_rho_left += rho
                  count_left += 1
                  """
                  print("rho:{}\ttheta:{}\tpassed as left".format(
                      rho,
                      theta
                      ))
                  """
              else:
                  if(theta > 0):
                      cv2.line(frame, (l[0], l[1]), (l[2], l[3]), (255,255,0), 3, cv2.LINE_AA)
                      #print("{} > 0".format(theta))
                  elif(theta < 0):
                      cv2.line(frame, (l[0], l[1]), (l[2], l[3]), (0,255,255), 3, cv2.LINE_AA)
                      print([right_theta_min, theta, right_theta_max])
                      print([right_rho_min, rho, right_rho_max])
          if count_left > 0:
              #print("count_left is bigger than zero")
              average_rho_left = sum_rho_left / count_left
              average_theta_left = sum_theta_left / count_left
              left_theta_min = average_theta_left - variance_theta
              left_theta_max = average_theta_left + variance_theta
              left_rho_min = average_rho_left - variance_rho
              left_rho_max = average_rho_left + variance_rho
              message = Float64MultiArray()
              message.data = [average_rho_left, average_theta_left]
              self.left_lane_publisher.publish(message)
              #print([left_rho_min, average_rho_left, left_rho_max])
              #print([left_theta_min, average_theta_left, left_theta_max])
              #"""
              try:
                  x1, y1, x2, y2 = self.two_dots_line(average_rho_left, average_theta_left, frame)
                  x3 = x1 + delta
                  x4 = x1 - delta
                  x5 = x2 + delta
                  x6 = x2 - delta
                  cv2.line(frame, (x1, y1), (x2, y2), (255,0,0), 3, cv2.LINE_AA)
              except:
                  pass
              #"""
          if count_right > 0:
              print("count_right is bigger than zero")
              average_rho_right = sum_rho_right / count_right
              average_theta_right = sum_theta_right / count_right
              right_theta_min = average_theta_right - variance_theta
              right_theta_max = average_theta_right + variance_theta
              right_rho_min = average_rho_right - variance_rho
              right_rho_max = average_rho_right + variance_rho
              message = Float64MultiArray()
              message.data = [average_rho_right, average_theta_right]
              self.right_lane_publisher.publish(message)
              print([right_rho_min, average_rho_right, right_rho_max])
              print([right_theta_min, average_theta_right, right_theta_max])
              #"""
              try:
                  x1, y1, x2, y2 = self.two_dots_line(average_rho_right, average_theta_right, frame)
                  x3 = x1 + delta
                  x4 = x1 - delta
                  x5 = x2 + delta
                  x6 = x2 - delta
                  cv2.line(frame, (x1, y1), (x2, y2), (0,0,255), 3, cv2.LINE_AA)
              except Exception as e:
                  print(e)
              #"""
          frame = cv2.rectangle(frame, (50, 140), (190, 240), (255, 0, 0), 5)
          frame = cv2.rectangle(frame, (450, 140), (590, 240), (0, 0, 255), 5)
          #print("#############################################################")
  #}}}
  
  # listener_callback {{{
  def listener_callback(self, data):
    global frame, band_pass, dst
    frame = self.br.imgmsg_to_cv2(data)[240:, :, :]
    #frame = current_frame
    hsv = self.process_image()
    band_pass = self.range_finder()
    self.line_finder()
    #"""
    cv2.imshow("camera", frame)
    cv2.imshow("band_filter", band_pass)
    cv2.imshow("dst", dst)
    cv2.setMouseCallback("camera", mouse_callback)
    cv2.setMouseCallback("dst", mouse_callback)
    cv2.setMouseCallback("band_filter", mouse_callback)
    cv2.waitKey(1)
    #"""
  # }}}

# main {{{
def main(args=None):
  rclpy.init(args=args)
  image_subscriber = ImageSubscriber()
  rclpy.spin(image_subscriber)
  image_subscriber.destroy_node()
  rclpy.shutdown()
#}}}
  
if __name__ == '__main__':
  main()
