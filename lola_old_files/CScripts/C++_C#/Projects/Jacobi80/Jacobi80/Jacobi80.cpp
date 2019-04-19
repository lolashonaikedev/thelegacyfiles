#include <iostream>
#include <math.h>
using namespace std;


int main(){
int i,j;

/* Used Book Examples to Check Precision
float b[3]={-1,4,-5};
float A[3][3] ={{2,-1,1},{2,2,2},{-1,-1,2}};
float x[3]={0.0f,0.0f,0.0f};
float temp[3]={0.0f,0.0f,0.0f};
*/
double b[80],A[80][80],x[80],temp[80];
double a=0.0;
double c=0.0;
for(i= 0;i<80;i++){
	b[i]= 22/7;
	x[i]=0;
	temp[i]=0;
	a=a+1;
	for(j=0;j<80;j++){
		if(j==i){
			A[i][j]=2*a;
		}
		else if(j== i+2 || j== i-2){
			A[i][j] =0.5*a;
		}
		else if(j== i+4 || j== i-4){
			A[i][j] =0.25*a;
			
		}
		else{
			A[i][j]=0;
		}
		c=c+1;
	}
	
}
int k= 0;
//float m=3.0f;
//float TOL= 10e-6;
while(k<33){
	double v1=0;
for(i=0; i<80; i++){
 
 double tempSum =0.0f;
 double div=(1.0/A[i][i]);
 for (j=0;j<80;j++){
	 
    if(j !=i){
	   tempSum = tempSum+( -1.0f * A[i][j] * x[j]);
	   
	}
 }
 temp[i] = div*(tempSum+b[i]);

 
}

k++;
memcpy(x, temp, sizeof(temp));
if(fabs((x[i]-temp[i]))> v1){
	  v1= fabs(x[i]-temp[i]);
 }
//m=v1;
}
cout<<"The Solution that satisfies the tolerance after "<<k<<" iterations is:"<<endl;
for(i=0;i<80;i++){
	cout<<x[i]<<endl;
	
}
   }
	
