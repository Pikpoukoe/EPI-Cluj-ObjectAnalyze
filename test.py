import cv2
import numpy as np

# Capture vidéo depuis la caméra (0 pour la caméra par défaut, mais vous pouvez changer cela en fonction de votre configuration)
cap = cv2.VideoCapture(0)

while True:
    # Lire une image depuis la caméra
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Appliquer une détection de cercles à l'image
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=200, param2=30, minRadius=5, maxRadius=100)

    # Si des cercles sont détectés
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        # Dessiner les cercles sur l'image
        for (x, y, r) in circles:
            cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

            # Mesurer le diamètre du cercle
            diameter = 2 * r

            # Afficher la mesure sur l'image
            cv2.putText(frame, f"Diamètre: {diameter} pixels", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Afficher l'image
    cv2.imshow("Object Dimension Measurement", frame)

    # Quitter si la touche 'q' est pressée
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Libérer les ressources et fermer les fenêtres
cap.release()
cv2.destroyAllWindows()
