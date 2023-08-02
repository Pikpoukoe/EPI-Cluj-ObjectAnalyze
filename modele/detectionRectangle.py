import cv2
import numpy as np

# Ouvrir la vidéo à partir d'un fichier (ou laisser l'index à 0 pour la caméra)
cap = cv2.VideoCapture(0)

while True:
    # Lecture de la frame
    ret, frame = cap.read()

    if not ret:
        break

    # Conversion de l'image en niveaux de gris
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Filtrage d'image pour réduire le bruit
    blurred = cv2.medianBlur(gray, 15)

    # Détection de contours
    edges = cv2.Canny(blurred, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Approximation de polygone pour obtenir le nombre de côtés
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Si le contour a 4 côtés (rectangle)
        if len(approx) == 4:
            # Calculer les dimensions du rectangle englobant
            x, y, w, h = cv2.boundingRect(contour)
            aspect_ratio = float(w) / h

            # Vérifier si l'aspect ratio est proche de 1 (carré ou rectangle)
            if 0.9 < aspect_ratio < 1.1:
                # Dessiner le rectangle autour du carré sur l'image originale
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Afficher la vidéo avec les rectangles détectés
    cv2.imshow('Rectangles Detection', frame)

    # Quitter la boucle si la touche 'q' est pressée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la capture vidéo et fermer les fenêtres
cap.release()
cv2.destroyAllWindows()
