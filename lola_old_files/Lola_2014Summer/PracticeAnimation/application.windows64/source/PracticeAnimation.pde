//import sftp.*;
//Sftp sftp;


import saito.objloader.*; 
import processing.opengl.*; 
OBJModel model; 
float rotX; 
float rotY; 

PShape alien;  
//PImage img;
ArrayList stars;
PFont Cat, catStage, ttools, tstage, buttons;


float cl, cp, ht, OUR,cl1,cl2,cl3,cl4,cp1,cp2,cp3,cp4,ht1,ht2,ht3,ht4,OUR1,OUR2,OUR3,OUR4,ad,ad1,ad2,ad3,ad4,ss,ss1,ss2,ss3,ss4,md,md1,md2,md3,md4,ct,ct1,ct2,ct3,ct4,sd,sd1,sd2,sd3,sd4,pt,pt1,pt2,pt3,pt4,nb,nb1,nb2,nb3,nb4,pl,pl1,pl2,pl3,pl4,pd,pd1,pd2,pd3,pd4;
float mc,mc1,mc2,mc3,mc4,mt,mt1,mt2,mt3,mt4,sc,sc1,sc2,sc3,sc4;
float thetaMercury, thetaVenus, thetaVenusMoon, thetaEarth, thetaEarthMoon, thetaMars, thetaMarsMoon1, thetaMarsMoon2, thetaJupiter, thetaSaturn, thetaUranus, thetaNeptune, thetaPluto; 
import peasy.*;
PeasyCam cam;
PeasyDragHandler PanDragHandler;
PeasyDragHandler ZoomDragHandler;
String selection;
boolean button1 = false;
boolean button2=  false;
boolean button3= false;
boolean button4 = false;
boolean buttonCat = false;
boolean buttonTool = false;

void setup () {
  
 selectInput(" a file to process:", "fileSelected");


//int(totalCat);
//int(phase1cat);
//int(totalTool);

 size (1300,700,OPENGL);
// if (mouseClicked)
//scaleFactor=100;

 cam = new PeasyCam(this,width/2, height/2,0,5000);
 cam.setMinimumDistance(5);
 cam.setMaximumDistance(700);
 PanDragHandler = cam.getPanDragHandler();
 ZoomDragHandler = cam.getZoomDragHandler();
 cam.setLeftDragHandler(PanDragHandler);
 cam.setRightDragHandler(ZoomDragHandler);
// print(totalFreqCatp.sortKeys());
  stars = new ArrayList();
 for(int i=1; i<=1300;i++){
  stars.add(new star());
 }
model = new OBJModel(this, "testing.obj", POLYGON); 
model.scale(5);



 lights();
 //lipseMode(Corner);
 ellipseMode(CENTER);
 //***Writing the text****
 Cat=createFont("Cambria", 26,true);
 catStage   = createFont("Cambria",20, true);
 ttools = createFont("Cambria",18,true);
 tstage = createFont("Cambria",15,true);
 buttons = createFont("Cambria",18,true); 
 // cam = new PeasyCam(this,width/2, height/2, 0,5000);
 // cam.setMinimumDistance(5);
//  cam.setMaximumDistance(700);
 // PanDragHandler = cam.getPanDragHandler();
 // ZoomWheelHandler = cam.getZoomWheelHandler();
 // cam.setWheelHandler(ZoomWheelHandler);

 fill(81,72,175);
 //text("Hello", 10,100);
 //img = loadShape("3DAlien.obj");
 //phase1 = createFont("Arial", 8,true);
 //img = loadShape("SunAlien.obj");
//img.resize(200,200);

 }
//} 

void draw () { 

  
  noStroke(); 
   smooth(); 
   background(0);
  // ZoomDragHandler.handleDrag(10,10);
  // PanDragHandler.handleDrag(10,10);
   //*****Write Texts and Create Legends************
    fill(281,10,10);
    textFont(Cat);
    fill(77, 130, 232);
    text("Cognitive Loads:"+cl+"%", 70,50);
    fill(0, 378, 238);
    text("Cognitive Processing:"+cp+"%", 110,590);
    fill(232 ,119, 77);
    text("Out of Reach Activities:"+OUR+"%", 930,50);
    fill(0, 255, 0);
    text("Hypothesis Testing:" +ht+"%", 930, 360);
    textFont(catStage);
    fill(243,253,309);
    text("Stage 1:  "+cl1+"% Stage 2:  "+cl2+"% Stage 3:   "+cl3+"% Stage 4:  "+cl4+ "%",70,80);
    text("Stage 1:"+cp1+" Stage 2:"+cp2+" Stage 3:"+cp3+" Stage 4:"+cp4, 110,620);
    text("Stage 1:"+OUR1+" Stage 2:"+OUR2+" Stage 3:"+OUR3+" Stage 4:"+OUR4, 930,  80);
    text("Stage 1:"+ht1+" Stage 2:"+ht2+" Stage 3:"+ht3+" Stage 4:"+ht4, 930, 390);
    textFont(ttools);
    fill(169, 136, 120);
    text("Alien Database:"+ad+"%",20,430);
    fill(139, 136, 12);
    text("SolarSystem Database:"+ss+"%",300,430);
    fill(139, 16, 120);
    text("Missions Database:"+md+"%",20, 480);
    fill(250, 139,  48);
    text("Concepts Database:"+ct+"%",300, 480);
    fill(39, 136, 120);
    text("Spectral Database:"+sd+"%",10,530);
    fill(18,  58, 137);
    text("Period table:"+pt+"%",300,530);
    fill(255, 136, 120);
    text("Probe Design:"+pd+"%",850,290);
    fill(239, 136, 20);
    text("Probe Launch:"+pl+"%",1150,290);
    fill(66 ,232,125);
    text("Mission Status:"+mc+"%",1000,620);
    fill(109, 131, 20);
    text("Message Tool:"+mt+"%",1000,670);
    fill(175, 245, 220);
   
    textFont(tstage);
     fill(245,243,172);
    text("Stage 1:"+ad1+"% Stage 2: "+ad2+"%  Stage 3:"+ad3+"%  Stage 4:"+ad4+"%", -90,450);
    text("Stage 1:"+ss1+"% Stage 2: "+ss2+"%  Stage 3:"+ss3+"%  Stage 4:"+ss4+"%", 290,450);
    text("Stage 1:"+md1+"% Stage 2: "+md2+"%  Stage 3:"+md3+"%  Stage 4:"+md4+"%", -70,500);
    text("Stage 1:"+ct1+"% Stage 2: "+ct2+"%  Stage 3:"+ct3+"%  Stage 4:"+ct4+"%", 290, 500);
     text("Stage 1:"+sd1+"% Stage 2: "+sd2+"%  Stage 3:"+sd3+"% Stage 4:"+sd4+"%",-70,550);
    text("Stage 1:"+pt1+"% Stage 2: "+pt2+"%  Stage 3:"+pt3+"%  Stage 4:"+pt4+"%", 290,550);
    text("Stage 1:"+pd1+"% Stage 2: "+pd2+"%  Stage 3:"+pd3+"%  Stage 4:"+pd4+"%", 750, 310);
    text("Stage 1:"+pl1+"% Stage 2: "+pl2+"%  Stage 3:"+pl3+"%  Stage 4:"+pl4+"%",1130, 310);
     text("Stage 1:"+mc1+"% Stage 2: "+mc2+"%  Stage 3:"+mc3+"% Stage 4:"+mc4+"%", 930, 640);
     text("Stage 1:"+mt1+"% Stage 2: "+mt2+"%  Stage 3:"+mt3+"% Stage 4:"+mt4+"%", 930, 690);
    //text("Stage 1:"+ad1+"% Stage 2: "+ad2+"%  Stage 3:"+ad3+"%   Stage 4:"+ad4+"%",1100, 640);
    
    //Creates The Legend Button Commands******************
     fill(243,253,309);
    rect(370,0,20,20);
    textFont(buttons);
    text("Catergories",390,15);
    rect(500,00,20,20);
    text("Tools", 520,15);
     fill(255,0,0);
    rect(600,00,20,20);
    text("Stage 1", 620,15);
    fill(0, 0, 255);
    rect(700,00,20,20);
    text("Stage 2", 720,15);
    fill(237,255,3);
    rect(800,00,20,20);
    text("Stage 3", 820,15);
     fill(131,131,126);
    rect(900,00,20,20);
    text("Stage 4",920,15);
  
  
  
  
  
 //*****Draw Stars BackGrounds**************
  for (int i=0; i<= stars.size()-1;i++){
   star starUse= (star) stars.get(i);
    starUse.display();
  }
    
 pushMatrix(); 
 translate(width/2, height/2, 0); 
 rotateX(rotY); 
 rotateY(rotX); 
 scale(20.0); 
 model.draw(); 
 popMatrix();
   
   //shape(img);
   //shape(img, (width/3)+95, (height/2)-95);
   //img.scale(0.25);
  
  



 
 //-----------Cognitive Process Planet+ Moons+ Orbits---------
 orbitDisplay(250, 660,100, 1);//Cognitive Process
 pushMatrix(); 

 //ranslate(600,600);
  popMatrix();
  pushMatrix();
planetDisplay (250,660,cp,0, 378, 238);//Cognitive Process Planet
  popMatrix(); 
  pushMatrix(); 


///-----Tools Supporting Out of Reach Activities -------------------
   orbitDisplay(1100, 180,200,1);//Probe Design Orbit
   orbitDisplay(1100, 180, 380, 1);//Probe Launch Orbit
  planetDisplay (1100, 180, OUR,232 ,119, 77);//OUR Sun
   
   pushMatrix();
   float a = (110/1.5)* cos(thetaMars);
   float b = (110/3)* sin(thetaMars);
   planetDisplay(a,b, pd, 255, 136, 120);//Probe Design
   stageMoonDisplay(pd1*.25,pd2*.25,pd3*.25,pd4*.25);
   popMatrix();
   pushMatrix();
   float z =(180/1.5)*cos(thetaJupiter);
   float u=(180/ 3) * sin(thetaJupiter);
  planetDisplay(z, u, pl, 239, 136, 20);//Probe Launch
  stageMoonDisplay(pl1*.25,pl2*.25,pl3*.25,pl4*.25);
  popMatrix();
   
   popMatrix();  
    pushMatrix();  

 //----Toools Supporting Hypothesis Testing---------------------------
  orbitDisplay(1100, 500, 200, 1);//saturn orbit 
  orbitDisplay(1100, 500, 350, 1);//saturn orbit 
  orbitDisplay(1100, 500, 500, 1);//saturn orbit 
  planetDisplay (1100, 500, ht, 0, 255, 0);//jupiter 
 //popMatrix();
 pushMatrix(); 
  
 float d = (110/1.5) * cos(thetaMarsMoon1);
 float e = (110/3) * sin(thetaMarsMoon1);
 moonDisplay(d, e, mc, 66 ,232,125 ); //Mission Status
 stageMoonDisplay(mc1*.25,mc2*.25,mc3*.25,mc4*.25);
 popMatrix();
 pushMatrix();
 float g = (170/1.5) * cos(thetaMarsMoon2);
 float m = (170/3) * sin(thetaMarsMoon2);
 moonDisplay(g, m, mt, 109, 131, 20);//message tool
 stageMoonDisplay(mt1*.25,mt2*.25,mt3*.25,mt4*.25);
 popMatrix();
 pushMatrix();
 float v = (240/1.5) * cos(thetaJupiter);
 float w = (240/3) * sin(thetaJupiter);
 moonDisplay(v, w, 1, 175, 245, 220);//solution tool
 stageMoonDisplay(1,2,3,4);
 popMatrix();
 popMatrix();
 pushMatrix();


  
  
 //-------------------------CognitiveLoads---------------------------------------------
  orbitDisplay(200,250,200, 1);//neptune orbit 
   orbitDisplay(200,250,350,1);
   orbitDisplay(200,250,500,1);
   orbitDisplay(200,250,650,1);
   orbitDisplay(200,250,800,1);
   orbitDisplay(200,250,950,1);
  planetDisplay (200, 250, cl,  77, 130, 232);//cognitive Load sun
//  //translate(0,-475); 
  pushMatrix();
  float h = (100 /1.5)* cos(thetaMars);
  float i = (100 /3)* sin(thetaMars);
  planetDisplay(h, i, ct, 250, 139,  48); //concepts
  stageMoonDisplay(ct1*.25,ct2*.25,ct3*.25,ct4*.25);
  popMatrix();
  pushMatrix();
  float j = (180/1.5)* cos(thetaMercury);
  float k = (180/3)* sin(thetaMercury);
moonDisplay(j, k, pt,  18,  58, 137);//periodic table
stageMoonDisplay(pt1*.25,pt2*.25,pt3*.25,pt4*.25);
  popMatrix();
  pushMatrix();
  float l = (250/1.5)* cos(thetaVenus);
  float n = (250/3)* sin(thetaVenus );
  moonDisplay(l, n, sd,  39, 136, 120);//spectral database
  stageMoonDisplay(sd1*.25,sd2*.25,sd3*.25,sd4*.25);
  popMatrix();
  pushMatrix();
  float o =(330/1.5)* cos(thetaEarth );
  float p =(330/3)* sin(thetaEarth );
  moonDisplay(o,p, md, 139, 16, 120);//missions database
  stageMoonDisplay(md1*.25,md2*.25,md3*.25,md4*.25);
  popMatrix();
  pushMatrix();
  float q = (400/1.5)* cos(thetaSaturn);
  float r =(400/3)* sin(thetaSaturn);
  moonDisplay(q, r, ss, 139, 136, 12);//Solar System Database
  stageMoonDisplay(ss1*.25,ss2*.25,ss3*.25,ss4*.25);
  popMatrix();
  pushMatrix();
  float s =(470/1.5)* cos(thetaPluto );
  float t =(470/3)* sin(thetaPluto );
  moonDisplay(s, t, ad, 169, 136, 120);//Alien Database
  stageMoonDisplay(ad1*.25,ad2*.25,ad3*.25,ad4*.25);
  popMatrix();

  popMatrix(); 
  pushMatrix(); 
  
  popMatrix(); 
  //INCREMENTS FOR PLANETS AND MOONS 
  thetaMercury +=0.015; 
  thetaVenus +=0.008; 
  thetaVenusMoon +=0.08; 
  thetaEarth +=0.005; 
  thetaEarthMoon +=0.05; 
  thetaMars +=0.009; 
  thetaMarsMoon1 +=0.03; 
  thetaMarsMoon2 +=0.025; 
  thetaJupiter += 0.04; 
  thetaSaturn += 0.008;
  thetaUranus += 0.002; 
  thetaNeptune +=0.004; 
  thetaPluto += 0.003; 
//println("What is the value of thetaMercury?" +thetaMercury); 
    
 pushMatrix(); 
 translate(width/2, height/2, 0); 
 rotateX(rotY); 
 rotateY(rotX); 
 scale(20.0); 
 model.draw(); 
 popMatrix();
   


//----------------MouseFunctions---------

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
void moonDisplay (float x, float y, float radius, float r, float g, float b){//moon display 
noStroke(); 
fill(r, g, b); 
//ellipse(x, y, radius, radius); 
translate(x,y);
sphere(radius);
} 

void orbitDisplay (float x, float y, float radius, float bold) { 
noFill(); 
stroke(255); 
strokeWeight(bold); 
ellipse (x, y, radius/1.5, radius/3); 
} 
void stageMoon1Display (float x, float y, float radius ){//moon display 
noStroke(); 
fill(0,255,0); 
//ellipse(x, y, radius, radius); 
translate(x,y);
sphere(radius);
} 
void stageMoon2Display (float x, float y, float radius){//moon display 
noStroke(); 
fill(255,0,0); 
//ellipse(x, y, radius, radius); 
translate(x,y);
sphere(radius);
} 
void stageMoon3Display (float x, float y, float radius){//moon display 
noStroke(); 
fill(0, 0, 255);
//ellipse(x, y, radius, radius); 
translate(x,y);
sphere(radius);
} 
void stageMoon4Display (float x, float y, float radius){//moon display 
noStroke(); 
fill(237,255,3);
//ellipse(x, y, radius, radius); 
translate(x,y);
sphere(radius);
} 
void stageMoonDisplay(float radius1, float radius2, float radius3, float radius4){
  pushMatrix();
   float co = (40 /1.5)* cos(thetaMars);
   float fo = (40/3)* sin(thetaMars);
   //***Stages****
  pushMatrix();
   translate(-co,-fo);
  
   fill(255,0,0); 
   sphere(radius1);
   pushMatrix();
    if (button1){
     sphere(radius1);
     stroke(245);
   }
   popMatrix();
   popMatrix();
   translate(co, fo);
   fill(0, 0, 255);
   sphere(radius2);
   if (button2){
     sphere(radius2);
     stroke(25);
   }
   popMatrix();
   pushMatrix();
   pushMatrix();
    if (button3){
     sphere(radius3);
     stroke(245);
   }
   popMatrix();
   translate(co,-fo);
   fill(237,255,3);
   sphere(radius3);
   popMatrix();
   pushMatrix();
   pushMatrix();
    if (button4){
     sphere(radius4);
     stroke(245);
   }
   popMatrix();
   translate(-co,fo,5);
   fill(131,131,126);
   sphere(radius4);
   popMatrix();
}
void fileSelected(File selection) {
  
  if (selection == null) 
    println ("NO FILE SELECTED"); 
  else { 
    String[] lines = loadStrings (selection.getAbsolutePath()); 
    print(lines);
   
    //String[] lines = loadStrings("AlienRescueData.txt");

    ////--------------Creates the General Initial arrays-----------
   int[] arrStage = new int[lines.length]; //The phases array
    IntList freqStage = new IntList(lines.length);
    String[] arrTool = new String[lines.length]; //The tools array
    String[] arrCategory = new String[lines.length];
    float[] arrDuration = new float[lines.length];
    StringList freqTools= new StringList(lines.length);
    StringList freqCat = new StringList(lines.length);
    StringList freqCat1 = new StringList(lines.length);
    StringList freqCat2 = new StringList(lines.length);
    StringList freqCat3 = new StringList(lines.length);
    StringList freqCat4 = new StringList(lines.length);
    StringList freqTools1 = new StringList(lines.length);
    StringList freqTools2 = new StringList(lines.length);
    StringList freqTools3 = new StringList(lines.length);
    StringList freqTools4 = new StringList(lines.length);
    for (int i=0; i<lines.length; i++){
  
     String[] arrTokens= split(lines[i], '\t');

    int stage = int(arrTokens[0])+'\n';
 
     String tool = arrTokens[1];
     String category = arrTokens[2];
     float duration = float(arrTokens[3]) +'\n';
   //  print(arrStage);
     arrTool[i] = tool;
     arrCategory[i] = category;
     arrDuration[i] = duration;
    }

  
  for (int i=0; i<lines.length; i++){
    freqTools.append(arrTool[i]);
    freqCat.append(arrCategory[i]);
    freqStage.append(arrStage[i]);

  }
    
  for (int i=0; i<lines.length; i++){
  String[] arrTokens1= split(lines[i], '\t');
  int stage = int(arrTokens1[0])+'\n';
 
    if(1 == int(arrTokens1[0])){
     freqTools1.append(arrTool[i]);
     freqCat1.append(arrCategory[i]);
 }
  if(2 == int(arrTokens1[0])){
     freqTools2.append(arrTool[i]);
     freqCat2.append(arrCategory[i]);
  }
   if(3 == int(arrTokens1[0])){
    freqTools3.append(arrTool[i]);
     freqCat3.append(arrCategory[i]);
  }
 if(4 == int(arrTokens1[0])){
     freqTools4.append(arrTool[i]);
   freqCat4.append(arrCategory[i]);
 }
  }
  print(freqCat1);
////---------Begins Extracting Unique Frequencies------------------
FloatDict totalFreqCat = new FloatDict();
FloatDict totalFreqTools = new FloatDict();
FloatDict stage1FreqCat = new FloatDict();
FloatDict stage1FreqTools = new FloatDict();
FloatDict stage2FreqCat= new FloatDict();
FloatDict stage2FreqTools = new FloatDict();
FloatDict stage3FreqCat = new FloatDict();
FloatDict stage3FreqTools = new FloatDict();
FloatDict stage4FreqCat= new FloatDict();
FloatDict stage4FreqTools= new FloatDict();


//**** Calculate Total Frequencies**********
IntDict totalFreqCatf= freqCat.getTally();
FloatDict totalFreqCatp = totalFreqCatf.getPercent();
OUR = round(totalFreqCatp.get("Activities") * 100);
ht = round(totalFreqCatp.get("Hypothesis Testing") *100);
cl = round(totalFreqCatp.get("Cognitive Load") * 100);
cp = round(totalFreqCatp.get("Cognitive Processing") * 100);

IntDict totalFreqCatf1= freqCat1.getTally();
FloatDict totalFreqCatp1 = totalFreqCatf1.getPercent();
OUR1 = round(totalFreqCatp1.get("Activities") * 100);
ht1 = round(totalFreqCatp1.get("Hypothesis Testing") *100);
cl1 = round(totalFreqCatp1.get("Cognitive Load") * 100);
cp1 = round(totalFreqCatp1.get("Cognitive Processing") * 100);

IntDict totalFreqCatf2= freqCat2.getTally();
FloatDict totalFreqCatp2 = totalFreqCatf2.getPercent();
OUR2 = round(totalFreqCatp2.get("Activities") * 100);
ht2 = round(totalFreqCatp2.get("Hypothesis Testing") *100);
cl2 = round(totalFreqCatp2.get("Cognitive Load") * 100);
cp2 = round(totalFreqCatp2.get("Cognitive Processing") * 100);

IntDict totalFreqCatf3= freqCat3.getTally();
FloatDict totalFreqCatp3 = totalFreqCatf3.getPercent();
OUR3 = round(totalFreqCatp3.get("Activities") * 100);
ht3 = round(totalFreqCatp3.get("Hypothesis Testing") *100);
cl3 = round(totalFreqCatp3.get("Cognitive Load") * 100);
cp3 = round(totalFreqCatp3.get("Cognitive Processing") * 100);

IntDict totalFreqCatf4= freqCat4.getTally();
FloatDict totalFreqCatp4 = totalFreqCatf4.getPercent();
OUR4 = round(totalFreqCatp4.get("Activities") * 100);
ht4 = round(totalFreqCatp4.get("Hypothesis Testing") *100);
cl4 = round(totalFreqCatp3.get("Cognitive Load") * 100);
cp4 = round(totalFreqCatp4.get("Cognitive Processing") * 100);



IntDict totalFreqToolf= freqTools.getTally();
FloatDict totalFreqToolp = totalFreqToolf.getPercent();
ad = round(totalFreqToolp.get("alien database") *100);
ss = round(totalFreqToolp.get("solar system")*100);
md = round(totalFreqToolp.get("missions")* 100);
ct = round(totalFreqToolp.get("concepts")*100);
sd = round(totalFreqToolp.get("spectra")*100);
pt = round(totalFreqToolp.get("periodic table") *100);
pl = round(totalFreqToolp.get("probe launch") *100);
pd = round(totalFreqToolp.get("probe design") *100);
mt =round(( totalFreqToolp.get("message") + totalFreqToolp.get("message tool")) *100);
mc =round( totalFreqToolp.get("mission control") * 100);

IntDict totalFreqToolf1= freqTools1.getTally();
FloatDict totalFreqToolp1 = totalFreqToolf1.getPercent();
ad1 = round(totalFreqToolp1.get("alien database") *100);
ss1 = round(totalFreqToolp1.get("solar system")*100);
md1 = round(totalFreqToolp1.get("missions")* 100);
ct1 = round(totalFreqToolp1.get("concepts")*100);
sd1 = round(totalFreqToolp1.get("spectra")*100);
pt1 = round(totalFreqToolp1.get("periodic table") *100);
pl1 = round(totalFreqToolp1.get("probe launch") *100);
pd1 = round(totalFreqToolp1.get("probe design") *100);
mt1 =round(( totalFreqToolp1.get("message") + totalFreqToolp.get("message tool")) *100);
mc1 =round( totalFreqToolp1.get("mission control") * 100);

IntDict totalFreqToolf2= freqTools2.getTally();
FloatDict totalFreqToolp2 = totalFreqToolf2.getPercent();
ad2 = round(totalFreqToolp2.get("alien database") *100);
ss2 = round(totalFreqToolp2.get("solar system")*100);
md2 = round(totalFreqToolp2.get("missions")* 100);
ct2 = round(totalFreqToolp2.get("concepts")*100);
sd2 = round(totalFreqToolp2.get("spectra")*100);
pt2 = round(totalFreqToolp2.get("periodic table") *100);
pl2 = round(totalFreqToolp2.get("probe launch") *100);
pd2 = round(totalFreqToolp2.get("probe design") *100);
mt2 =round(( totalFreqToolp2.get("message") + totalFreqToolp.get("message tool")) *100);
mc2 =round( totalFreqToolp2.get("mission control") * 100);

IntDict totalFreqToolf3= freqTools3.getTally();
FloatDict totalFreqToolp3 = totalFreqToolf3.getPercent();
ad3 = round(totalFreqToolp3.get("alien database") *100);
ss3 = round(totalFreqToolp3.get("solar system")*100);
md3 = round(totalFreqToolp3.get("missions")* 100);
ct3 = round(totalFreqToolp3.get("concepts")*100);
sd3 = round(totalFreqToolp3.get("spectra")*100);
pt3 = round(totalFreqToolp3.get("periodic table") *100);
pl3 = round(totalFreqToolp3.get("probe launch") *100);
pd3 = round(totalFreqToolp3.get("probe design") *100);
mt3 =round(( totalFreqToolp3.get("message") + totalFreqToolp.get("message tool")) *100);
mc3 =round( totalFreqToolp3.get("mission control") * 100);

IntDict totalFreqToolf4= freqTools4.getTally();
FloatDict totalFreqToolp4 = totalFreqToolf4.getPercent();
ad4 = round(totalFreqToolp4.get("alien database") *100);
ss4 = round(totalFreqToolp4.get("solar system")*100);
md4 = round(totalFreqToolp4.get("missions")* 100);
ct4 = round(totalFreqToolp4.get("concepts")*100);
sd4 = round(totalFreqToolp4.get("spectra")*100);
pt4 = round(totalFreqToolp4.get("periodic table") *100);
pl4 = round(totalFreqToolp4.get("probe launch") *100);
pd4 = round(totalFreqToolp4.get("probe design") *100);
mt4 =round(( totalFreqToolp4.get("message") + totalFreqToolp.get("message tool")) *100);
mc4 =round( totalFreqToolp4.get("mission control") * 100);

//print(ht);


//IntDict totalFreqToolf= freqTools.getTally();
//FloatDict totalFreqToolp = totalFreqToolf.getPercent();
//ht = totalFreqCatp.get("Hypothesis Testing") *100;
//print(ht);









for(int i= 0; i< arrTool.length -1 ; i++){
  totalFreqCat.add(arrCategory[i],arrDuration[i]);
  totalFreqTools.add(arrTool[i],arrDuration[i]);
  if(1 == int(arrStage[i])){
    stage1FreqCat.add(arrCategory[i],arrDuration[i]);
    stage1FreqTools.add(arrTool[i],arrDuration[i]);
  }
  if(2 == int(arrStage[i])){
    stage2FreqCat.add(arrCategory[i],arrDuration[i]);
    stage2FreqTools.add(arrTool[i],arrDuration[i]);
  }
  if(3 == int(arrStage[i])){
    stage3FreqCat.add(arrCategory[i],arrDuration[i]);
    stage3FreqTools.add(arrTool[i],arrDuration[i]);
  }
  if(4 == int(arrStage[i])){
    stage4FreqCat.add(arrCategory[i],arrDuration[i]);
    stage4FreqTools.add(arrTool[i],arrDuration[i]);
  }
}
FloatDict totalCat = totalFreqCat.getPercent();
FloatDict totalTool = totalFreqTools.getPercent();
FloatDict Stage1cat = stage1FreqCat.getPercent();
FloatDict stage1tools = stage1FreqTools.getPercent();
FloatDict Stage2cat = stage2FreqCat.getPercent();
FloatDict stage2tools = stage2FreqTools.getPercent();
FloatDict Stage3cat = stage3FreqCat.getPercent();
FloatDict stage3tools = stage3FreqTools.getPercent();
FloatDict Stage4cat = stage4FreqCat.getPercent();
FloatDict stage4tools = stage4FreqTools.getPercent();

 } 
}




void mousePressed () { 
if ((mouseX >600) && (mouseX < 620) && (mouseY <620 )) { 
button1 =!button1; 
button2 =false; 
button3=false;
button4=false;


} 
if ((mouseX > 700) && (mouseX < 720) && (mouseY < 720 )) { 

button2 =!button2; 
button1 =false;  
button3=false;
button4 = false;
} 
if ((mouseX > 820) && (mouseX < 840) && (mouseY < 840 )) { 

button3 =!button3; 
button1 =false;  
button4= false;
button3 = false;
} 
if ((mouseX > 900) && (mouseX < 920) && (mouseY < 920 )) { 

button4 =!button4; 
button1 =false; 
button3 = false;
button2 = false;
} 
} 


  











