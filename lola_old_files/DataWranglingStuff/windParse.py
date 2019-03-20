import numpy as np

def main():
 infile = open('windTry0000.obj','r')
 outfile=open('winTryPython.obj','w')
 getSize=0
 tempArray =[]
 for line in infile:
  getSize +=1
  temp = line.strip().split(" ")
  tempArray.append(temp)
  outfile.write(line)
 countVert=0
 for i in range(getSize):
  for j in range(len(tempArray[i])):
   if j!=0:
    countVert +=1
 for m in range(countVert):
   if int(m+1) % 3 == 0 and m !=0:
     faceLine="f"+" "+str(int(m-2))+" "+str(int(m-1))+" "+str(int(m))+"\n"
     outfile.write(faceLine)
    #print(tempArray[i][j])
 print(getSize)
 print(len(tempArray))
 print(tempArray[2][3])
 print(countVert)
 outfile.close()
 infile.close()


 '''
 #Reading the VTK Binary File from Paraview(look up PVFileConversion.txt for instructions) into a Numpy Array
  infile = np.fromfile('windVel2.vtk', dtype=np.float32, count=-1)
  outfile= open('windStreamlines4.obj','w')
  outfile.write("# wavefront obj file written by VisIt"+"\n"+"\n")
  #infile2= np.fromfile('qi.obj', dtype=np.float32, count=-1) reference file for writing OBJ File
 
  #Setting Up Vertices Array for OBJ
  splitWind = len(infile) / 5
  wind1= np.split(infile,splitWind)
  print(len(wind1))
  print(len(infile))
  print(wind1[3])
  faceSide = 1
  for i in range(len(wind1)):
    temp = str("v")+" "
    for j in range(len(wind1[i])):
     temp +=str(wind1[i][j])+" "
    temp+="\n"
    outfile.write(temp)
  for i in range(len(wind1)):
    temp = str('f')+" "
    for j in range(len(wind1[i])):
     temp +=str(faceSide)+" "
     faceSide += 1
    temp+="\n"
    outfile.write(temp)
  outfile.close()
  
    
  
   #temp = line.strip().split(",")
   #windStreamlinesArray.append(temp)
  #print(len(windStreamlinesArray))
   #print(temp)
   #for j in range(len(line)):
    # windStreamlinesArray.append(temp)
  
  print((windStreamlinesArray[11]))
  #print(len(windStreamlinesArray))
  
 for i in range(10, 15):
   Objstr = "v"+" "+str(windStreamlinesArray[i])+" "+str(windStreamlinesArray[i+1])+" "+
   print(Objstr)
  for line in infile2:
    windStreamlinesArray.append(line)
  '''
  #print("The others are")
  #print(windStreamlinesArray[0])
  #print(windStreamlinesArray[1])
  #print(windStreamlinesArray[2])
  
 
main()
