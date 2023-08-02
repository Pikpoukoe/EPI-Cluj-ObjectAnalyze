# Standard imports
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Set up the detector with parameters
    params = cv2.SimpleBlobDetector_Params()
    params.filterByArea = True
    params.minArea = 1000
    params.filterByCircularity = True
    params.minCircularity = 0.9

    detector = cv2.SimpleBlobDetector_create(params)

    # Webcam
    ret, im = cap.read()
    # Read image
    #im = cv2.imread("assets/circles.jpg")

    # Detect blobs
    keypoints = detector.detect(im)

    # Draw detected blobs as red circles
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    im_with_keypoints = cv2.drawKeypoints(im, [kp.pt for kp in keypoints], np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Show keypoints
    cv2.imshow("Blobs", im_with_keypoints)
    cv2.waitKey(0)

    # Quitter la boucle si 'q' est pressé
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

# When everything done, release the capture
im.release()
cv2.destroyAllWindows()
