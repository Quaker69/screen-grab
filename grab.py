import numpy as np
import cv2
from PIL import ImageGrab
import pytesseract

while True:
    img= ImageGrab.grab(bbox=(650,477,1259,543))
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", frame)
    
    #print(pytesseract.image_to_string(('frame')))
    print(pytesseract.image_to_string(img_np))
    if cv2.waitKey(1) & 0Xff == ord('q'):
        break
    
cv2.destroyAllWindows()



