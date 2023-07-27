import cv2
import numpy as np
video_capture = cv2.VideoCapture(0)  # Indice 0 pour la caméra par défaut

while True:
    # Capture de l'image depuis le flux vidéo
    ret, frame = video_capture.read()

    # Détection des blobs dans l'image
    blobs = blob_detector.detect(frame)

    # Création d'une image noire pour afficher uniquement les lignes entre les changements de couleur
    black_image = np.zeros_like(frame)

    # Dessin des contours des blobs sur l'image noire
    cv2.drawContours(black_image, blobs, -1, (0, 255, 0), 2)

    # Afficher l'image résultante
    cv2.imshow('Lignes entre les changements de couleur', black_image)

    # Quitter la boucle si la touche 'q' est pressée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer les ressources
video_capture.release()
cv2.destroyAllWindows()
