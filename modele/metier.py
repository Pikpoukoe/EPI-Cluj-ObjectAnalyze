import cv2
import numpy as np

# Ouvre le flux vidéo de la webcam
cap = cv2.VideoCapture(0)

# Boucle principale pendant que le flux vidéo est ouvert
while cap.isOpened():
    # Cature image par image le flux vidéo
    ret, frame = cap.read()

    # Obtention du nb de fps (30 fixe à confirmer)
    fps = cap.get(cv2.CAP_PROP_FPS)

    if ret == True:

        # Quitte la boucle si la touche 'q' est pressée
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Convertis le flux vidéo en gris
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Texte dans l'angle supérieur gauche
        gray_text = cv2.putText(gray, "Mode gris", (20, 40), cv2.FONT_ITALIC, 1, (0, 0, 0), 5)


        # Tt ça bug qd on décommente c'est à refractorer avec notre nouvelle architecture
        # Détecte les cercles grâce à la transformation de Hough
        #circles = cv2.HoughCircles(gray_text, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

        # Vérifie si on a détecté des cercles
        #if circles is not None:
        #    circles = np.uint16(np.around(circles))
        #    for i in circles[0, :]:
                # Dessine le cercle en vert
        #        cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
                # Pointe le centre du cercle en rouge
        #        cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)


        # Affiche la fenêtre
        cv2.imshow('frame', gray)
    else:
        break

# Après l'arrêt, montre le nombre de fps de la séquence
print(fps)

# Libère le flux vidéo
cap.release()

# Ferme toutes les fenêtres générées
cv2.destroyAllWindows()
