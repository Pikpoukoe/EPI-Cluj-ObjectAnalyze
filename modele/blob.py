import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    frame = cap.read()

    detector = cv2.SimpleBlobDetector()

    # Detect blobs.
    keypoints = detector.detect(frame)

    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    frame_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Show keypoints
    cv2.imshow("Keypoints", frame_with_keypoints)
    cv2.waitKey(0)
    
    # Quitter la boucle si 'q' est pressé
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()