#include <iostream>
#include <math.h>
#include <memory.h>
using namespace std;

void solution4(double &Tol, double (&b)[4],double (&A)[4][4],double (&x)[4],double (&temp)[4]);
int main(){
int i,j;
double tol1=10e-2, tol2=10e-4,tol3=10e-6;
double A1[4][4],x1[4],temp1[4];
double a=1.0;
double c=1.0;
double b1[4] = {1,0,0,1};
for(i= 0;i<4;i++){
	x1[i]=0;
	temp1[i]=0;

	for(j=0;j<4;j++){
		A1[i][j] = (1.0/(i+2+j-1));
		
	}
}
cout<<"For the Tolerance of 0.1"<<endl;
solution4(tol1,b1,A1,x1,temp1);
cout<<"For the Tolerance of 0.001"<<endl;
solution4(tol2,b1,A1,x1,temp1);
cout<<"For the Tolerance of 0.00001"<<endl;
solution4(tol3,b1,A1,x1,temp1);
}
void solution4(double &Tol, double (&b)[4],double (&A)[4][4],double (&x)[4],double (&temp)[4])
{
int k= 0;
int i,j;
double TOL=10e-2;
double m=3.0;

while(m>Tol){
double v1=0;
for(i=0; i<4; i++){
 double tempSum =0;
 double tempSum2 =0;
 double div=(1/A[i][i]);
 //temp[i]=x[i];
 for (j=0;j<4;j++){
	 
    if(j <i && j!=i){
	   tempSum = tempSum+( -1 * A[i][j] * x[j]);
	 
	}
	if (j>=i && j!=i){
		tempSum2=tempSum2+(-1*A[i][j]*temp[j]);
        
	}
 }
 x[i] = div*(tempSum+tempSum2+b[i]);
 v1 += pow(x[i]-temp[i],2);
 
}
m=pow(v1,1/2.0);
//cout<<m<<endl;
k++;

memcpy(temp, x, sizeof(temp));

}

cout<<"The Solution "<<k<<" iterations is :"<<endl;
for(i=0;i<4;i++){
	
	cout<<x[i];
	cout<<"\n";	
	
}

   }
	