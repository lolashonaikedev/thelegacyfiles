#include <iostream>
#include <math.h>
using namespace std;


int main(){
int i,j;

double b[3]={-1,4,-5};
double A[3][3] ={{2,-1,1},{2,2,2},{-1,-1,2}};
double x[3]={0,0,0};
double temp[3]={0,0,0};
//float b[4]={6,25,-11,15};
//float A[4][4] ={{10,-1,2,0},{-1,11,-1,3},{2,-1,10,-1},{0,3,-1,8}};
//float x[4]={0.0f,0.0f,0.0f,0.0f};
//float temp[4]={0.0f,0.0f,0.0f,0.0f};
int k= 0;
double T=10e-5;
while(k<22){
double v1=0;
for(i=0; i<3; i++){
 double tempSum =0;
 double tempSum2 =0;
 double div=(1/A[i][i]);
 //temp[i]=x[i];
 for (j=0;j<3;j++){
	 
    if(j <i && j!=i){
	   tempSum = tempSum+( -1 * A[i][j] * x[j]);
	 
	}
	if (j>=i && j!=i){
		tempSum2=tempSum2+(-1*A[i][j]*temp[j]);
        
	}
 }
 x[i] = div*(tempSum+tempSum2+b[i]);
 //cout<<x[i]<<temp[j];
 if(fabs((x[i]-temp[i]))> v1){
	  v1= fabs(x[i]-temp[i]);
 }

 
}

k++;

memcpy(temp, x, sizeof(temp));
cout<<v1<<endl;
}

cout<<"The Solution to homework 9D after "<<k<<" iterations is (I spoke to you in office Hours about the Rounding Errors, I get the books solution at 15iterations):"<<endl;
for(i=0;i<3;i++){
	
	cout<<x[i];
	cout<<"\n";	
	
}
   }
	