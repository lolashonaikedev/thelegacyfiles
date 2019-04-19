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
   double A[4][4]={{4,-1,-2,2},{1,2,0,1},{-2,0,3,-2},{2,1,-2,-1}};
   double tempA[4][4]={{0,0,0,0},{0,0,0,0},{0,0,0,0},{0,0,0,0}};
  // double q=0;
   //3A Problem
	double A3A[3][3]={{2,-1,3},{2,0,1},{-2,1,4}};
	double tempA3A[3][3]={{2,-1,3},{2,0,1},{-2,1,4}};
	//double xvec3A[3] ={1,-1,2};
	//float tol9A = 10e4;

//3B Problem
	double A3B[3][3]={{-1,2,3},{2,3,-2},{3,1,-1}};
	double tempA3B[3][3]={{-1,2,3},{2,3,-2},{3,1,-1}};
	//double xvec3B[3] ={-1,0,1};
	//float tol9B = 10e4;

//3C Problem
	double A3C[4][4]={{5,-2,-3,4},{0,4,2,-1},{1,3,-5,2},{-1,4,0,3}};
	double tempA3C[4][4]={{5,-2,-3,4},{0,4,2,-1},{1,3,-5,2},{-1,4,0,3}};
	//double xvec3C[3] ={-1,2,1};
	//float tol9C = 10e4;
//3D Problem
	double A3D[4][4]={{4,-1,-1,-1},{-1,4,0,1},{1,-1,4,-1},{-1,-1,-1,4}};
	double tempA3D[4][4]={{4,-1,-1,-1},{-1,4,0,1},{1,-1,4,-1},{-1,-1,-1,4}};
	//double xvecD[4] ={1,2,0,3};
	//float tol9 = 10e4;

	for (k=1;k<4;k++){
		double q=0;
		for(i=0;i<3;i++){
		  for (j=0;j<3;j++){
			  if (j==k+1){
				  q= q+pow(A[j][k],2);
			  }
			  //if(A[k+1][k] ==0){

		  }
		}

	}
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