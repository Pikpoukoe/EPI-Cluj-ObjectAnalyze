import cv2
import numpy as np

# Ouvrir le flux vidéo de la webcam
cap = cv2.VideoCapture(0)

while (True):
    # Capturer une image par image
    frame = cap.read()
    # Convertir l'image en gris
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Appliquer un flou pour réduire le bruit
    gray_blur = cv2.GaussianBlur(gray, (15, 15), 0)

    # Détecter les cercles avec la transformation de Hough
    circles = cv2.HoughCircles(gray_blur, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

    # Vérifier si on a détecté des cercles
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # Dessiner le cercle extérieur
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # Dessiner le centre du cercle
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)

    # Afficher l'image avec les cercles
    cv2.imshow('frame', frame)

    # Quitter la boucle si 'q' est pressé
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()