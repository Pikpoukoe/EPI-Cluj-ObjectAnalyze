import cv2

# Ouvre le flux vidéo de la webcam
cap = cv2.VideoCapture(0)

# Vérifie si la webcam est ouverte avec succès
if not cap.isOpened():
    print("Erreur lors de l'ouverture de la webcam")
    exit()

while True:
    # Cature image par image le flux vidéo
    ret, frame = cap.read()

    if ret:
        # Convertis le flux vidéo en gris
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Appliquer un flou pour réduire le bruit
        blurred = cv2.GaussianBlur(gray, (15, 25), 0)

        # Appliquer la détection de contours
        edges = cv2.Canny(blurred, 50, 150)

        # Trouver les contours dans l'image
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Dessiner les contours sur l'image originale
        cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

        # Afficher l'image avec les contours détectés
        cv2.imshow("Contours", frame)

    # Quitte la boucle si la touche 'q' est pressée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libère le flux vidéo
cap.release()

# Ferme toutes les fenêtres générées
cv2.destroyAllWindows()
