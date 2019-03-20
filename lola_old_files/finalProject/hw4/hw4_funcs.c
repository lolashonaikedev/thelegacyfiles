#include <stdio.h>
#include <string.h>
#include <math.h>
#include "hw4_funcs.h"
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

void readparticlevalue(FILE* part_file1,FILE* vel_file1, particle * par1, int num_particles1, vector ***velocity1){
 int i,j,k;
 fscanf(part_file1,"%d\n",&num_particles1); 

 par1 = (particle*)malloc(sizeof(particle)*num_particles1);

 velocity1 = (vector***)malloc(sizeof(vector**)*num_particles1);


for(i=0;i<num_particles1;i++){
 fscanf(part_file1,"%d %d %d",&par1[i].x,&par1[i].y,&par1[i].z);
 velocity1[i] =(vector**)malloc(sizeof(vector*)*num_particles1);
for(j=0;j<num_particles1;j++){
 velocity1[i][j]=(vector*)malloc(sizeof(vector)*num_particles1);
for(k=0;k<num_particles1;k++){
 fscanf(vel_file1,"%lf %lf %lf",&velocity1[i][j][k].x,&velocity1[i][j][k].y,&velocity1[i][j][k].z); 
// printf("%lf %lf %lf\n",velocity1[i][j][k].x,velocity1[i][j][k].y,velocity1[i][j][k].z);
}
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