import cv2
import controller2 as cnt
import numpy as np

model=model_path="tinyml_model.tflite"
cap=cv2.VideoCapture(0)
def cropImage(img,offset):
    h,w,c=img.shape
    imgCrop=img[offset:h-offset,offset:w-offset]
    cv2.rectangle(img,(offset,offset),(w-offset,h-offset),(200,0,200),3)
    cv2.imshow("ImageCrop",imgCrop)
    return imgCrop

def averageColor(img):
    avgColorPerRow=np.average(img,axis=0)
    avgColor=np.average(avgColorPerRow,axis=0)
    myColor=(int(avgColor[2]),int(avgColor[1]),int(avgColor[0]))
    return myColor

while True:
    _,img=cap.read()
    imgCrop=cropImage(img,100)
    myColor=averageColor(imgCrop)
    print(myColor)
    cnt.led(myColor)
    cv2.imshow("Image",img)
    k=cv2.waitKey(1)
    if k==ord("k"):
        break

cap.release()
cv2.destroyAllWindows()
