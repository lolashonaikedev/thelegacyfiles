#include <stdio.h>
typedef struct{
  double x;
  double y;
  double z;
}particle;

typedef struct{
  double x;
  double y;
  double z;
}vector;

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