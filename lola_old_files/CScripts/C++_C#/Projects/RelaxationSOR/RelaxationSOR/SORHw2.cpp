#include <iostream>
#include <math.h>
using namespace std;
void solution3(double &w, double (&b)[3],double (&A)[3][3],double (&x)[3],double (&temp)[3]);
void solution4(double &w, double (&b)[4],double (&A)[4][4],double (&x)[4],double (&temp)[4]);
void solution5(double &w, double (&b)[5],double (&A)[5][5],double (&x)[5],double (&temp)[5]);
void solution6(double &w, double (&b)[6],double (&A)[6][6],double (&x)[6],double (&temp)[6]);
void solution3tol(double &w, double (&b)[3],double (&A)[3][3],double (&x)[3],double (&temp)[3],double &Tol);
void solution4tol(double &w, double (&b)[4],double (&A)[4][4],double (&x)[4],double (&temp)[4],double &Tol);
void solution5tol(double &w, double (&b)[5],double (&A)[5][5],double (&x)[5],double (&temp)[5],double &Tol);
void solution6tol(double &w, double (&b)[6],double (&A)[6][6],double (&x)[6],double (&temp)[6], double &Tol );
void solution10tol(double &w, double (&b)[8],double (&A)[8][8],double (&x)[8],double (&temp)[8], double &Tol);
void solution11tol(double &w, double (&b)[80],double (&A)[80][80],double (&x)[80],double (&temp)[80], double &Tol);

int main(){

double w =1.1f;
double w1= 1.3f;
double w2=1.2000000;
double w3=1.0;
double TOL=10e-3;
///Problem1

//1A
double b0[3]={1,0,4};
double A0[3][3] ={{3,-1,1},{3,6,2},{3,3,7}};
double x0[3]={0,0,0};
double temp0[3]={0.0,0.0,0.0};
solution3(w, b0, A0, x0, temp0);
//1B
double b1[3]={9,7,6};
double A1[3][3] ={{10,-1,0},{-1,10,-2},{0,-2,10}};
double x1[3]={0,0,0};
double temp1[3]={0.0,0.0,0.0};
solution3(w, b1, A1, x1, temp1);
//1C
double b2[4]={6,25,-11,-11};
double A2[4][4] ={{10,5,0,0},{5,10,-4,0},{0,-4,8,-1},{0,0,-1,5}};
double x2[4]={0,0,0,0};
double temp2[4]={0.0,0.0,0.0,0.0};
solution4(w, b2, A2, x2, temp2);

//1D
double b3[5]={6,6,6,6,6};
double A3[5][5] ={{4,1,1,0,1},{-1,-3,1,1,0},{2,1,5,-1,-1},{-1,-1,-1,4,0},{0,2,-1,1,1}};
double x3[5]={0,0,0,0,0};
double temp3[5]={0.0,0.0,0.0,0.0,0.0};
solution5(w, b3, A3, x3, temp3);

///Problem2

//2A

double b21[3]={5,4,-1};
double A21[3][3] ={{4,1,-1},{-1,3,1},{2,2,5}};
double x21[3]={0,0,0};
double temp21[3]={0.0,0.0,0.0};
solution3(w, b21, A21, x21, temp21);

//2B
double b22[3]={4,-4,0};
double A22[3][3] ={{-2,1,0.5},{1,-2,-0.5},{0,1,2}};
double x22[3]={0,0,0};
double temp22[3]={0.0,0.0,0.0};
solution3(w, b22, A22, x22, temp22);
//2C
double b23[4]={2,-1,0,-1};
double A23[4][4] ={{4,1,-1,1},{1,4,-1,-1},{-1,-1,5,1},{1,-1,1,3}};
double x23[4]={0,0,0,0};
double temp23[4]={0.0,0.0,0.0,0.0};
solution4(w, b23, A23, x23, temp23);

//2D
double b24[6]={0,5,0,6,-2,6};
double A24[6][6] ={{4,-1,0,0,0,0},{-1,4,-1,0,0,0},{0,-1,4,0,0,0},{0,0,0,4,-1,0},{0,0,0,-1,4,-1},{0,0,0,0,-1,4}};
double x24[6]={0,0,0,0,0,0};
double temp24[6]={0.0,0.0,0.0,0.0,0.0,0};
solution6(w, b24, A24, x24, temp24);

//Problem 3
solution3(w1, b0, A0, x0, temp0);
solution3(w1, b1, A1, x1, temp1);
solution4(w1, b2, A2, x2, temp2);
solution5(w1, b3, A3, x3, temp3);


//Problem 4
solution3(w1, b21, A21, x21, temp21);
solution3(w1, b22, A22, x22, temp22);
solution4(w1, b23, A23, x23, temp23);
solution6(w1, b24, A24, x24, temp24);

//Problem5
solution3tol(w2, b0, A0, x0, temp0, TOL);
solution3tol(w2, b1, A1, x1, temp1, TOL);
solution4tol(w2, b2, A2, x2, temp2, TOL);
solution5tol(w2, b3, A3, x3, temp3, TOL);

//Problem6
solution3tol(w2, b21, A21, x21, temp21, TOL);
solution3tol(w2, b22, A22, x22, temp22, TOL);
solution4tol(w2, b23, A23, x23, temp23, TOL);
solution6tol(w2, b24, A24, x24, temp24, TOL);

//Problem 7
double w31=1.0120607;
double w33=1.1543499;
solution3(w31, b0, A0, x0, temp0);
solution4(w33, b2, A2, x2, temp2);


//Problem 8
solution3(w3, b21, A21, x21, temp21);
solution3(w3, b22, A22, x22, temp22);
solution4(w3, b23, A23, x23, temp23);
solution6(w3, b24, A24, x24, temp24);

//Problem10
double b10[8]={0,0,0,0,0,10000,0,0};
double w4= 1.25;
double tol2= 10e-2;
double A10[8][8] ={{-1,0,0,0.707106781,1,0,0,0},{0,-1,0,0.707106781,0,0,0,0},{0,0,-1,0,0,0,0.5,0},{0,0,0,-0.707106781,0,-1,-0.5,0},{0,0,0,0,-1,0,0,1},{0,0,0,0,0,1,0,0},{0,0,0,-0.707106,0,0,0.8660254,0},{0,0,0,0,0,0,-0.8660254,-1}};
double x10[8]={0,0,0,0,0,0,0,0};
double temp10[8]={0.0,0.0,0.0,0.0,0.0,0};
solution10tol(w4, b10, A10, x10, temp10,tol2);


//Problem11
double bt[80],At[80][80],xt[80],tempt[80];
double at=0.0;
double ct=0.0;
double tol3= 10e-5;
int h,g;
for(h= 0;h<80;h++){
	bt[h]= 22/7;
	xt[h]=0;
	tempt[h]=0;
	at=at+1;
	for(g=0;g<80;g++){
		if(h==g){
			At[h][g]=2*at;
		}
		else if(g== h+2 || g== h-2){
			At[h][g] =0.5*at;
		}
		else if(g== h+4 || g== h-4){
			At[h][g] =0.25*at;
			
		}
		else{
			At[h][g]=0;
		}
		ct=ct+1;
	}
	
}
solution11tol(w3, bt, At, xt, tempt,tol3);
}
void solution3(double &w, double (&b)[3],double (&A)[3][3],double (&x)[3],double (&temp)[3]){

int i,j;
int k=0;
for (i=0; i<3;i++){
	x[i]=0;
	temp[i]=0;
}
while(k<2){
double v1=0;
for(i=0; i<3; i++){
 double tempSum =0;
 double tempSum2 =0;
 double div=(w/A[i][i]);
 //temp[i]=x[i];
 for (j=0;j<3;j++){
	 
    if(j <i && j!=i){
	   tempSum = tempSum+(1.0 * A[i][j] * x[j]);
	  
	}
	if (j>i && j!=i){
		tempSum2=tempSum2+(1.0*A[i][j]*temp[j]);
      
	}
 }
 x[i] =((1-w)*temp[i])+(div*(-tempSum-tempSum2+b[i]));
 //cout<<x[i]<<endl;
 if(fabs((x[i]-temp[i]))> v1){
	  v1= fabs(x[i]-temp[i]);
 }

 
}

k++;

memcpy(temp, x, sizeof(temp));
//cout<<v1<<endl;
}

cout<<"The Solution to this problem after "<<k<<" iterations is :"<<endl;
for(i=0;i<3;i++){
	
	cout<<x[i]<<endl;
		
	
}
   }
void solution4(double &w, double (&b)[4],double (&A)[4][4],double (&x)[4],double (&temp)[4]){

int i,j;
int k=0;
for (i=0; i<4;i++){
	x[i]=0;
	temp[i]=0;
}
while(k<2){
double v1=0;
for(i=0; i<4; i++){
 double tempSum =0;
 double tempSum2 =0;
 double div=(w/A[i][i]);
 //temp[i]=x[i];
 for (j=0;j<4;j++){
	 
    if(j <i && j!=i){
	   tempSum = tempSum+(1.0 * A[i][j] * x[j]);
	  
	}
	if (j>i && j!=i){
		tempSum2=tempSum2+(1.0*A[i][j]*temp[j]);
      
	}
 }
 x[i] =((1-w)*temp[i])+(div*(-tempSum-tempSum2+b[i]));
 //cout<<x[i]<<endl;
 if(fabs((x[i]-temp[i]))> v1){
	  v1= fabs(x[i]-temp[i]);
 }

 
}

k++;

memcpy(temp, x, sizeof(temp));
//cout<<v1<<endl;
}

cout<<"The Solution to this problem after "<<k<<" iterations is :"<<endl;
for(i=0;i<4;i++){
	
	cout<<x[i]<<endl;
		
	
}
   }
void solution5(double &w, double (&b)[5],double (&A)[5][5],double (&x)[5],double (&temp)[5]){

int i,j;
int k=0;
for (i=0; i<5;i++){
	x[i]=0;
	temp[i]=0;
}
while(k<2){
double v1=0;
for(i=0; i<5; i++){
 double tempSum =0;
 double tempSum2 =0;
 double div=(w/A[i][i]);
 //temp[i]=x[i];
 for (j=0;j<5;j++){
	 
    if(j <i && j!=i){
	   tempSum = tempSum+(1.0 * A[i][j] * x[j]);
	  
	}
	if (j>i && j!=i){
		tempSum2=tempSum2+(1.0*A[i][j]*temp[j]);
      
	}
 }
 x[i] =((1-w)*temp[i])+(div*(-tempSum-tempSum2+b[i]));
 //cout<<x[i]<<endl;
 if(fabs((x[i]-temp[i]))> v1){
	  v1= fabs(x[i]-temp[i]);
 }

 
}

k++;

memcpy(temp, x, sizeof(temp));
//cout<<v1<<endl;
}

cout<<"The Solution to this problem after "<<k<<" iterations is :"<<endl;
for(i=0;i<5;i++){
	
	cout<<x[i]<<endl;
		
	
}
   }
void solution6(double &w, double (&b)[6],double (&A)[6][6],double (&x)[6],double (&temp)[6]){

int i,j;
int k=0;
for (i=0; i<6;i++){
	x[i]=0;
	temp[i]=0;
}
while(k<2){
double v1=0;
for(i=0; i<6; i++){
 double tempSum =0;
 double tempSum2 =0;
 double div=(w/A[i][i]);
 //temp[i]=x[i];
 for (j=0;j<6;j++){
	 
    if(j <i && j!=i){
	   tempSum = tempSum+(1.0 * A[i][j] * x[j]);
	  
	}
	if (j>i && j!=i){
		tempSum2=tempSum2+(1.0*A[i][j]*temp[j]);
      
	}
 }
 x[i] =((1-w)*temp[i])+(div*(-tempSum-tempSum2+b[i]));
 //cout<<x[i]<<endl;
 if(fabs((x[i]-temp[i]))> v1){
	  v1= fabs(x[i]-temp[i]);
 }

 
}

k++;

memcpy(temp, x, sizeof(temp));
//cout<<v1<<endl;
}

cout<<"The Solution to this problem after "<<k<<" iterations is :"<<endl;
for(i=0;i<6;i++){
	
	cout<<x[i]<<endl;
		
	
}
   }
void solution3tol(double &w, double (&b)[3],double (&A)[3][3],double (&x)[3],double (&temp)[3], double &Tol){

int i,j;
int k=0;
for (i=0; i<3;i++){
	x[i]=0;
	temp[i]=0;
}
double m=1.0;
	while(m>Tol){
double v1=0;
for(i=0; i<3; i++){
 double tempSum =0;
 double tempSum2 =0;
 double div=(w/A[i][i]);
 //temp[i]=x[i];
 for (j=0;j<3;j++){
	 
    if(j <i && j!=i){
	   tempSum = tempSum+(1.0 * A[i][j] * x[j]);
	  
	}
	if (j>i && j!=i){
		tempSum2=tempSum2+(1.0*A[i][j]*temp[j]);
      
	}
 }
 x[i] =((1-w)*temp[i])+(div*(-tempSum-tempSum2+b[i]));
 //cout<<x[i]<<endl;
 if(fabs((x[i]-temp[i]))> v1){
	  v1= fabs(x[i]-temp[i]);
 }

 
}

k++;
m=v1;
memcpy(temp, x, sizeof(temp));
//cout<<v1<<endl;
}

cout<<"The Solution to this problem after "<<k<<" iterations is :"<<endl;
for(i=0;i<3;i++){
	
	cout<<x[i]<<endl;
		
	
}
   }
void solution4tol(double &w, double (&b)[4],double (&A)[4][4],double (&x)[4],double (&temp)[4],double &Tol){

int i,j;
int k=0;
for (i=0; i<4;i++){
	x[i]=0;
	temp[i]=0;
}
double m=1.0;
	while(m>Tol){
double v1=0;
for(i=0; i<4; i++){
 double tempSum =0;
 double tempSum2 =0;
 double div=(w/A[i][i]);
 //temp[i]=x[i];
 for (j=0;j<4;j++){
	 
    if(j <i && j!=i){
	   tempSum = tempSum+(1.0 * A[i][j] * x[j]);
	  
	}
	if (j>i && j!=i){
		tempSum2=tempSum2+(1.0*A[i][j]*temp[j]);
      
	}
 }
 x[i] =((1-w)*temp[i])+(div*(-tempSum-tempSum2+b[i]));
 //cout<<x[i]<<endl;
 if(fabs((x[i]-temp[i]))> v1){
	  v1= fabs(x[i]-temp[i]);
 }

 
}

k++;
m=v1;
memcpy(temp, x, sizeof(temp));
//cout<<v1<<endl;
}

cout<<"The Solution to this problem after "<<k<<" iterations is :"<<endl;
for(i=0;i<4;i++){
	
	cout<<x[i]<<endl;
		
	
}
   }
void solution5tol(double &w, double (&b)[5],double (&A)[5][5],double (&x)[5],double (&temp)[5], double &Tol){

int i,j;
for (i=0; i<5;i++){
	x[i]=0;
	temp[i]=0;
}
	int k=0;
	double m=1.0;
while(m>Tol){
double v1=0;
for(i=0; i<5; i++){
 double tempSum =0;
 double tempSum2 =0;
 double div=(w/A[i][i]);
 //temp[i]=x[i];
 for (j=0;j<5;j++){
	 
    if(j <i && j!=i){
	   tempSum = tempSum+(1.0 * A[i][j] * x[j]);
	  
	}
	if (j>i && j!=i){
		tempSum2=tempSum2+(1.0*A[i][j]*temp[j]);
      
	}
 }
 x[i] =((1-w)*temp[i])+(div*(-tempSum-tempSum2+b[i]));
 //cout<<x[i]<<endl;
 if(fabs((x[i]-temp[i]))> v1){
	  v1= fabs(x[i]-temp[i]);
 }

 
}

k++;
m=v1;
memcpy(temp, x, sizeof(temp));
//cout<<v1<<endl;
}

cout<<"The Solution to this problem after "<<k<<" iterations is :"<<endl;
for(i=0;i<5;i++){
	
	cout<<x[i]<<endl;
		
	
}
   }
void solution6tol(double &w, double (&b)[6],double (&A)[6][6],double (&x)[6],double (&temp)[6],double &Tol){

int i,j;
int k=0;
for (i=0; i<6;i++){
	x[i]=0;
	temp[i]=0;
}
double m=1.0;
	while(m>Tol){
double v1=0;
for(i=0; i<6; i++){
 double tempSum =0;
 double tempSum2 =0;
 double div=(w/A[i][i]);
 //temp[i]=x[i];
 for (j=0;j<6;j++){
	 
    if(j <i && j!=i){
	   tempSum = tempSum+(1.0 * A[i][j] * x[j]);
	  
	}
	if (j>i && j!=i){
		tempSum2=tempSum2+(1.0*A[i][j]*temp[j]);
      
	}
 }
 x[i] =((1-w)*temp[i])+(div*(-tempSum-tempSum2+b[i]));
 //cout<<x[i]<<endl;
 if(fabs((x[i]-temp[i]))> v1){
	  v1= fabs(x[i]-temp[i]);
 }

 
}

k++;
m=v1;
memcpy(temp, x, sizeof(temp));
//cout<<v1<<endl;
}

cout<<"The Solution to this problem after "<<k<<" iterations is :"<<endl;
for(i=0;i<6;i++){
	
	cout<<x[i]<<endl;
		
	
}
   }
void solution10tol(double &w, double (&b)[8],double (&A)[8][8],double (&x)[8],double (&temp)[8], double &Tol){

int i,j;
int k=0;
for (i=0; i<8;i++){
	x[i]=0;
	temp[i]=0;
}
double m=1.0;
	while(m>Tol){
double v1=0;
for(i=0; i<8; i++){
 double tempSum =0;
 double tempSum2 =0;
 double div=(w/A[i][i]);
 //temp[i]=x[i];
 for (j=0;j<8;j++){
	 
    if(j <i && j!=i){
	   tempSum = tempSum+(1.0 * A[i][j] * x[j]);
	  
	}
	if (j>i && j!=i){
		tempSum2=tempSum2+(1.0*A[i][j]*temp[j]);
      
	}
 }
 x[i] =((1-w)*temp[i])+(div*(-tempSum-tempSum2+b[i]));
 //cout<<x[i]<<endl;
 if(fabs((x[i]-temp[i]))> v1){
	  v1= fabs(x[i]-temp[i]);
 }

 
}

k++;
m=v1;
memcpy(temp, x, sizeof(temp));
//cout<<v1<<endl;
}

cout<<"The Solution to this problem after "<<k<<" iterations is :"<<endl;
for(i=0;i<8;i++){
	
	cout<<x[i]<<endl;
		
	
}
   }
void solution11tol(double &w, double (&b)[80],double (&A)[80][80],double (&x)[80],double (&temp)[80], double &Tol){

int i,j;
int k=0;
for (i=0; i<80;i++){
	x[i]=0;
	temp[i]=0;
}
double m=1.0;
	while(m>Tol){
double v1=0;
for(i=0; i<80; i++){
 double tempSum =0;
 double tempSum2 =0;
 double div=(w/A[i][i]);
 //temp[i]=x[i];
 for (j=0;j<80;j++){
	 
    if(j <i && j!=i){
	   tempSum = tempSum+(1.0 * A[i][j] * x[j]);
	  
	}
	if (j>i && j!=i){
		tempSum2=tempSum2+(1.0*A[i][j]*temp[j]);
      
	}
 }
 x[i] =((1-w)*temp[i])+(div*(-tempSum-tempSum2+b[i]));
 //cout<<x[i]<<endl;
 if(fabs((x[i]-temp[i]))> v1){
	  v1= fabs(x[i]-temp[i]);
 }

 
}

k++;
m=v1;
memcpy(temp, x, sizeof(temp));
//cout<<v1<<endl;
}

cout<<"The Solution to this problem after "<<k<<" iterations is :"<<endl;
for(i=0;i<80;i++){
	
	cout<<x[i]<<endl;
		
	
}
   }