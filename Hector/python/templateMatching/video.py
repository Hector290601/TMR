import cv2
import numpy as np

vdo = cv2.VideoCapture("primero.mp4")    #lee el video de prueba
template = cv2.imread("template4.png")   #lee el template
while vdo.isOpened():
    ret, img = vdo.read()

    #   crea la zona de interés
    poly = np.array([
        [600, 330],
        [600, 600],
        [1450, 600],
        [1450, 330],
    ])
    image = cv2.polylines(img, [poly], True, (255, 255, 255), 1)  # dibuja la zona de interés en el video principal
    # interes = frame[330:600, 600:1420]
    interes = img[poly[0][1]:poly[0][0], poly[0][0]:poly[3][0]]  # recrota la imagen
    #pasa todo a grises
    imgray = cv2.cvtColor(interes, cv2.COLOR_BGR2GRAY)
    tempGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    """
    ##############################################TEMPLATE 1##############################################
    #######################primero.mp4#######################
    # TM_SQDIFF_NORMED  10%
    # TM_SQDIFF         10%
    # TM_CCOEFF_NORMED  10%
    # TM_CCOEFF         00%
    # TM_CCORR_NORMED   15%
    # TM_CCORR          05%
    #######################segundo.mp4#######################
    # TM_SQDIFF_NORMED  05%
    # TM_SQDIFF         10%
    # TM_CCOEFF_NORMED  00%
    # TM_CCOEFF         00%
    # TM_CCORR_NORMED   05%
    # TM_CCORR          00%
    ##############################################TEMPLATE 2##############################################
    #######################primero.mp4#######################
    # TM_SQDIFF_NORMED  20%
    # TM_SQDIFF         20%
    # TM_CCOEFF_NORMED  00%
    # TM_CCOEFF         00%
    # TM_CCORR_NORMED   00%
    # TM_CCORR          00%
    #######################segundo.mp4#######################
    # TM_SQDIFF_NORMED  90%
    # TM_SQDIFF         90%
    # TM_CCOEFF_NORMED  00%
    # TM_CCOEFF         00%
    # TM_CCORR_NORMED   00%
    # TM_CCORR          00%
    ##############################################TEMPLATE 3##############################################
    #######################primero.mp4#######################
    # TM_SQDIFF_NORMED  00%
    # TM_SQDIFF         00%
    # TM_CCOEFF_NORMED  00%
    # TM_CCOEFF         00%
    # TM_CCORR_NORMED   00%
    # TM_CCORR          00%
    #######################segundo.mp4#######################
    # TM_SQDIFF_NORMED  00%
    # TM_SQDIFF         00%
    # TM_CCOEFF_NORMED  00%
    # TM_CCOEFF         00%
    # TM_CCORR_NORMED   00%
    # TM_CCORR          00%
    #######################tercero.mp4#######################
    # TM_SQDIFF_NORMED  30%
    # TM_SQDIFF         15%
    # TM_CCOEFF_NORMED  00%
    # TM_CCOEFF         00%
    # TM_CCORR_NORMED   00%
    # TM_CCORR          00%
    ##############################################TEMPLATE 4##############################################
    #######################primero.mp4#######################
    # TM_SQDIFF_NORMED  00%
    # TM_SQDIFF         00%
    # TM_CCOEFF_NORMED  00%
    # TM_CCOEFF         00%
    # TM_CCORR_NORMED   00%
    # TM_CCORR          00%
    #######################segundo.mp4#######################
    # TM_SQDIFF_NORMED  00%
    # TM_SQDIFF         00%
    # TM_CCOEFF_NORMED  00%
    # TM_CCOEFF         00%
    # TM_CCORR_NORMED   00%
    # TM_CCORR          00%
    #######################tercero.mp4#######################
    # TM_SQDIFF_NORMED  00%
    # TM_SQDIFF         00%
    # TM_CCOEFF_NORMED  00%
    # TM_CCOEFF         00%
    # TM_CCORR_NORMED   00%
    # TM_CCORR          00%
    ##############################################TEMPLATE X##############################################
    #######################primero.mp4#######################
    # TM_SQDIFF_NORMED  00%
    # TM_SQDIFF         00%
    # TM_CCOEFF_NORMED  00%
    # TM_CCOEFF         00%
    # TM_CCORR_NORMED   00%
    # TM_CCORR          00%
    #######################segundo.mp4#######################
    # TM_SQDIFF_NORMED  00%
    # TM_SQDIFF         00%
    # TM_CCOEFF_NORMED  00%
    # TM_CCOEFF         00%
    # TM_CCORR_NORMED   00%
    # TM_CCORR          00%
    #######################tercero.mp4#######################
    # TM_SQDIFF_NORMED  00%
    # TM_SQDIFF         00%
    # TM_CCOEFF_NORMED  00%
    # TM_CCOEFF         00%
    # TM_CCORR_NORMED   00%
    # TM_CCORR          00%
    """
    result = cv2.matchTemplate(imgray, tempGray, cv2.TM_SQDIFF_NORMED)  #busca la primer coincidencia del template con la imagen original
    minV, maxV, minL, maxL = cv2.minMaxLoc(result)  #obtiene los valores de las coordenadas de la coincidencia
    x1, y1 = minL   #Desempaqueta las coordenadas de minL
    x2, y2 = minL [0] + template.shape[1], minL[1] + template.shape[0]  #obtiene la esquina contraria a x1 y y1 para crear el polígono
    cv2.rectangle(interes, (x1, y1), (x2, y2), (0, 0, 255), 3)  #dibuja el polígono
    # cv2.imshow("Image", img)    #muestra la imagen con el polígono dibujado
    cv2.imshow("Template", template)    #muestra el template
    cv2.imshow("salida", interes)    #muestra el template
    #cierra el programa
    k = 0
    k = cv2.waitKey(1)
    if k == 27:
        break

vdo.release()
cv2.destroyAllWindows()
