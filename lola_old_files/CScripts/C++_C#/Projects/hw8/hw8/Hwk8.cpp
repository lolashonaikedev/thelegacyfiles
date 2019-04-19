#include <iostream>
#include <math.h>
using namespace std;


int main(){
int i,j;
//Problem 5B
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
double maxNumOld =0;
cout<<"For the Functional Iteration for Problem 5b:"<<endl;
while(m>Tol){
	k=k+1;
	x15bnew= (1.0f/10)*(pow(x15b,2)*pow(x25b,2)+8);
	x25bnew= (1.0/10)*((pow(x15b,2)*pow(x25b,2))+x15b+8);
    double maxNumNew =x15bnew;
	if (x25bnew > maxNumNew){
		x25bnew = maxNumNew;
	}
	m=maxNumNew - maxNumOld;
    maxNumOld=maxNumNew;
	x15b=x15bnew;
	x25b=x25bnew;
	cout<<"At the "<<k<<" X1 is"<<x15b<<" X2 is" <<x25b<<endl;
}

///////8A
double x18A=0.1;
double x28A=0.1;
double x18Anew=0;
double x28Anew=0;
k= 0;
Tol=10e-5;
m=1;
maxNumOld =0;
cout<<"For the Functional Iteration for Problem 8A:"<<endl;
while(m>Tol){
	k=k+1;
	x18Anew= pow(x28A,2)+pow(x28A,2)-x18A;
	x28Anew=pow(x18A,2)-pow(x28A,2)-x28A;
    double maxNumNew =x18Anew;
	if (x28Anew > maxNumNew){
		x28Anew = maxNumNew;
	}
	m=maxNumNew - maxNumOld;
    maxNumOld=maxNumNew;
	x18A=x18Anew;
	x28A=x28Anew;
	cout<<"At the "<<k<<" X1 is"<<x18A<<" X2 is" <<x28A<<endl;
}
////8D

double x18D=0.1;
double x28D=0.1;
double x38D=0.1;
double x18Dnew=0;
double x28Dnew=0;
double x38Dnew=0;
k= 0;
Tol=10e-5;
m=1;
maxNumOld =0;
cout<<"For the Functional Iteration for Problem 8D:"<<endl;
while(m>Tol){
	k=k+1;
	x18Dnew= pow(x18A,2)+(2*pow(x28A,2))-x28A-(2*x38D);
	x28Dnew=pow(x18D,2)-(8*pow(x28D,2))+(10*x38D);
	x38Dnew=((1.0/(7*x28D*x38D))*pow(x18D,2))-1;
    double maxNumNew=x38Dnew;
	if (x28Dnew >maxNumNew){
		x28Dnew=maxNumNew;
	}
	if(x18D >maxNumNew){
		x18D=maxNumNew;
	}
	m=maxNumNew - maxNumOld;
    maxNumOld=maxNumNew;
	x18A=x18Anew;
	x28A=x28Anew;
	x38D=x38Dnew;
	cout<<"At the "<<k<<" X1 is"<<x18D<<" X2 is" <<x28D<<" X3 is"<<x38D<<endl;
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
	