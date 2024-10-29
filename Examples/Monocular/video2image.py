import cv2
import time
import os

cap = cv2.VideoCapture('./IMG_0733.MOV')

if not cap.isOpened():
    print("Video cannot open")
    exit()

frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frame_number = 0

fps = cap.get(cv2.CAP_PROP_FPS)
timestamp = int(time.time()*1000)

f = open("./rgb.txt", "w")
while True:
    ret, frame = cap.read()
    if not ret:
        break

    name = str(int(timestamp+frame_number*1000/fps))
    cv2.imwrite(f'./rgb/{name}.jpg', frame)
    f.write(name[0:-3]+'.'+name[-3:]+" rgb/"+name+".jpg\n")
    frame_number += 1

    if frame_number >= frame_count:
        break

cap.release()
f.close()