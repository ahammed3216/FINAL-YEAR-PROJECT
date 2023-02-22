import cv2
vid=cv2.VideoCapture(0)
i=0
while(i<20):

    ret,image=vid.read()

    cv2.imshow('image',image)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imwrite('image.png',image)
    i=i+1
vid.release()
cv2.destroyAllWindows()