import cv2
import numpy as np
import matplotlib as plt
image = np.full((512, 512, 3), 255, np.uint8)
image = cv2.putText(image, 'hello world',(0,200), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (255,0,0))

cv2.imshow("Image", image)
cv2.waitKey(0)