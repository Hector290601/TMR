import cv2

img = cv2.imread("test.png")    #lee la imagen de prueba
template = cv2.imread("template.png")   #lee el template

#pasa todo a grises
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
tempGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

result = cv2.matchTemplate(imgray, tempGray, cv2.TM_SQDIFF_NORMED)  #busca la primer coincidencia del template con la imagen original
minV, maxV, minL, maxL = cv2.minMaxLoc(result)  #obtiene los valores de las coordenadas de la coincidencia

print(minV, maxV, minL, maxL)   #imprime

x1, y1 = minL   #Desempaqueta las coordenadas de minL

x2, y2 = minL [0] + template.shape[1], minL[1] + template.shape[0]  #obtiene la esquina contraria a x1 y y1 para crear el polígono

cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 3)  #dibuja el polígono
cv2.imshow("Image", img)    #muestra la imagen con el polígono dibujado
cv2.imshow("Template", template)    #muestra el template
cv2.waitKey(0)  #sale del programa
cv2.destroyAllWindows()
