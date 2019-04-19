#include <iostream>

using namespace std;


int main(){
	int n ,k,i,j;
double TOL,m, b[4],a[4][4],x[4],temp[4], maxArr[4],maxArr2[4],v1,v2;
	cout<<"\nPlease enter the number of unknowns(equations):\n";
	cin>>n;
	cout<<"\nPlease enter the tolerance:\n";
	cin>>TOL;	
	//return 0;
	cout<<"\nPlease enter the Solution array(bth array)\n";
	for (int sol= 0; sol< n; sol++)
	{
		cin>>b[sol];	
		
	}
	cout<<"\nPlease enter the Coeffiecient Matrix:\n";
	 for(i=0;i<n;i++) {
        x[i]=0;
        for(j=0;j<n;j++) {
            cin>>a[i][j];
        }
    }
	k=1;
	 m=1;
	v1=0;
	v2=0;
   while(m>TOL&& k<20){
	for(i =0;i <n;i++){
       double div = 1.0/(a[i][i]);
	   temp[i]=x[i];
	   double tempSum=0;
	   for(j=0;j<n;j++){
		   if (j!=i){
			tempSum = tempSum- (a[i][j]*temp[j]);
		   }
	   }
	 
	   x[i] = div*(b[i]+tempSum);
	   maxArr[i]=x[i];
	   if(v1>maxArr[i]){
         v1=maxArr[i];
	   }

	   maxArr2[i] = x[i] -temp[i];
	   if(v2>maxArr[i]){
         v2=maxArr[i];
	   }
	}
	m= v2 /v1;
	if(m<TOL){
		break;
	}
	k++;
	cout <<k;
	cout<<"\n";
	cout<<m;
	cout<<"\n";
   }
   
   }
	