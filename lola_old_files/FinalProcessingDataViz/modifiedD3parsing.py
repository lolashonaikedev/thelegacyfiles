import operator
def main():
    #opens the files to read the solution score and Logs
    infile1 = open("Solution_Score.csv", "r")
    infile2 = open("Logs.csv", "r")
    ARScore = []
    ARTable = []
    ARSname= {}
    ARTname={}
    #Count How .Many Students have each Solution to put in D3.js circle
    infile1.readline()
    infile2.readline()
    for line in infile1:
      temp = line.strip().split(",")
      ARScore.append(temp)
      ARSname[str(temp[0])]= int(temp[1])
    #create a Solution Count Score Dictionary to be used to create the Partions for the circle in D3.
    countNull = 0
    count0 = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
   # print(len(ARScore))
    for i in range(0,len(ARScore)):
      if int(ARScore[i][1]) == 0:
          count0 +=1
      if int(ARScore[i][1]) == 1:
          count1 +=1
      if int(ARScore[i][1]) == 2:
          count2 +=1
      if int(ARScore[i][1]) == 3:
          count3 +=1
      if int(ARScore[i][1]) == 4:
          count4 +=1
      if int(ARScore[i][1]) == 5:
          count5 += 1
      if int(ARScore[i][1]) == 6:
          count6 += 1
    #print(count0,count1,count2,count3,count4,count5,count6)
    #This Parses out data that doesn't belong in one of the six tools
    for line in infile2:
        temp = line.strip().split(",")
        ARTname[str(temp[0])]= ""
        if (temp[1] == "solar system"):
            ARTable.append(temp)
        if (temp[1] == "alien database"):
            ARTable.append(temp)
        if (temp[1] == "mission control"):
            ARTable.append(temp)
        if (temp[1] == "notebook"):
            ARTable.append(temp)
        if (temp[1] == "probe launch"):
           ARTable.append(temp)
        if (temp[1] =="probe design"):
          ARTable.append(temp)
   #Junk Code but for some reason, if I take it out, it cause scripting errors 
    for key in ARTname:
      if key not in ARSname:
          countNull += 1
    maxList=[]
    for key in ARTname:
        templist=list()
        for i in range(len(ARTable)):
          if key == ARTable[i][0]:
              choice = ARTable[i][1]
              templist.append(choice)
              ARTname[key]= templist
        maxList.append(len(ARTname.get(key)))
    maxChoice= max(maxList)
  #Do not delete the junk code up to here

 #*******Initializing the ARD3 data for the Circos software and also for pattern manipulation*******

    ARD3= [["Students","Score"]]
    #Create the Column Row to be implemented in D3.js
    for i in range(maxChoice):
       colStr = str("Decision")+str(i+1)
       ARD3[0].append(colStr)
    
    #print(len(ARTname.get("sciencebook")))
    for key in ARTname:
        tempList1=[]
        reaList=[]
        reaList.append(key)
        tempList1.append(ARTname.get(key))
        if key in ARSname:
           reaList.append(ARSname.get(key))
        else:
           reaList.append("null")
           #print(key)
        for j in range(len(tempList1[0])) :
            reaList.append(tempList1[0][j])
        ARD3.append(reaList)
    
    #Set Up A 2DList to Store all the Students decisions that will be later saved into a dictionary
    #Max values are stored for research purposes
    pattern0,pattern1,pattern2,pattern3,pattern4,pattern5,pattern6= getPatNumList(ARD3,0),getPatNumList(ARD3,1),getPatNumList(ARD3,2),getPatNumList(ARD3,3),getPatNumList(ARD3,4),getPatNumList(ARD3,5),getPatNumList(ARD3,6)
    maxPat0,maxPat1,maxPat2,maxPat3,maxPat4,maxPat5,maxPat6 = getMax(pattern0),getMax(pattern1),getMax(pattern2),getMax(pattern3),getMax(pattern4),getMax(pattern5),getMax(pattern6)
    pop0,pop1,pop2,pop3,pop4,pop5,pop6= popularLine(pattern0),popularLine(pattern1),popularLine(pattern2),popularLine(pattern3),popularLine(pattern4),popularLine(pattern5),popularLine(pattern6)
    pops0,pops1,pops2,pops3,pops4,pops5,pops6= popularLine3(pattern0),popularLine3(pattern1),popularLine3(pattern2),popularLine3(pattern3),popularLine3(pattern4),popularLine3(pattern5),popularLine3(pattern6)
    #print(maxPat0,maxPat1,maxPat2,maxPat3,maxPat4,maxPat5,maxPat6)
    pop0,pop1,pop2,pop3,pop4,pop5,pop6=pop0.split(","),pop1.split(","),pop2.split(","),pop3.split(","),pop4.split(","),pop5.split(","),pop6.split(",")
    #print("For Score 0, the popular 3 is,"
    print pop5
    toolsList = ['solar system', 'alien database','mission control','notebook','probe launch','probe design']
    popList=[pop0,pop1,pop2,pop3,pop4,pop5,pop6]
    popFile=open("solutionPath.csv","w")
    decisionList=["Score"]
    for i in range(50):
        dStr="Decision" +str(i+1)
        decisionList.append(dStr)
    firstRowStr=""
    for i in range(len(decisionList)):
        if i !=49:
          firstRowStr+=str(decisionList[i])+","
        else:
          firstRowStr+=str(decisionList[i])
    for i in range(len(decisionList)):
        popFile.write(str(decisionList[i])+",")
    for i in range(len(popList)):
       pstr="\n"+str(i)+","
       for j in range(len(popList[i])):
        if j!=len(popList[i])-1:
          pstr+=str(popList[i][j])+","
        else:
          pstr+=str(popList[i][j])+"\n"
       popFile.write(pstr)
    outfile=open("ARPOP.txt","w")
    
    for i in range(len(pop0)):
          #posLine = -(7*i)
          posLine=25*i
          strokeCol=""
          if pop0[i] == "alien database":
             strokeCol ="#348899"
            #strokeCol = "#FF0033" #red
          if pop0[i] == "solar system":
            #strokeCol = "#00FF00" #green
             strokeCol ="#FFD34E"
          if pop0[i] == "probe launch":
             strokeCol="#979C9C"
            #strokeCol = "#0000FF" #darkBlue
          if pop0[i] == "notebook":
             strokeCol="#343642"
             #strokeCol = "#FF9900"#orange
          if pop0[i] == "mission control":
             strokeCol="#962D3E"
             #strokeCol = "#9900FF"
          if pop0[i] == "probe design":
             strokeCol="#A2EB8F"
            #strokeCol = "#FF6666"#pinkish
          if pop0[i] == "0":
             strokeCol = "white"

          #Check Example Student User SVG for now
         #For Rectangles
          lineStr="<rect x=\"250\" y=\"0\" width=\"15\" height=\"50\" transform=\"translate("+str(posLine)+",0)\""+"  style=\"fill:"+strokeCol+";stroke-width:1;stroke:rgb(0,0,0)\" />"

 
          #lineStr="<ellipse id=\"pop1\" cx=\"500px\" cy=\"400\" rx=\"50\" ry=\"2.5\" transform=\"translate(0,"+str(posLine)+")\""+" style=\" stroke:"+strokeCol+"; stroke-width:0.5; fill:"+strokeCol+";\"/>"  
          outfile.write(str(lineStr)+"\n")
   # outfile.close()

    for i in range(len(pop1)):
          #posLine = -(7*i)
          posLine = 25*i
          strokeCol=""
          if pop1[i] == "alien database":
             strokeCol ="#348899"
            #strokeCol = "#FF0033" #red
          if pop1[i] == "solar system":
            #strokeCol = "#00FF00" #green
             strokeCol ="#FFD34E"
          if pop1[i] == "probe launch":
             strokeCol="#979C9C"
            #strokeCol = "#0000FF" #darkBlue
          if pop1[i] == "notebook":
             strokeCol="#343642"
             #strokeCol = "#FF9900"#orange
          if pop1[i] == "mission control":
             strokeCol="#962D3E"
             #strokeCol = "#9900FF"
          if pop1[i] == "probe design":
             strokeCol="#A2EB8F"
            #strokeCol = "#FF6666"#pinkish
          if pop1[i] == "0":
             strokeCol = "white"

          #Check Example Student User SVG for now
           #For Rectangles
          lineStr="<rect x=\"250\" y=\"115\" width=\"15\" height=\"50\" transform=\"translate("+str(posLine)+",0)\""+"  style=\"fill:"+strokeCol+";stroke-width:1;stroke:rgb(0,0,0)\" />"

          #lineStr="<ellipse id=\"pop1\" cx=\"560px\" cy=\"440\" rx=\"50\" ry=\"4\" transform=\" rotate(45,580,460) translate(0,"+str(posLine)+")\""+" style=\" stroke:"+strokeCol+"; stroke-width:0.5; fill:"+strokeCol+";\"/>"  
          outfile.write(str(lineStr)+"\n")
    #outfile.close()
    
    for i in range(len(pop2)):
          #posLine = (7*i)
          posLine=25*i
          strokeCol=""
          if pop2[i] == "alien database":
             strokeCol ="#348899"
            #strokeCol = "#FF0033" #red
          if pop2[i] == "solar system":
            #strokeCol = "#00FF00" #green
             strokeCol ="#FFD34E"
          if pop2[i] == "probe launch":
             strokeCol="#979C9C"
            #strokeCol = "#0000FF" #darkBlue
          if pop2[i] == "notebook":
             strokeCol="#343642"
             #strokeCol = "#FF9900"#orange
          if pop2[i] == "mission control":
             strokeCol="#962D3E"
             #strokeCol = "#9900FF"
          if pop2[i] == "probe design":
             strokeCol="#A2EB8F"
            #strokeCol = "#FF6666"#pinkish
          if pop2[i] == "0":
             strokeCol = "white"

          #Check Example Student User SVG for now
            #For Rectangles
          lineStr="<rect x=\"250\" y=\"235\" width=\"15\" height=\"50\" transform=\"translate("+str(posLine)+",0)\""+"  style=\"fill:"+strokeCol+";stroke-width:1;stroke:rgb(0,0,0)\" />"

          #lineStr="<ellipse id=\"pop1\" cx=\"610px\" cy=\"560\" rx=\"50\" ry=\"4\" transform=\" rotate(-90,580,540) translate(0,"+str(posLine)+")\""+" style=\" stroke:"+strokeCol+"; stroke-width:0.5; fill:"+strokeCol+";\"/>"  
          outfile.write(str(lineStr)+"\n")
    #outfile.close()
     
    for i in range(len(pop3)):
          #posLine = (7*i)
          posLine=25*i
          strokeCol=""
          if pop3[i] == "alien database":
            strokeCol ="#348899"
            #strokeCol = "#FF0033" #red
          if pop3[i] == "solar system":
            #strokeCol = "#00FF00" #green
             strokeCol ="#FFD34E"
          if pop3[i] == "probe launch":
             strokeCol="#979C9C"
            #strokeCol = "#0000FF" #darkBlue
          if pop3[i] == "notebook":
             strokeCol="#343642"
             #strokeCol = "#FF9900"#orange
          if pop3[i] == "mission control":
             strokeCol="#962D3E"
             #strokeCol = "#9900FF"
          if pop3[i] == "probe design":
             strokeCol="#A2EB8F"
            #strokeCol = "#FF6666"#pinkish
          if pop3[i] == "0":
             strokeCol = "white"
          #Check Example Student User SVG for now
            #For Rectangles
          lineStr="<rect x=\"250\" y=\"360\" width=\"15\" height=\"50\" transform=\"translate("+str(posLine)+",0)\""+"  style=\"fill:"+strokeCol+";stroke-width:1;stroke:rgb(0,0,0)\" />"

          #lineStr="<ellipse id=\"pop1\" cx=\"550px\" cy=\"580\" rx=\"50\" ry=\"4\" transform=\" rotate(-45,560,580) translate(0,"+str(posLine)+")\""+" style=\" stroke:"+strokeCol+"; stroke-width:0.5; fill:"+strokeCol+";\"/>"  
          outfile.write(str(lineStr)+"\n")
   # outfile.close()
   
    for i in range(len(pop4)):
          #posLine = (7*i)
          posLine=25*i        
          strokeCol=""
          if pop4[i] == "alien database":
             strokeCol ="#348899"
            #strokeCol = "#FF0033" #red
          if pop4[i] == "solar system":
            #strokeCol = "#00FF00" #green
             strokeCol ="#FFD34E"
          if pop4[i] == "probe launch":
             strokeCol="#979C9C"
            #strokeCol = "#0000FF" #darkBlue
          if pop4[i] == "notebook":
             strokeCol="#343642"
             #strokeCol = "#FF9900"#orange
          if pop4[i] == "mission control":
             strokeCol="#962D3E"
             #strokeCol = "#9900FF"
          if pop4[i] == "probe design":
             strokeCol="#A2EB8F"
            #strokeCol = "#FF6666"#pinkish
          if pop4[i] == "0":
             strokeCol = "white"
          #Check Example Student User SVG for now
          #For Rectangles
          lineStr="<rect x=\"250\" y=\"485\" width=\"15\" height=\"50\" transform=\"translate("+str(posLine)+",0)\""+"  style=\"fill:"+strokeCol+";stroke-width:1;stroke:rgb(0,0,0)\" />"


          #lineStr="<ellipse id=\"pop1\" cx=\"460px\" cy=\"600\" rx=\"50\" ry=\"4\" transform=\" rotate(25,470,610) translate(0,"+str(posLine)+")\""+" style=\" stroke:"+strokeCol+"; stroke-width:0.5; fill:"+strokeCol+";\"/>"  
          outfile.write(str(lineStr)+"\n")
    #outfile.close()
    
    for i in range(len(pop5)):
          #posLine = (7*i)
           
          posLine=25*i
          strokeCol=""
          if pop5[i] == "alien database":
             strokeCol ="#348899"
            #strokeCol = "#FF0033" #red
          if pop5[i] == "solar system":
            #strokeCol = "#00FF00" #green
             strokeCol ="#FFD34E"
          if pop5[i] == "probe launch":
             strokeCol="#979C9C"
            #strokeCol = "#0000FF" #darkBlue
          if pop5[i] == "notebook":
             strokeCol="#343642"
             #strokeCol = "#FF9900"#orange
          if pop5[i] == "mission control":
             strokeCol="#962D3E"
             #strokeCol = "#9900FF"
          if pop5[i] == "probe design":
             strokeCol="#A2EB8F"
            #strokeCol = "#FF6666"#pinkish
          if pop5[i] == "0":
             strokeCol = "white"

          #Check Example Student User SVG for now
          #For Rectangles
          lineStr="<rect x=\"250\" y=\"610\" width=\"15\" height=\"50\" transform=\"translate("+str(posLine)+",0)\""+"  style=\"fill:"+strokeCol+";stroke-width:1;stroke:rgb(0,0,0)\" />"

          #lineStr="<ellipse id=\"pop1\" cx=\"410px\" cy=\"540\" rx=\"50\" ry=\"4\" transform=\" rotate(75,420,530) translate(0,"+str(posLine)+")\""+" style=\" stroke:"+strokeCol+"; stroke-width:0.5; fill:"+strokeCol+";\"/>"  
          outfile.write(str(lineStr)+"\n")
    #outfile.close()
    
    for i in range(len(pop6)):
          #posLine = -(7*i)
          posLine=25*i
          strokeCol=""
          if pop6[i] == "alien database":
             strokeCol ="#348899"
            #strokeCol = "#FF0033" #red
          if pop6[i] == "solar system":
            #strokeCol = "#00FF00" #green
             strokeCol ="#FFD34E"
          if pop6[i] == "probe launch":
             strokeCol="#979C9C"
            #strokeCol = "#0000FF" #darkBlue
          if pop6[i] == "notebook":
             strokeCol="#343642"
             #strokeCol = "#FF9900"#orange
          if pop6[i] == "mission control":
             strokeCol="#962D3E"
             #strokeCol = "#9900FF"
          if pop6[i] == "probe design":
             strokeCol="#A2EB8F"
            #strokeCol = "#FF6666"#pinkish
          if pop6[i] == "0":
             strokeCol = "white"
          #Check Example Student User SVG for now
          #For Rectangles
          lineStr="<rect x=\"250\" y=\"735\" width=\"15\" height=\"50\" transform=\"translate("+str(posLine)+",0)\""+"  style=\"fill:"+strokeCol+";stroke-width:1;stroke:rgb(0,0,0)\" />"

          #lineStr="<ellipse id=\"pop1\" cx=\"400px\" cy=\"450\" rx=\"50\" ry=\"4\" transform=\" rotate(-65,400,430) translate(0,"+str(posLine)+")\""+" style=\" stroke:"+strokeCol+"; stroke-width:0.5; fill:"+strokeCol+";\"/>"  
          outfile.write(str(lineStr)+"\n")
    outfile.close()

'''
def popularLine3(pattern):
 realMax=""
 tempdict={}
 for i in range(len(pattern)):  
  for l in range(len(pattern[i])):
    patStr=str(pattern[i][l])+","+str(pattern[i][l+1])+","+str(pattern[i][l+2])
    if patStr in tempdict:
      tempdict[patStr] +=1
    else:
     tempdict[patStr]=1
     #print(tempdict.values(),max(tempdict.values()))
     #print(tempdict)
     realMax +=str(max(tempdict.iteritems(),key=operator.itemgetter(1))[0])+ ","
     #print(len(tempdict))
     
      
    return realMax 
'''
def popularLine3(pattern):
    realMax=""
    for elt in range(3):
     count=0
     tempdict={}
     for i in range(len(pattern)):
         x=len(pattern[i]) // 3
         for j in range(len(pattern[i])):
             if j==(x*(elt+1)):
                 #print(len(pattern[i]),j)
                 for l in range(j-x,j):
                     patStr = pattern[i][l]
                     #print(l,j,x,len(pattern[i]))
                     if patStr in tempdict:
                         tempdict[patStr] +=1
                     else:
                         tempdict[patStr] =1
     realMax +=str(max(tempdict.iteritems(),key=operator.itemgetter(1))[0])+ ","
    return realMax 
    
def popularLine(pattern):
    realMax=" "
    for elt in range(25):
      count=0
      tempdict={}
      for i in range(len(pattern)):
       x= len(pattern[i]) // 25
       for j in range(len(pattern[i])):
        if j ==(x*(elt+1)):
          count +=1
          #print (j,j-x,x,len(pattern0[i]),elt,count)
          for l in range(j-x,j):
            patStr=str(pattern[i][l])+","+str(pattern[i][l+1])
            if patStr in tempdict:
              tempdict[patStr] +=1
            else:
              tempdict[patStr]=1
      #print(tempdict.values(),max(tempdict.values()))
      #print(tempdict)
      realMax +=str(max(tempdict.iteritems(),key=operator.itemgetter(1))[0])+ ","
       #print(len(tempdict))
     
      
    return realMax 
    
     
          
    #for i in range(len(pattern0)):
      #patStr=""
      #for j in range(len(pattern0[i])):
       # if j+20 < len(pattern0[i]):
       #   patStr=str(pattern0[i][j:j+20])
         # print(j,j+20)
        #if patStr in pattern0dict:
         # pattern0dict[patStr] +=1
        #else:
         # pattern0dict[patStr]=1

def getPatNumList(Dlist,num):
  pattern=[]
  for i in range(len(Dlist)):
    templine= Dlist[i]
    if Dlist[i][1] == int(num):
        templine.pop(0)
        templine.pop(0)
        pattern.append(templine)    
  return pattern
def getMax(list1):
    maxlist= []
    for i in range(len(list1)):
     maxlist.append(len(list1[i]))
    return max(maxlist)
      
    

main()
          
          
    








