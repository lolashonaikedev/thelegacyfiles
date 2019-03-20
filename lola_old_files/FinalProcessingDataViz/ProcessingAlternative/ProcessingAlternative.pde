 /* @pjs font='../data/animeace_b.tff'; */


PFont Font1;
import processing.opengl.*; 
//StringList score0 =new StringList();
//StringList score1 =new StringList();
//StringList score2 =new StringList();
//StringList score3 =new StringList();
//StringList score4 =new StringList();
//StringList score5 =new StringList();
//StringList score6 =new StringList();

String[] score0 =new String[51];
String[] score1 =new String[51];
String[] score2 =new String[51];
String[] score3 =new String[51];
String[] score4 =new String[51];
String[] score5 =new String[51];
String[] score6 =new String[51];
// Setup the Processing Canvas
void setup(){
  size( 1520, 910, P3D );
  noFill();
  //Font1 = createFont("animeace_b.tff", 30);
 // Font1 = createFont("animeace_b.tff", 30);
  importTextFile();

}

  


// Main draw loop
void draw(){
   
  background(253, 245, 230);
  //Alien Path Rescue Visualization
  //font = loadFont("FFScala-Bold.ttf"); 
  //textFont(Font1);
  textSize(30);  
  fill( 0, 121, 184 );
  String s = "Alien Path Rescue Visualization";
  text(s,275,10);
  //Alien Database
  textSize(20);
  fill(52,136,153) ;
  //font = loadFont("FFScala-Bold.ttf"); 
  //textFont(font,20);
  String ad = "ALIEN DATABASE";
   
  text(ad, 75, 695);
  fill(52,136,153) ;
  rect(5, 675, 65, 25);
  //Solar System
  fill(255,211,78);
  //font = loadFont("FFScala-Bold.ttf"); 
  //textFont(font,20); 
  String ss = "SOLAR SYSTEM";
  text(ss, 75, 745);
  
  rect(5, 725, 65, 25);
  //Probe Design
  fill(150,45,62);
  // font = loadFont("FFScala-Bold.ttf"); 
  //textFont(font,20); 
  String mc = "MISSION CONTROL";
  text(mc, 75, 795);
  rect(5, 775, 65, 25);
  //Probe Launch
fill(0,102,0);
   //font = loadFont("FFScala-Bold.ttf"); 
  //textFont(font,20); 
  String pd = "PROBE DESIGN";
  text(pd, 1350, 695);
  rect(1250, 675, 65, 25);
  //Notebook
  fill(151,156,156);
  // font = loadFont("FFScala-Bold.ttf"); 
  //textFont(font,20); 
  String pl = "PROBE LAUNCH";
  text(pl, 1350, 745);
  rect(1250, 725, 65, 25);
  //Mission Control
  fill(52,54,66);
   //font = loadFont("FFScala-Bold.ttf"); 
  //textFont(font,20); 
  String nb = "NOTEBOOK";
  text(nb, 1350, 795);
  rect(1250, 775, 65, 25);
  ///SCORE 

    //textFont(Font1);
     fill(0,0,0) ;
   //font = loadFont("FFScala-Bold.ttf"); 
  //textFont(font,40); 
  String s0 = "0";
  text(s0, 490, 790);
  //orbDisplay(400,550,50,10,0,0,0);
  for(int i=0;i<50;i++){
    float posX = 500 - 9*i;
    float posY=  760-12*i;
     getRGB(score0[i+1]);
    orbDisplay(posX,posY,100,12);
  }
  
  
  ////SCORE1
    
   //font = loadFont("FFScala-Bold.ttf"); 
  //textFont(font,40); 
   fill(0,0,0) ;
  String s1 = "1";
  text(s1, 570, 700);
  //orbDisplay(470,490,30,20,0,0,0);
for(int i=0;i<50;i++){
    float posX = 570 - 6*i;
    float posY=  670-12*i;
    getRGB(score1[i+1]);
    orbDisplay(posX,posY,100,12);
  }
  
  //Score 2
    
   //font = loadFont("FFScala-Bold.ttf"); 
  //textFont(font,40); 
   fill(0,0,0) ;
  String s2 = "2";
  text(s2, 650, 660);
  //orbDisplay(560,450,30,20,0,0,0);
  for(int i=0;i<50;i++){
    float posX = 650-3*i;
    float posY=  630-12*i;
    getRGB(score2[i+1]);
    orbDisplay(posX,posY,100,12);
  }
  //Score 3
  
   //font = loadFont("FFScala-Bold.ttf"); 
  //textFont(font,40); 
   fill(0,0,0) ;
  String s3 = "3";
  text(s3, width/2, 645);
 // orbDisplay(650,430,30,20,0,0,0);
  for(int i=0;i<50;i++){
    float posX = width/2;
    float posY=  620-12*i;
     getRGB(score3[i+1]);
    orbDisplay(posX,posY,100,12);
  }
  //Score4
    
  // font = loadFont("FFScala-Bold.ttf"); 
  //textFont(font,40); 
   fill(0,0,0) ;
  String s4 = "4";
  text(s4, 850, 660);
  //orbDisplay(740,450,30,20,0,0,0);
  for(int i=0;i<50;i++){
    float posX = 860+3*i;
    float posY=  630-12*i;
     getRGB(score4[i+1]);
    orbDisplay(posX,posY,100,12);
  }
  //Score 5
    
   //font = loadFont("FFScala-Bold.ttf"); 
  //textFont(font,40); 
   fill(0,0,0) ;
  String s5 = "5";
  text(s5, 930, 700);
 // orbDisplay(830,500,30,20,0,0,0);
  for(int i=0;i<50;i++){
    float posX = 930+6*i;
    float posY=  670-12*i;
     getRGB(score5[i+1]);
    orbDisplay(posX,posY,100,12);
  }
  //Score6
    fill(0,0,0);
   //font = loadFont("FFScala-Bold.ttf"); 
  //textFont(font,40); 
  String s6 = "6";
 text(s6, 1020, 790);
  //orbDisplay(900,550,30,20,0,0,0);
  for(int i=0;i<50;i++){
    float posX = 1000+9*i;
    float posY=  760-12*i;
     getRGB(score6[i+1]);
    orbDisplay(posX,posY,100,12);
  }
///Big Score Sphere
   
  planetDisplay(width/2-4,960,300,0,121,184);

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
void orbDisplay (float x, float y, float radius1, float radius2){//planet display function 
//void planetDisplay(float x, float y, float radius, float r, float g, float b, float z){
noStroke(); 
//pointLight(r, g, b, 0, 255, 0); 
//fill(r,g,b);
//lights();
//translate(x,y);
//sphere(radius2);
ellipse(x,y, radius1, radius2);

}

void importTextFile(){
String[] strLines = loadStrings("solutionPath.csv");
//table=loadTable("solutionPath.csv","header");
//TableRow zeroRow= (table.getRow(1));

//totData=strLines.length-1;
//println(4);


for(int i=0; i<strLines.length;i++){
  String[] tokens= split(strLines[i],',');
  String checkScore =tokens[0];
   for (int j=0;j<tokens.length-1;j++){
    if (checkScore.equals("0")){
      score0[j]=tokens[j];
    }
    if (checkScore.equals("1")){
      score1[j]=tokens[j];
    }
    if (checkScore.equals("2")){
      score2[j]=tokens[j] ;
    }
    if (checkScore.equals("3")){
      score3[j]=tokens[j];
    }
    if (checkScore.equals("4")){
      score4[j]=tokens[j];
    }
      if (checkScore.equals("5")){
      score5[j]=tokens[j];
    }
    if (checkScore.equals("6")){
      score6[j]=tokens[j];
    }
   }
}
println(score0);
}
void getRGB(String tools){
 
   if (tools.equals("alien database")){
       fill(52,136,153);
    }
     if (tools.equals("solar system")){
       fill(153,153,0);
    }
     if (tools.equals("probe launch")){
       fill(151,156,156);
    }
     if (tools.equals("notebook")){
       fill(52,54,66);
    }
     if (tools.equals("mission control")){
       fill(150,45,62);
    }
     if (tools.equals("probe design")){
       fill(0,102,0);
    }
    
   
    
    
  }
 

 


