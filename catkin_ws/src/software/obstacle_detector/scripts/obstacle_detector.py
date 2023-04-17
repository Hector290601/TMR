import rospy
from sensor_msgs.msg import LaserScan
import numpy as np
from sklearn.cluster import DBSCAN

def scan_callback(scan_data):
    # Convertir datos de láser en matriz
    ranges = np.array(scan_data.ranges)
    angles = np.linspace(scan_data.angle_min, scan_data.angle_max, len(ranges))
    X = np.vstack((ranges*np.cos(angles), ranges*np.sin(angles))).T

    # Eliminar puntos de ruido
    X = X[ranges > 0.1, :]

    # Segmentación de objetos utilizando el algoritmo DBSCAN
    db = DBSCAN(eps=0.2, min_samples=5).fit(X)
    labels = db.labels_

    # Filtrar objetos por tamaño
    unique_labels = set(labels)
    for label in unique_labels:
        if label == -1:
            # Este es el ruido, ignorarlo
            continue
        else:
            # Obtener los puntos que pertenecen a este objeto
            mask = (labels == label)
            points = X[mask, :]

            # Calcular la posición y el tamaño del objeto
            x = np.mean(points[:, 0])
            y = np.mean(points[:, 1])
            size = np.sqrt(np.sum((points - np.mean(points, axis=0))**2, axis=1)).max()

            # Publicar los resultados de detección de obstáculos
            # Implemente la publicación de resultados aquí

def main():
    rospy.init_node('/obstacle_detector')
    rospy.Subscriber('/scan', LaserScan, scan_callback)
    rospy.spin()

if __name__ == '__main__':
    main()
