import os
import cv2

path = "C:/Users/Admin/Documents/JV/Projeto-105/Images/"

images = []

for i in os.listdir(path):
    
    name, end = os.path.splitext(i)


    if end in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+i

        images.append(file_name)

count = len(images)

frame = cv2.imread(images[0])

height, width, channels = frame.shape
size = (width, height)
out = cv2.VideoWriter("Projeto.avi", cv2.VideoWriter_fourcc(*"DIVX"), 0.8, size)

for i in range(0, count -1):
    frame = cv2.imread(images[i])

    out.write(frame)

print("Concluído")