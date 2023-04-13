import GoldenFace
import cv2
vid = cv2.VideoCapture(0)
while(True):
    ret, image = vid.read()
    
    cv2.imshow('image',image)
    
    if cv2.waitKey(1) & 0xFF ==ord(' '):
        break
    cv2.imwrite("test.png",image)
    
#vid.release()
#cv2.destroyAllWindows()

vid = cv2.VideoCapture(0)
while(True):
    ret, image = vid.read()
    
    cv2.imshow('image',image)
    
    if cv2.waitKey(1) & 0xFF ==ord(' '):
        break
    cv2.imwrite("test1.png",image)
    
#vid.release()
#cv2.destroyAllWindows()

vid = cv2.VideoCapture(0)
while(True):
    ret, image = vid.read()
    
    cv2.imshow('image',image)
    
    if cv2.waitKey(1) & 0xFF ==ord(' '):
        break
    cv2.imwrite("test2.png",image)
     
vid.release()
cv2.destroyAllWindows()



color_a = (255,255,0)
color_b = (0,0,255 )

analysis = GoldenFace.goldenFace("test.png")
analysis.drawFaceCover(color_a)
cv2.imshow("Image",analysis.img)
key = cv2.waitKey(1000)
 
analysis = GoldenFace.goldenFace("test.png")
goldenRatio = analysis.geometricRatio()

analysis1 = GoldenFace.goldenFace("test1.png")
goldenRatio1 = analysis1.geometricRatio()

analysis2 = GoldenFace.goldenFace("test2.png")
goldenRatio2 = analysis2.geometricRatio()


text = "Your Face is " + str(int((int(goldenRatio)+int(goldenRatio1)+int(goldenRatio2))/3)) + "% Symmetric."

image = cv2.putText(analysis.img, text, (0,450), cv2.FONT_HERSHEY_SIMPLEX, 1, color_b, 2)
cv2.imshow("Image",analysis.img)
key = cv2.waitKey(1000)

