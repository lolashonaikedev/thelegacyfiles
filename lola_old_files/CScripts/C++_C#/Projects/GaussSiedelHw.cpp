
// GAUSS Siedel Portion
#include <iostream>
using namespace std;

int main ()
{
  int main(){
int n,i,j;
float b[3]={-1,4,-5};
float A[3][3] ={{2,-1,1},{2,1,2},{-1,-1,2}};
float x[3]={0.0f,0.0f,0.0f};
float temp[3]={0.0f,0.0f,0.0f};
int k= 0;
float m=1.0f;
while(k<25){
for(i=0; i<3; i++){
 
 float tempSum =0.0f;
 float div=(1.0/A[i][i]);
 for (j=0;j<3;j++){
	 
    if(j !=i){
	   tempSum = tempSum+( -1.0f * A[i][j] * x[j]);
	   
	}
 }
 temp[i] = div*(tempSum+b[i]);

 
}

k++;
memcpy(x, temp, sizeof(temp));

}
cout<<"The Solution to homework 9B after 25 iterations is:"<<endl;
for(i=0;i<3;i++){
	cout<<x[i]<<endl;
	
}
   }
	

}

