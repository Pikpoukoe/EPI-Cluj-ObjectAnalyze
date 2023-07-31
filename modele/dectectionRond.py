import cv2
import numpy as np
video_capture = cv2.VideoCapture(0)  # Indice 0 pour la caméra par défaut

distance_objet = 15  # Distance en cm
rayon_objet = 0  # Initialisation du rayon de l'objet

while True:
    # Capture de l'image depuis le flux vidéo
    ret, frame = video_capture.read()
    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Appliquer un flou
    blurred = cv2.GaussianBlur(gray, (15, 15), 0)
    # Détecter les contours
    edges = cv2.Canny(blurred, 50, 150)
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 50, param1=200, param2=30, minRadius=5, maxRadius=100)
    # S'il y a des cercles détectés, mesurer le diamètre de l'objet et montre le cercle
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            # Dessiner le cercle sur l'image
            cv2.circle(frame, (x, y), r, (0, 255, 0), 2)
            # Dessiner le centre du cercle
            cv2.circle(frame, (x, y), 2, (0, 0, 255), 3)

            # Calculer le diamètre de l'objet en pixels
            diametre_pixels = 2 * y

            # Convertir le diamètre en cm en utilisant la relation de taille connue
            diametre_cm = (diametre_pixels / 38)


            # Afficher le diamètre à côté de l'objet
            cv2.putText(frame, f"Diametre: {diametre_cm:.2f} cm", (x - 70, y - r-15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0, 255, 0), 2)

    # Afficher l'image avec les cercles détectés et le diamètre
    cv2.imshow("Objet rond", frame)

    # Quitter la boucle si la touche 'q' est pressée
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Libérer les ressources
video_capture.release()
cv2.destroyAllWindows()
