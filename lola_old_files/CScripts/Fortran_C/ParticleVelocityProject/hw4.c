#include <stdio.h>
#include <string.h>
#include <math.h>
#include "hw4_funcs.h"
typedef struct{
 double x,y,z;

} vector;
typedef struct{
 int x,y,z;
} particle;
struct othervec { 
 double x,y,z;
};


int main(int argc, char **argv){
 int i,j,k,b,num_ts,num_particles;
 double posx,posy,posz;
 //int gridx,gridy,gridz;
// char filename[30];
 FILE *vel_file;
 FILE *part_file;
 FILE *out_file_basename;
 particle * par;
 char results[30], basename[20];
// vector *par;
 vector *** velocity;
// vector * particle;
 if(argc > 3){
  strcpy(basename, argv[2]);
  vel_file= fopen(argv[3],"r");
  part_file=fopen(argv[4],"r");
  num_ts= atoi(argv[1]);
}
 else{
  num_ts=50;
 // out_file_basename=fopen("results.dat","w");
  strcpy(basename,"results");
  vel_file=fopen("velocity.dat","r");
  part_file=fopen("particles.dat","r");
}

 fscanf(part_file,"%d\n",&num_particles); 

 par = (particle*)malloc(sizeof(particle)*num_particles);

 velocity = (vector***)malloc(sizeof(vector**)*num_particles);


for(i=0;i<num_particles;i++){
 fscanf(part_file,"%d %d %d",&par[i].x,&par[i].y,&par[i].z);
 velocity[i] =(vector**)malloc(sizeof(vector*)*num_particles);
for(j=0;j<num_particles;j++){
 velocity[i][j]=(vector*)malloc(sizeof(vector)*num_particles);
for(k=0;k<num_particles;k++){
 fscanf(vel_file,"%lf %lf %lf",&velocity[i][j][k].x,&velocity[i][j][k].y,&velocity[i][j][k].z); 
// printf("%lf %lf %lf\n",velocity[i][j][k].x,velocity[i][j][k].y,velocity[i][j][k].z);
}
}
}

for(j=0;j<num_ts;j++){
 for(i=0;i<num_particles;i++){
if (j+1 / 10 == 0){
sprintf(results,"%s_%04d.dat",basename,j);
out_file_basename=fopen(results,"w");
for( b=0;b<10;b++){
 par[i]=updatePosition(velocity,par[i]);
 fprintf(out_file_basename,"t= %d p=%d : ( %d, %d, %d) \n",j,i,par[i].x,par[i].y,par[i].z); 
}
}
}
}

}
