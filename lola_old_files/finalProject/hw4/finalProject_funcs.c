#include <stdio.h>
#include <string.h>
#include <math.h>
#include "finalProject_funcs.h"
//typedef struct{
  //double x;
  //double y;
  //double z;
//}particle;

//typedef struct{
  //double x;
  //double y;
  //double z;
//}vector;

//FILE *vel_file;
//FILE *part_file;
//particle * par;
//vector *** velocity;

void readparticlevalue(FILE* input_file1, heatMap ** plate1, int size_x1, int size_x2){
 int i,j,k;
 char xpos[10],ypos[10];
 double temp;
 int hold;
 {
 fscanf(input_file, "%s %s",xpos,ypos);
 if((xpos=="0") && (ypos=="0")){
 for(i=0;i<size_x1;i++){
  plate[i]=(heatMap*)malloc(sizeof(heatMap)*size_x);
  for(j=0;j<size_y1;j++){
 fscanf(input_file,"%s %s %lf %d",xpos,ypos,&plate1[0][0].tN,&plate1[0][0].h); 
}
}
}
 else if ((xpos=="0")&& (ypos=="*")){
 for(i=0;i<size_x1;i++){
  plate[i]=(heatMap*)malloc(sizeof(heatMap)*size_x);
  for(j=0;j<size_y1;j++){
// sscanf(ypos,"%d",&yint);
 fscanf(input_file,"%s %s %lf %d",xpos,ypos,&plate1[0][j].tN,&plate1[0][j].h);
 //sscanf(xpos,"%d",&xint);

}
}
}
 else if((xpos=="*") && (ypos=="9")){
 for(i=0;i<size_x1;i++){
   plate[i]=(heatMap*)malloc(sizeof(heatMap)*size_x);
  for(j=0;j<size_y1;j++){
// sscanf(xpos,"%d",&xint);
 fscanf(input_file,"%s %s %lf %d",xpos,ypos,&plate1[i][9].tN,&plate1[i][9].h);
  
}
}

}
else{
// sscanf(xpos,"%d",&xint);
// sscanf(ypos,"%d",&yint);
 fscanf(input_file,"%s %s %lf %d",xpos,ypos,&plate1[i][j].tN,&plate1[i][j].h);

}
}

}

particle  updatePosition(vector *** velocity, particle par){
  particle answer;
  double posx,posy,posz;
  posx=par.x+velocity[par.x][par.y][par.z].x;
  posy=par.y+velocity[par.x][par.y][par.z].y;
  posz=par.z+velocity[par.x][par.y][par.z].z;
  par.x=floor(posx);
  par.y=floor(posy);
  par.z=floor(posz);
  answer.x=par.x;
  answer.y=par.y;
  answer.z=par.z;
  return answer;

}