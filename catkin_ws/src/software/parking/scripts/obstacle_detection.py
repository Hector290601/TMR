#!/usr/bin/env python
import rospy
import numpy as np
from std_msgs.msg import Header
from sensor_msgs.msg import LaserScan
from sklearn.cluster import DBSCAN
from visualization_msgs.msg import MarkerArray, Marker

def callback(laser_scan):
    ranges = np.array(laser_scan.ranges)
    angles = np.linspace(laser_scan.angle_min, laser_scan.angle_max, len(ranges))
    mask_not_nan = np.logical_not(np.isnan(ranges))
    ranges = ranges[mask_not_nan]
    angles = angles[mask_not_nan]
    ranges = exponential_moving_average(ranges, alpha=0.2)
    angles = moving_average(angles, window_size=5)
    point_cloud_array = polar_to_cartesian(ranges, angles)
    distance_limits = (1.5, 10)
    point_cloud_array = filter_point_cloud_by_distance(point_cloud_array, distance_limits)
    if point_cloud_array.shape[0] > 0:
        cluster_labels = DBSCAN(eps=0.2, min_samples=10).fit_predict(point_cloud_array)
        centroids = find_cluster_centroids(point_cloud_array, cluster_labels)
        publish_point_cloud(centroids)

def polar_to_cartesian(ranges, angles):
    x = ranges * np.cos(angles)
    y = ranges * np.sin(angles)
    point_cloud_array = np.column_stack((x, y))
    return point_cloud_array

def filter_point_cloud_by_distance(point_cloud_array, distance_limits):
    distances = np.linalg.norm(point_cloud_array, axis=1)
    mask = np.logical_and(distances > distance_limits[0], distances < distance_limits[1])
    return point_cloud_array[mask]

def find_cluster_centroids(point_cloud_array, cluster_labels):
    unique_labels = np.unique(cluster_labels)
    centroids = []
    for label in unique_labels:
        mask = cluster_labels == label
        cluster_points = point_cloud_array[mask]
        centroid = np.mean(cluster_points, axis=0)
        centroids.append(centroid)
    return np.array(centroids)

def publish_point_cloud(points):
    global point_cloud_publisher
    header = Header()
    header.stamp = rospy.Time.now()
    header.frame_id = 'lidar_link'
    point_cloud = point_cloud2.create_cloud_xyz32(header, points)
    point_cloud_publisher.publish(point_cloud)

def main():
    global point_cloud_publisher
    print("INITIALIZING OBSTACLE DETECTION NODE...")
    rospy.init_node('obstacle_detection')
    point_cloud_publisher = rospy.Publisher('/obstacle_centroids', PointCloud2, queue_size=10)
    rospy.wait_for_message('/scan', LaserScan)
    rospy.Subscriber('/scan', LaserScan, callback)
    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except:
        rospy.ROSInterruptException
        pass
