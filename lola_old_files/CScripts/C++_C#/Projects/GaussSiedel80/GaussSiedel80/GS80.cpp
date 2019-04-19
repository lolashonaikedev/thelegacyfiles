#include <iostream>
#include <math.h>
using namespace std;


int main(){
int i,j;

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
double TOL=10e-6;
double m=3.0;
while(m>TOL){
double v1=0;
for(i=0; i<80; i++){
 double tempSum =0;
 double tempSum2 =0;
 double div=(1/A[i][i]);
 //temp[i]=x[i];
 for (j=0;j<80;j++){
	 
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
 m=v1;
 
}

k++;

memcpy(temp, x, sizeof(temp));

}

cout<<"The Solution "<<k<<" iterations is :"<<endl;
for(i=0;i<80;i++){
	
	cout<<x[i];
	cout<<"\n";	
	
}
   }
	