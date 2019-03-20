import os
import numpy as np
global GridXArray
def main():
  
  # User Inputs the two files that they want into their array
  print("This file will ask you to input two files. Make sure that you have your file wrapped in 'filename.extension'. Also, please input your desired timestep, when prompted. Make sure you input the largest file first, then the smallest.")
  infile1 = open(input(str("Please enter the name of the first file you wish to open:")),"r")
  infile2 = open(input(str("Please enter the name of the second file you wish to open:")),"r")
  timestep= (input("Please Enter the Timestep number for the file:"))

  file1 = np.fromfile(infile1, dtype=np.float32, count =-1)
  file2 = np.fromfile(infile2, dtype=np.float32, count =-1)

  #Split the ARRAYS to be functional for the grids
  #f1 will have 66049 Rows with 257 values, f2 will have 16705 rows with 65 values
  f1= np.split(file1,66049)
  f2= np.split(file2 ,16705)

  #Setting Up 3 different arrays for each axis
  GridX=[]
  #GridY=[]
  #GridZ=[]
  
  # Lay is short for layers, creates each axis for the layers
  for lay in range (257):
      
    #Does the Fill Up computation for the X Axis
    for i in range(65):
      for k in range(len(f1[i])):
       GridX.append(f1[i+(257*lay)][k])
      #print([i+(257*lay)])
      for j in range (100):
       GridX.append('0')
      for l in range(len(f2[i])):
          GridX.append(f2[i+(65*lay)][l])
    for i in range(192):
     for k in range(len(f1[i])):
       GridX.append(f1[(i+65)+(257*lay)][k])
     for j in range (165):
       GridX.append('0')

  # Printing the Grids and index is to Make sure that the correct amount of Array Entries are in there
  print(len(GridX))
  #print(len(GridY))
  print(GridX[422])
  
  #Writes the X axis array to a file in 32 bit float format
  GridXFile = open("GridX300File.raw", "wb")
  x= np.asfarray(GridX)
  x.astype('float32').tofile(GridXFile)





main()

