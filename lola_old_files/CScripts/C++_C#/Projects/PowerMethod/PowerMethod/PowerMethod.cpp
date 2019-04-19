#include <iostream>
#include <memory.h>
#include <math.h>
using namespace std;
int main(){
	int n,i,j,k,l,s;
	float tol;
	float m=1.0f;
	
   // double A[3][3]={{-4,14,0},{-5,13,0},{-1,0,2}};
 //	double xvec[3] ={1,1,1};
	double A[3][3]={{4,-1,1},{-1,3,-2},{1,-2,3}};
    double xvec[3] ={1,0,0};
	double tempx[3]={0,0,0};
	double q;
 //Find Q
	/*
    for(i=0;i<3;i++){
		double tempSumQ=0;
		double tempSum2Q=0;
	   for(j=0;j<3;j++){
         tempSum= tempSum + A[i][j]*xvec[j];
	   }
	 tempx[i]=tempSum;
	 cout<<tempx[i]<<endl;
	  }
	   memcpy(xvec, tempx, sizeof(xvec));
	 //
	}
	
	*/

//9 Problems

//9A Problem
	double A9A[3][3]={{2,1,1},{1,2,1},{1,1,2}};
	double xvec9A[3] ={1,-1,2};
	float tol9A = 10e4;

//9B Problem
	double A9B[3][3]={{1,1,1},{1,1,0},{1,0,1}};
	double xvec9B[3] ={-1,0,1};
	float tol9B = 10e4;

//9C Problem
	double A9C[3][3]={{1,1,1},{1,1,0},{1,0,1}};
	double xvec9C[3] ={-1,2,1};
	float tol9C = 10e4;
//9D Problem
	double A9D[4][4]={{4,1,1,1},{1,3,-1,1},{1,-1,2,0},{1,1,0,2}};
	double xvecD[4] ={1,2,0,3};
	float tol9 = 10e4;
//11 Problems//////////////////////////////
	
//11A Problem
	double A11A[3][3]={{2,1,1},{1,2,1},{1,1,2}};
	double xvec11A[3] ={1,-1,2};
	float tol11A = 10e4;

//11B Problem
	double A11B[3][3]={{1,1,1},{1,1,0},{1,0,1}};
	double xvec11B[3] ={-1,0,1};
	float tol11B = 10e4;
//11C Problem
	double A11C[3][3]={{4.75,2.25,-0.25},{2.25,4.75,1.25},{-0.25,1.25,4.75}};
	double xvec11C[3] ={0,1,0};
	float tol11C = 10e4;
   //11D Problem
	double A11D[4][4]={{4,1,-1,0},{1,3,-1,0},{-1,-1,5,2},{0,0,2,4}};
	double xvec11D[4] ={0,1,0,0};
	float tol11 = 10e4;
  
//12 Problems//////////////////////////////
	
//12A Problem
	double A12A[3][3]={{-2,1,3},{1,3,-1},{3,-1,2}};
	double xvec12A[3] ={1,-1,2};
	float tol12A = 10e4;

//12B Problem
	double A12B[3][3]={{4,2,-1},{2,0,2},{-1,2,0}};
	double xvec12B[3] ={-1,0,1};
	float tol12B = 10e4;
//12C Problem
double A12C[4][4]={{4,1,1,1},{1,3,-1,1},{1,-1,2,0},{1,1,0,2}};
	double xvec12C[4] ={1,0,0,0};
	float tol12C = 10e4;
//12D Problem
	double A12D[4][4]={{5,-2,-1/2.0f,3/2.0f},{-2,5,3/2.0f,-2},{-1/2.0f,3/2.0f,5,-2},{3/2.0f,-1/2.0f,-2,5}};
	double xvec12D[4] ={1,1,0,-3};
	float tol12D = 10e4;
//13 Problems//////////////////////////////
	
//13A Problem
	double A13A[3][3]={{2,1,1},{1,2,1},{1,1,2}};
	double xvec13A[3] ={1,-1,2};
	float tol13A = 10e4;

//13B Problem
	double A13B[3][3]={{1,1,1},{1,1,0},{1,0,1}};
	double xvec13B[3] ={-1,0,1};
	float tol13B = 10e4;
//13C Problem
	double A13C[3][3]={{1,1,1},{1,1,0},{1,0,1}};
	double xvec13C[3] ={-1,2,1};
	float tol13C = 10e4;
//13D Problem
	double A13D[4][4]={{4,1,1,1},{1,3,-1,1},{1,-1,2,0},{1,1,0,2}};
	double xvec13D[4] ={1,2,0,3};
	float tol13 = 10e4;	
	
////////////////////////ACTUAL POWER METHOD/////////////////////
	/*
	for(k=0;k<6;k++){
	  double max1=0;
	  double max2=0;
      for(i=0;i<3;i++){
		double tempSum=0;
	   for(j=0;j<3;j++){
         tempSum= tempSum + A[i][j]*xvec[j];
	   }
	 tempx[i]=tempSum;
	 cout<<tempx[i]<<endl;
	 for(l=0;l<3;l++){
		 for(s=0;s<3;s++){
		    
		 }
	 }
	 if (tempx[i] > max2){
	    max2=tempx[i];
	 }
	 if (xvec[i] > max1){
		 max1=xvec[i];
	 } 
	  }
	   memcpy(xvec, tempx, sizeof(xvec));
	   
	   cout<<max1<<" "<<max2<<endl;
	   double eval = max2/max1;
	   for(i=0;i<3;i++){
         xvec[i]=(1.0/eval) * xvec[i]; 
	   }
	   cout<<"The eval for this is"<<eval<<endl;
	   
	}
	
///////////////////Symmetric Power Method/////////////////////
	for(k=0;k<6;k++){
	  double tempSum2=0;
      for(i=0;i<3;i++){
		double tempSum=0;
	   for(j=0;j<3;j++){
         tempSum= tempSum + A[i][j]*xvec[j];
	   }
	 tempx[i]=tempSum; 
	 tempSum2 =tempSum2+ tempx[i] *xvec[i];
	  }
	  memcpy(xvec, tempx, sizeof(xvec));
	  double eigfind=0;
	  for(l=0;l<3;l++){
		 eigfind = eigfind + pow(xvec[l],2);
		 }
	   
	   //cout<<max1<<" "<<max2<<endl;
	   double eval = tempSum2;
	   for(i=0;i<3;i++){
         xvec[i]=(1.0/pow(eigfind,0.5)) * xvec[i]; 
		 cout<<xvec[i]<<endl;
	   }
	  cout<<"The eval for this is"<<eval<<endl;
	   
	}
	*/
}