f = open('IMG_6437.JPG','rb')

f1 = open('NewImage.JPG','wb')
for image in f:
    f1.write(image)