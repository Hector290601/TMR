# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 23:51:22 2020

@author: hrmha
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
maxb = np.array([180, 10, 170])
minb = np.array([90, 0, 10])
while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h, _, _ = frame.shape
    frame = frame[int(h / 2.1) :]
    mask = cv2.inRange(hsv, minb, maxb)
    gray = cv2.GaussianBlur(frame, (7, 7), 1.41)
    blur = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(blur, 25, 75)
    maskpfrm = cv2.bitwise_and(frame, frame, mask = mask)
    maskpedgs = cv2.bitwise_and(edge, edge, mask = mask)
    cv2.imshow('cannyEdge.jpeg', edge)
    cv2.imshow('hsv.jpeg', hsv)
    cv2.imshow('whites.jpeg', mask)
    cv2.imshow('whitesAndFrame.jpeg', maskpfrm)
    cv2.imshow('whitesAndEdges.jpeg', maskpedgs)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break;
