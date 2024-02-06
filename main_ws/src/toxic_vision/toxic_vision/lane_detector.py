import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
import math
from std_msgs.msg import Float64MultiArray
import os

upper_color = [130, 254, 255]
lower_color = [0, 216, 0]

left_min = 0.7
left_max = 1
right_min = -1.0
right_max = -0.7
variance = 0.1
delta = 5

upper = -1
lower = 1000
lefter = 1000
righter = -1

frame = []

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

class ImageSubscriber(Node):
  def __init__(self):
    super().__init__('image_subscriber')
    self.subscription = self.create_subscription(
      Image, 
      '/raw_rgb', 
      self.listener_callback, 
      1
      )
    self.left_lane_publisher = self.create_publisher(Float64MultiArray, '/lines/left', 1)
    self.subscription
    self.br = CvBridge()

  def range_finder(self):
    global lower_color, upper_color, where
    band_filter = cv2.inRange(
                where,
            np.array(lower_color),
            np.array(upper_color)
        )
    return band_filter

  def process_image(self):
      global frame, where
      hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
      where = hsv
      return hsv
  
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


  def line_finder(self):
      global band_pass, frame, dst, right_min, right_max, left_min, left_max, lower, upper, lefter, righter, upper_color, lower_color, color_delta
      kernel = np.ones((3, 5), np.uint8) 
      band_pass = cv2.morphologyEx(band_pass, cv2.MORPH_OPEN, kernel, iterations=1)
      dst = cv2.Canny(band_pass, 100, 100, 3, None)
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
          average_rho_left = 0
          average_theta_left = 0
          average_rho_right = 0
          average_theta_right = 0
          h = []
          s = []
          v = []
          for i in range(0, len(lines)):
              l = lines[i]
              rho, theta = to_normal_form(l[0], l[1], l[2], l[3])
              if right_min < theta < right_max:
                  #cv2.line(frame, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv2.LINE_AA)
                  sum_theta_right += theta
                  sum_rho_right += rho
                  count_right += 1
                  left1_tmp = l[0] - 5
                  left2_tmp = l[2] - 5
                  right1_tmp = l[0] + 5
                  right2_tmp = l[2] + 5
                  roi_left = right1_tmp if right1_tmp < left1_tmp else left1_tmp
                  roi_right = right2_tmp if right2_tmp < left2_tmp else left2_tmp
                  roi_upper = l[1] if l[1] > l[3] else l[3]
                  roi_lower = l[1] if l[1] < l[3] else l[3]
                  colors = frame[roi_lower:roi_upper, roi_left:roi_right, :]
                  #frame = cv2.rectangle(frame, (roi_left, roi_upper), (roi_right, roi_lower), (255, 0, 0), 0)
                  for row in colors:
                      for col in row:
                          if (lower_color[0] < col[0] < upper_color[0]) and (lower_color[1] < col[1] < upper_color[1]):
                              h.append(col[0])
                              s.append(col[1])
              elif left_min < theta < left_max:
                  #cv2.line(frame, (l[0], l[1]), (l[2], l[3]), (255,0,0), 3, cv2.LINE_AA)
                  sum_theta_left += theta
                  sum_rho_left += rho
                  count_left += 1
                  left1_tmp = l[0] - 5
                  left2_tmp = l[2] - 5
                  right1_tmp = l[0] + 5
                  right2_tmp = l[2] + 5
                  roi_left = right1_tmp if right1_tmp < left1_tmp else left1_tmp
                  roi_right = right2_tmp if right2_tmp < left2_tmp else left2_tmp
                  roi_upper = l[1] if l[1] > l[3] else l[3]
                  roi_lower = l[1] if l[1] < l[3] else l[3]
                  colors = frame[roi_lower:roi_upper, roi_left:roi_right, :]
                  #frame = cv2.rectangle(frame, (roi_left, roi_upper), (roi_right, roi_lower), (255, 0, 0), 0)
                  for row in colors:
                      for col in row:
                          if (lower_color[0] < col[0] < upper_color[0]) and (lower_color[1] < col[1] < upper_color[1]):
                              h.append(col[0])
                              s.append(col[1])
          if count_left > 0:
              average_rho_left = sum_rho_left / count_left
              average_theta_left = sum_theta_left / count_left
              left_min = average_theta_left - variance
              left_max = average_theta_left + variance
              message = Float64MultiArray()
              message.data = [average_rho_left, average_theta_left]
              self.left_lane_publisher.publish(message)
              try:
                  x1, y1, x2, y2 = self.two_dots_line(average_rho_left, average_theta_left, frame)
                  x3 = x1 + delta
                  x4 = x1 - delta
                  x5 = x2 + delta
                  x6 = x2 - delta
                  cv2.line(frame, (x1, y1), (x2, y2), (255,0,0), 3, cv2.LINE_AA)
              except:
                  pass
          if count_right > 0:
              average_rho_right = sum_rho_right / count_right
              average_theta_right = sum_theta_right / count_right
              right_min = average_theta_right - variance
              right_max = average_theta_right + variance
              try:
                  x1, y1, x2, y2 = self.two_dots_line(average_rho_right, average_theta_right, frame)
                  x3 = x1 + delta
                  x4 = x1 - delta
                  x5 = x2 + delta
                  x6 = x2 - delta
                  cv2.line(frame, (x1, y1), (x2, y2), (0,0,255), 3, cv2.LINE_AA)
              except:
                  pass
          upper = -1
          lower = 1000
          lefter = 1000
          righter = -1
          std_h = np.std(np.array(h))
          std_s = np.std(np.array(s))
          std_v = np.std(np.array(v))
          avg_h = np.average(h)
          avg_s = np.average(s)
          avg_v = np.average(v)
          new_h_up = avg_h + 130 if len(h) != 0 else upper_color[0]
          new_s_up = avg_s + 40 if len(s) != 0 else upper_color[1]
          new_h_low = avg_h - 130 if len(h) != 0 else lower_color[0]
          new_s_low = avg_s - 40 if len(s) != 0 else lower_color[1]
          """
          upper_color = [
                  int(new_h_up),
                  int(new_s_up),
                  255
                  ]
          lower_color = [
                  int(new_h_low),
                  int(new_s_low),
                  0
                  ]
          os.system("clear")
          print([std_h, std_s, std_v])
          """


  def listener_callback(self, data):
    global frame, band_pass, dst
    current_frame = self.br.imgmsg_to_cv2(data)[240:, :, :]
    frame = current_frame
    hsv = self.process_image()
    band_pass = self.range_finder()
    self.line_finder()
    cv2.imshow("camera", frame)
    cv2.imshow("band_filter", band_pass)
    cv2.imshow("dst", dst)
    cv2.setMouseCallback("camera", mouse_callback)
    cv2.setMouseCallback("dst", mouse_callback)
    cv2.setMouseCallback("band_filter", mouse_callback)
    cv2.waitKey(1)
  
def main(args=None):
  rclpy.init(args=args)
  image_subscriber = ImageSubscriber()
  rclpy.spin(image_subscriber)
  image_subscriber.destroy_node()
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()
