import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
img = cv2.imread('4.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 2)
print(faces)
for (x,y,w,h) in faces:
    print("Detected Face")
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
         
    eyes = eye_cascade.detectMultiScale(roi_gray)
    print("Eyes", eyes)
    if eyes is ():
        print("eyes closed")
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),1)
cv2.imshow('FACE EYE DETECTION',img)
cv2.waitKey(0)
cv2.destroyAllWindows()