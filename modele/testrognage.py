"""import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)  # Indice 0 pour la caméra par défaut
distance_objet = 15  # Distance en cm
nbPixelsPour1Cm = 50 # nombre de pixel pour 1cm de large a 15cm de la camera
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
            diametre_pixels = 2 * r
            # Convertir le diamètre en cm en utilisant la relation de taille connue
            diametre_cm = ((diametre_pixels*15) / (nbPixelsPour1Cm*distance_objet))
            # Afficher le diamètre à côté de l'objet
            cv2.putText(frame, f"Diametre: {diametre_cm:.2f} cm", (x - 70, y - r-15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0, 255, 0), 2)
            # Créer un masque circulaire pour extraire le contenu du cercle
            cv2.circle(frame, (x, y), r, 255, -1)



    # Afficher l'image avec les cercles détectés et le diamètre
    cv2.imshow("Objet rond", frame)
    # Quitter la boucle si la touche 'q' est pressée
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
# Libérer les ressources
video_capture.release()
cv2.destroyAllWindows()
"""
import cv2

# Ouvrir la capture vidéo à partir de la caméra (0 pour la caméra par défaut)
video_capture = cv2.VideoCapture(0)

is_paused = False

while True:
    # Si la lecture n'est pas en pause, lisez une image frame depuis la vidéo
    if not is_paused:
        ret, frame = video_capture.read()

        # Assurez-vous que la lecture de la vidéo se déroule correctement
        if not ret:
            break

        # Afficher l'image frame (vidéo en temps réel)
        cv2.imshow('Video en temps réel', frame)

    # Attendre une touche pour décider de mettre en pause ou reprendre la vidéo
    key = cv2.waitKey(1)
    if key == ord('p'):
        is_paused = not is_paused  # Mettre en pause ou reprendre la lecture
    elif key == ord('q'):
        break

# Relâchez la capture vidéo et fermez la fenêtre
video_capture.release()
cv2.destroyAllWindows()

