#bibliotecas
import numpy as np
import cv2

#cargamos el clasificador de cascada
sign_cascade = cv2.CascadeClassifier('haarCascade.xml')

#prueba si reconoce el objeto
img = cv2.imread('90-velocidad.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sign = sign_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in sign:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
