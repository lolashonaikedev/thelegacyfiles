import operator
from itertools import izip

def main():
    #opens the files to read the solution score and Logs
    #infile1 = open("Solution_Score.csv", "r")
    #infile2 = open("Logs.csv", "r")
    infile1=open(input(str("Please enter the file with Students names and Score:")))
    infile2=open(input(str("Please enter the file with the Students Logs:")))
    minNum=eval(input(str("Please enter the minimum number for the solution score:")))
    countNum=eval(input("Please enter maximum number for solution score:"))
    isNull= False
    countNum=countNum+1
    #nullAns=input(str("Do you want a Null, yes or no? (type exactly yes or no)"))
    #countNum = countNum+1
    #if nullAns== "yes":
     #   isNull=True
    
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
      countLimit = countNum
    countFnct = lambda cnt, dictInput : sum( x == cnt for x in dictInput.values())  
    counts = [countFnct(x,ARSname) for x in xrange(countLimit+1)]
    print counts
 
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
    #for key in ARTname:
      #if key not in ARSname:
         # countNull += 1
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
        #else:
           #reaList.append("null")
           #print(key)
        for j in range(len(tempList1[0])) :
            reaList.append(tempList1[0][j])
        ARD3.append(reaList)
    
    #Set Up A 2DList to Store all the Students decisions that will be later saved into a dictionary
    #Max values are stored for research purposes
    patternList=[]
    maxPat=[]
    popList=[]
    popFileList=[]
    for i in range(countNum):
        newPatName=str("pattern")+str(i)
        newMaxPatName=str("maxPat")+str(i)
        newPopName=str("pop")+str(i)
        #newPopfileName=str("popFile")+str(i)
        patternList.append(newPatName)
        maxPat.append(newMaxPatName)
        popList.append(newPopName)
        #popFileList.append(newPopfileName)
    for i in range(countNum):
        patternList[i]=getPatNumList(ARD3,i)
        maxPat[i]=getMax(patternList[i])
        popList[i]=popularLine(patternList[i])
        popList[i]=popList[i].split(",")
    #pattern0,pattern1,pattern2,pattern3,pattern4,pattern5,pattern6= getPatNumList(ARD3,0),getPatNumList(ARD3,1),getPatNumList(ARD3,2),getPatNumList(ARD3,3),getPatNumList(ARD3,4),getPatNumList(ARD3,5),getPatNumList(ARD3,6)
   # maxPat0,maxPat1,maxPat2,maxPat3,maxPat4,maxPat5,maxPat6 = getMax(pattern0),getMax(pattern1),getMax(pattern2),getMax(pattern3),getMax(pattern4),getMax(pattern5),getMax(pattern6)
    #pop0,pop1,pop2,pop3,pop4,pop5,pop6= popularLine(pattern0),popularLine(pattern1),popularLine(pattern2),popularLine(pattern3),popularLine(pattern4),popularLine(pattern5),popularLine(pattern6)
   # pops0,pops1,pops2,pops3,pops4,pops5,pops6= popularLine3(pattern0),popularLine3(pattern1),popularLine3(pattern2),popularLine3(pattern3),popularLine3(pattern4),popularLine3(pattern5),popularLine3(pattern6)
    #print(maxPat0,maxPat1,maxPat2,maxPat3,maxPat4,maxPat5,maxPat6)
    #pop0,pop1,pop2,pop3,pop4,pop5,pop6=pop0.split(","),pop1.split(","),pop2.split(","),pop3.split(","),pop4.split(","),pop5.split(","),pop6.split(",")
    #print("For Score 0, the popular 3 is,"
    #print popList[2]
    toolsList = ['solar system', 'alien database','mission control','notebook','probe launch','probe design']
    #popList=[pop0,pop1,pop2,pop3,pop4,pop5,pop6]
    popFile=open("solutionPath.csv","w")
    popFile0=open("score0path.csv","w")
    popFile1=open("score1path.csv","w")
    popFile2=open("score2path.csv","w")
    popFile3=open("score3path.csv","w")
    popFile4=open("score4path.csv","w")
    popFile5=open("score5path.csv","w")
    popFile6=open("score6path.csv","w")
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
      if i >= minNum:
       pstr="\n"+str(i)+","
       for j in range(len(popList[i])):
        if j!=len(popList[i])-1:
          pstr+=str(popList[i][j])+","
        else:
          pstr+=str(popList[i][j])
       popFile.write(pstr)
    for i in range(len(popList)):
       if i==0:
           outfilePopNew=popFile0
       if i==1:
            outfilePopwNew=popFile1
       if i==2:
           outfilePopNew=popFile2
       if i==3:
            outfilePopwNew=popFile3
       if i==4:
           outfilePopNew=popFile4
       if i==5:
            outfilePopwNew=popFile5
       if i==6:
           outfilePopNew=popFile6
       for j in range(len(popList[i])):
           getRGB=getRGBCol(popList[i])
           outfilePopNew.write(getRGB)
    outfilePopNew.close()  
    outfile=open("ARPOP.html","w")
    #outfile.write ("<!DOCTYPE html>"
    message= """<!DOCTYPE html> 
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <title>  </title>
    <link rel = "stylesheet" title = "basic style" type = "text/css" 
      href = "./ShoddleDay.css" media = "all" />
    </head>
    <body>
    <div class="center">

     <div class = "header">

     <h1> Alien Path Rescue Visualization</h1>

     </div>

     <div class = "scrollbar">
     <ul style="list-style-type:none">





     </ul>
     </div>

     <div class = "headlines">
     <div class="center">
    <svg width="1500" height="1500">
     <text x="100" y="-100" font-size="30">Alien Database</text>
<rect x="300" y="-135" width="50" height="50" style="fill:#348899;"/>
<text x="400" y="-100" font-size="30" >Solar System</text>
<rect x="575" y="-135" width="50" height="50" style="fill:#FFD34E;"/>
<text x="700" y="-100" font-size="30">Probe Design</text>
<rect x="900" y="-135" width="50" height="50" style="fill:#A2EB8F;"/>
<text x="1000" y="-100" font-size="30">Probe Launch</text>
<rect x="1200" y="-135" width="50" height="50" style="fill:#979C9C;"/>
<text x="1300" y="-100" font-size="30">Mission Control</text>
<rect x="1525" y="-135" width="50" height="50" style="fill:#962D3E;" />
<text x="1600" y="-100" font-size="30">Notebook</text>
<rect x="1750" y="-135" width="50" height="50" style="fill:#343642;"/>
    """
    outfile.write(message)
    for i in range(len(popList)):
     if i>=minNum:
      y=(115*i)+70
      tX=105+115*i
      tY=120+115*i
      textStr1="<text x=\"75\"  y=\""+str(tX)+"\" fill=\"black\" font-size=\"40\">Score "+str(i)+"</text>"
      textStr2="<text x=\"200\" y=\""+str(tY)+"\" fill=\"black\" font-size=\"100\">{</text>"
      outfile.write(str(textStr1))
      outfile.write(str(textStr2))
      for j in range(len(popList[i])):
        posLine= 25*j
        strokeCol=getStrokeCol(popList[i][j])
        if strokeCol != "":
          lineStr="<rect x=\"250\" y=\""+str(y)+"\" width=\"15\" height=\"50\" transform=\"translate("+str(posLine)+",0)\""+"  style=\"fill:"+strokeCol+";stroke-width:1;stroke:rgb(0,0,0)\" />"
        #lineStr="<ellipse id=\"pop1\" cx=\"500px\" cy=\"400\" rx=\"50\" ry=\"2.5\" transform=\"translate(0,"+str(posLine)+")\""+" style=\" stroke:"+strokeCol+"; stroke-width:0.5; fill:"+strokeCol+";\"/>"  
          outfile.write(str(lineStr)+"\n")
    message2=""" </svg>

    </div> 
    <div class=footer>
    <footer> <a href= ""> May 1st 2015</a>| <a href= ""> Damilola Shonaike</a>| <a href= ""> </a>| <a href= ""> </a>| <a href= ""> </a>| <a href= ""> Spring 2015</a>| 
    <br>
    <br>
    <p>CopyRight @Shoddle</p>
    </footer>
    </div>
     </body>
     </html>"""
    outfile.write(message2)
    outfile.close()
    outfileNew11=open("ARProcessing.html","w")
    message3="""<html> <head>
  <title>Processing.js Example</title>
  <link href="style.css" media="screen" rel="stylesheet" type="text/css" />
  <script type="text/javascript" src="processing.js"></script>
  <script type="text/javascript" src="init.js"></script>
  <script type="text/javascript" src="Table_01.js"></script>
  <script type="text/javascript" src="jquery.pack.js"></script>

  </head>
  <body>
  <h1>Pag.33 - drawing objects on top of an image</h1>

  <script type="application/processing">
  PFont font;
  import processing.opengl.*; 


  // Setup the Processing Canvas
  void setup(){
  size( 1500, 800, P3D );
  noFill();


 }

  


  // Main draw loop
  void draw(){
   
  background(253, 245, 230);
  //Alien Path Rescue Visualization
  font = loadFont("FFScala-Bold.ttf"); 
  textFont(font,30); 
   fill( 0, 121, 184 );
  String s = "Alien Path Rescue Visualization";
  text(s,275,10);
  //Alien Database
  fill(52,136,153) ;
  font = loadFont("FFScala-Bold.ttf"); 
  textFont(font,20);
  String ad = "ALIEN DATABASE";
   
  text(ad, 75, 695);
  fill(52,136,153) ;
  rect(5, 675, 65, 25);
  //Solar System
  fill(255,211,78);
  font = loadFont("FFScala-Bold.ttf"); 
  textFont(font,20); 
  String ss = "SOLAR SYSTEM";
  text(ss, 75, 745);
  
  rect(5, 725, 65, 25);
  //Probe Design
  fill(150,45,62);
   font = loadFont("FFScala-Bold.ttf"); 
  textFont(font,20); 
  String mc = "MISSION CONTROL";
  text(mc, 75, 795);
  rect(5, 775, 65, 25);
  //Probe Launch
  fill(162,235,143);
   font = loadFont("FFScala-Bold.ttf"); 
  textFont(font,20); 
  String pd = "PROBE DESIGN";
  text(pd, 1350, 695);
  rect(1250, 675, 65, 25);
  //Notebook
  fill(151,156,156);
   font = loadFont("FFScala-Bold.ttf"); 
  textFont(font,20); 
  String pl = "PROBE LAUNCH";
  text(pl, 1350, 745);
  rect(1250, 725, 65, 25);
  //Mission Control
  fill(52,54,66);
   font = loadFont("FFScala-Bold.ttf"); 
  textFont(font,20); 
  String nb = "NOTEBOOK";
  text(nb, 1350, 795);
  rect(1250, 775, 65, 25);
  ///SCORE 
  
    
    fill(0,0,0);
   font = loadFont("FFScala-Bold.ttf"); 
  textFont(font,40); 
  String s0 = "0";
  text(s0, 490, 790);
  //orbDisplay(400,550,50,10,0,0,0);
  for(int i=0;i<50;i++){
    float posX = 500 - 9*i;
    float posY=  760-12*i;
    int r;
    int g;
    int b;
    orbDisplay(posX,posY,80,12,0,0,0);
  }
  
  
  ////SCORE1
    fill(0,0,0);
   font = loadFont("FFScala-Bold.ttf"); 
  textFont(font,40); 
  String s1 = "1";
  text(s1, 570, 700);
  //orbDisplay(470,490,30,20,0,0,0);
  for(int i=0;i<50;i++){
    float posX = 570 - 6*i;
    float posY=  670-12*i;
    orbDisplay(posX,posY,80,12,0,0,0);
  }
  
  //Score 2
    fill(0,0,0);
   font = loadFont("FFScala-Bold.ttf"); 
  textFont(font,40); 
  String s2 = "2";
  text(s2, 650, 660);
  //orbDisplay(560,450,30,20,0,0,0);
  for(int i=0;i<50;i++){
    float posX = 650-3*i;
    float posY=  630-12*i;
    orbDisplay(posX,posY,80,12,0,0,0);
  }
  //Score 3
    fill(0,0,0);
   font = loadFont("FFScala-Bold.ttf"); 
  textFont(font,40); 
  String s3 = "3";
  text(s3, width/2, 645);
 // orbDisplay(650,430,30,20,0,0,0);
  for(int i=0;i<50;i++){
    float posX = width/2;
    float posY=  620-12*i;
    orbDisplay(posX,posY,80,12,0,0,0);
  }
  //Score4
    fill(0,0,0);
   font = loadFont("FFScala-Bold.ttf"); 
  textFont(font,40); 
  String s4 = "4";
  text(s4, 850, 660);
  //orbDisplay(740,450,30,20,0,0,0);
  for(int i=0;i<50;i++){
    float posX = 860+3*i;
    float posY=  630-12*i;
    orbDisplay(posX,posY,80,12,0,0,0);
  }
  //Score 5
    fill(0,0,0);
   font = loadFont("FFScala-Bold.ttf"); 
  textFont(font,40); 
  String s5 = "5";
  text(s5, 930, 700);
 // orbDisplay(830,500,30,20,0,0,0);
  for(int i=0;i<50;i++){
    float posX = 930+6*i;
    float posY=  670-12*i;
    orbDisplay(posX,posY,80,12,0,0,0);
  }
  //Score6
    fill(0,0,0);
   font = loadFont("FFScala-Bold.ttf"); 
  textFont(font,40); 
  String s6 = "6";
  text(s6, 1010, 790);
  //orbDisplay(900,550,30,20,0,0,0);
  for(int i=0;i<50;i++){
    float posX = 1000+9*i;
    float posY=  760-12*i;
    orbDisplay(posX,posY,80,12,0,0,0);
  }
  ///Big Score Sphere
   
  planetDisplay(width/2,975,300,0,121,184);

  }
  void planetDisplay (float x, float y, float radius, float r, float g, float b){//planet display function 
  //void planetDisplay(float x, float y, float radius, float r, float g, float b, float z){
  noStroke(); 
  //pointLight(r, g, b, 0, 255, 0); 
  fill(r,g,b);
  lights();
  //ellipse(x,y, radius, radius);
  translate(x,y);
  sphere(radius);
  }
  void orbDisplay (float x, float y, float radius1, float radius2, int r, int g, int b){//planet display function 
  //void planetDisplay(float x, float y, float radius, float r, float g, float b, float z){
  noStroke(); 
  //pointLight(r, g, b, 0, 255, 0); 
  fill(r,g,b);
  //lights();
  //translate(x,y);
  ellipse(x,y, radius1, radius2);

  }

	}	
   }

  </script><canvas></canvas>
  <div style="height:0px;width:0px;overflow:hidden;"><img src='map.png' id='map.png'/></div>
  </body> </html>

  """
    outfileNew11.write(message3)
    outfileNew11.close()
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
    '''
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
      
def getStrokeCol(pop0):
  strokeCol=""
  if pop0 == "alien database":
    strokeCol ="#348899"
    #strokeCol = "#FF0033" #red
  if pop0== "solar system":
    #strokeCol = "#00FF00" #green
    strokeCol ="#FFD34E"
  if pop0 == "probe launch":
    strokeCol="#979C9C"
    #strokeCol = "#0000FF" #darkBlue
  if pop0 == "notebook":
    strokeCol="#343642"
    #strokeCol = "#FF9900"#orange
  if pop0 == "mission control":
    strokeCol="#962D3E"
    #strokeCol = "#9900FF"
  if pop0 == "probe design":
    strokeCol="#A2EB8F"
    #strokeCol = "#FF6666"#pinkish
  if pop0 == "0":
    strokeCol = "white"
  return strokeCol

def getRGBCol(pop0):
  getRGB=""
  if pop0 == "alien database":
    #strokeCol ="#348899"
    getRGB="52,136,153"
  if pop0== "solar system":
    getRGB ="153,153,0"
  if pop0 == "probe launch":
    #strokeCol="#979C9C"
    getRGB ="151,156,156"
  if pop0 == "notebook":
    #strokeCol="#343642"
    getRGB="52,54,66"
  if pop0 == "mission control":
     getRGB="150,45,62"
    #strokeCol="#962D3E"
  if pop0 == "probe design":
    #strokeCol="#A2EB8F"
    getRGB="0,102,0"
    #strokeCol = "#FF6666"#pinkish
  if pop0 == "0":
    getRGB = "255,0,0"
  return getRGB
main()
          
          
    








