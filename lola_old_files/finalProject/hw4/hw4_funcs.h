#ifndef _hw4_funcs_
#define _hw4_funcs_

typedef struct{
  int x;
  int y;
  int z;
}particle;

typedef struct{
  double x;
  double y;
  double z;
}vector;

void readparticlevalue(FILE* part_file,FILE* vel_file, particle *arr1, int num_particles,vector ***arr2);
particle  updatePosition(vector *** velocity, particle par);

#endif