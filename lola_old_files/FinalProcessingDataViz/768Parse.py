#Read open



iNS1= []
iNS2= []
iNS3= []
iNS4=[]
iNS5=[]
infile=open("768.csv","r")
for i in range(12):
    infile.readline()


for line in infile:
   temp= line.strip().split(",")
   for i in range(5):
    if i ==0:
     tempList1=[]
     tempList1.append(temp[6])
     tempList1.append(temp[1])
     iNS1.append(tempList1)
    elif i ==1:
     tempList2=[]
     tempList2.append(temp[6])
     tempList2.append(temp[2])
     iNS2.append(tempList2)
    elif i==2:
     tempList3=[]
     tempList3.append(temp[6])
     tempList3.append(temp[3])
     iNS3.append(tempList3)
    elif i==3:
     tempList4=[]
     tempList4.append(temp[6])
     tempList4.append(temp[4])
     iNS4.append(tempList4)
    else:
      tempList5=[]
      tempList5.append(temp[6])
      tempList5.append(temp[5])
      iNS5.append(tempList5)
print(iNS1)
print(iNS2)
print(iNS3)
print(iNS4)
print(iNS5)
outfile = open("Init_1stParam.txt","w")
for i in range(len(iNS1)):
    valStr=""
    valStr= str(iNS1[i][0])+"\t"+str(iNS1[i][1])
    outfile.write(str(valStr)+"\n")
infile.close()
outfile.close()
    
file
