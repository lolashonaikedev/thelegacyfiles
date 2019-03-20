#include <stdio.h>
#include <string.h>
#include <math.h>
typedef struct{
 double x,y,z;

} vector;
typedef struct{
 int x,y,z;
} particle;
struct othervec { 
 double x,y,z;
};
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
if ((j+1) % 10 == 0){
sprintf(results,"%s_%04d.dat",basename,j+1);
out_file_basename=fopen(results,"w");
 for(i=0;i<num_particles;i++){
 par[i]=updatePosition(velocity,par[i]);
 fprintf(out_file_basename," %d %d %d %d %d \n",j,i,par[i].x,par[i].y,par[i].z); 
}
}
}

}
