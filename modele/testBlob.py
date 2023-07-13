# Standard imports
import cv2
import numpy as np;
 

while(True):
    # Read image
    im = cv2.imread("/assets/circles.jpg")
    
    # Set up the detector with default parameters.
    detector = cv2.SimpleBlobDetector()
    
    # Detect blobs.
    keypoints = detector.detect(im)
    
    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    #im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    # Show keypoints
    cv2.imshow("Keypoints", keypoints)
    cv2.waitKey(0)

    # Quitter la boucle si 'q' est pressé
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # When everything done, release the capture
im.release()
cv2.destroyAllWindows()