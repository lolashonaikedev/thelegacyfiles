#include <iostream>
#include <math.h>
using namespace std;


int main(){
int i,j;
#Problem 5B
//double A5B[2]={-1,4,-5};
//double A5B[3][3] ={{2,-1,1},{2,2,2},{-1,-1,2}};
//double x5B[2]={0,0,0};
//double temp5B[3]={0,0,0};
double x15b=0;
double x25b=0;
double x15bnew=0;
double x25bnew=0;
int k= 0;
double Tol=10e-5;
double m=1;
double maxNumNew =0;
while(m>Tol){
	double maxNumOld=maxNumNew; 
	x15bnew= (1.0f/10)*(pow(x15b,2)*pow(x25b,2)+8);
	x25bnew= (1.0/10)*((pow(x15b,2)*pow(x25b,2))+x15b+8);
    double maxNumNew =x15bnew;
	if (x25bnew > maxNumNew){
		x25bnew = maxNumNew;
	}
	m=maxNumNew - maxNumOld;
	k=k+1;
	cout<<k<<endl;
}
/*
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
	
}*/
   }
	