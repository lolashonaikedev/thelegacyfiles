#include <stdio.h>
#include <string.h>
#include <math.h>

typedef struct{
 double tN;
 int h;
 }heatMap;

int main(int argc, char**argv){
 int i,j,k,size_x,size_y,num_ts,output_freq,hold,xint,yint;
 double alpha;
 char results[30],basename[30],xpos[10],ypos[10];
 FILE *input_file;
 heatMap **plate;
 double temp,tempOld;
 if(argc >3){
  strcpy(basename,argv[3]);
  input_file=fopen(argv[1],"r");
  output_freq=atoi(argv[2]);
 }
 fscanf(input_file,"%d %d %lf %d", &size_x,&size_y,&alpha,&num_ts);
 plate =(heatMap**)malloc(sizeof(heatMap*)*100);
 while(!feof(input_file))
// while(fscanf(File *,"%s %s %lf %d",xposStr,yPosStr,&temp,&hold)!=EOF)
{
 fscanf(input_file, "%s %s",xpos,ypos);
 if((xpos=="0") && (ypos=="0")){
 for(i=0;i<size_x;i++){
  plate[i]=(heatMap*)malloc(sizeof(heatMap)*size_x);
  for(j=0;j<size_y;j++){
 fscanf(input_file,"%s %s %lf %d",xpos,ypos,&plate[0][0].tN,&plate[0][0].h); 
}
}
}
 else if ((xpos=="0")&& (ypos=="*")){
 for(i=0;i<size_x;i++){
  plate[i]=(heatMap*)malloc(sizeof(heatMap)*size_x);
  for(j=0;j<size_y;j++){
// sscanf(ypos,"%d",&yint);
 fscanf(input_file,"%s %s %lf %d",xpos,ypos,&plate[0][j].tN,&plate[0][j].h);
 //sscanf(xpos,"%d",&xint);

}
}
}
 else if((xpos=="*") && (ypos=="9")){
 for(i=0;i<size_x;i++){
   plate[i]=(heatMap*)malloc(sizeof(heatMap)*size_x);
  for(j=0;j<size_y;j++){
// sscanf(xpos,"%d",&xint);
 fscanf(input_file,"%s %s %lf %d",xpos,ypos,&plate[i][9].tN,&plate[i][9].h);
  
}
}

}
else{
// sscanf(xpos,"%d",&xint);
// sscanf(ypos,"%d",&yint);
 fscanf(input_file,"%s %s %lf %d",xpos,ypos,&plate[i][j].tN,&plate[i][j].h);

}
}

}
