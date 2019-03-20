#ifndef _finalProject_funcs_
#define _finalProject_funcs_

typedef struct{
  double tN;
  int h;
}heatMap;

void readparticlevalue(FILE* part_file,FILE* vel_file, particle *arr1, int num_particles,vector ***arr2);
particle  updatePosition(vector *** velocity, particle par);

#endif