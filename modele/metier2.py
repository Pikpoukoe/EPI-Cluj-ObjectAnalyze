import cv2
import numpy as np

# Ouvre le flux vidéo de la webcam
cap = cv2.VideoCapture(0)

# Vérifie si la webcam est ouverte avec succès
if not cap.isOpened():
    print("Erreur lors de l'ouverture de la webcam")
    exit()

while True:
    # Capture image par image le flux vidéo
    ret, frame = cap.read()

    if ret:
        # Convertis le flux vidéo en gris
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Appliquer un flou pour réduire le bruit
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Appliquer la détection de cercles avec la transformation de Hough
        circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 20,
                                   param1=50, param2=30, minRadius=10, maxRadius=50)

        # Vérifie si des cercles ont été détectés
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for circle in circles[0, :]:
                center = (circle[0], circle[1])
                radius = circle[2]
                # Dessine le cercle sur l'image originale
                cv2.circle(frame, center, radius, (0, 255, 0), 2)

        # Afficher l'image avec les cercles détectés
        cv2.imshow("Cercles", frame)

    # Quitte la boucle si la touche 'q' est pressée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libère le flux vidéo
cap.release()

# Ferme toutes les fenêtres générées
cv2.destroyAllWindows()
