from PIL import Image
import sys

#img1= Image.open(input(str("Please enter the File you wish to have all the black pixels removed:")))
#img2= Image.open(input(str("Please enter the File you wish to use to overlap the images black pixels:")))
#img1= Image.open("1.jpg")
#img3 =(input(str("What would like to call your file?:")))

img1=Image.open(sys.argv[1])
img2=Image.open(sys.argv[2])
#img3=Image.open(sys.argv[3]))

print sys.argv[1]
pix1=img1.load()
pix2=img2.load()

imSize1= img1.size
imSize2= img2.size
width =imSize1[0]
height= imSize1[1]
black=(0,0,0)
blackrange=[]
for x in range(13):
 col1=(x,x,x)
 blackrange.append(col1)
 for y in range(13):
     for z in range(13):
         col2=(x,y,z)
         blackrange.append(col2)


finalPic=Image.new("RGB",(width,height),"white")
finalimg=finalPic.load()
print width, height
for x in range(width):
    for y in range(height):
       if pix1[x,y]== black or pix1[x,y] in blackrange:
            finalimg[x,y]=pix2[x,y]
       else:
           finalimg[x,y]=pix1[x,y]
        
finalPic.save(sys.argv[3],"jpeg")
