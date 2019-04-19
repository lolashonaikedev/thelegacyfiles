#include <iostream>
#include <math.h>
#include <memory.h>
using namespace std;
//void solution(double &m, double (&x)[10],double (&A)[3][3],double (&x)[3],double (&temp)[3]);
int main(){


//Problem 5
	//A
	double x[10] = {4.0,4.2,4.5,4.7,5.1,5.5,5.9,6.3,6.8,7.1};
	double y[10]= {102.56,113.18,130.11,142.05,167.53,195.14,224.87,256.73,299.50,326.72};
   //	double x[10]={1,2,3,4,5,6,7,8,9,10};
//	double y[10] ={1.3,3.5,4.2,5.0,7.0,8.8,10.1,12.5,13.0,15.6};
	//double x[5] ={0,0.25,0.5,0.75,1.00};
	//double y[5]={1.0,1.2840,1.6487,2.1170,2.7183};
	double sumxi=0, sumyi=0,sumx2i=0,sumxiyi=0,sumx3i=0,sumx4i=0,sumx5i=0,sumx6i=0,sumx2iyi=0,sumx3iyi=0,sumlogyi=0,sumxilogyi=0,sumy2i=0;
	double a0a,a1a,a2,a3,a0d,a1d;
	//double m=5;
	double m = 10;
	int i,j,k;
	//Degree 1
	for(i=0;i<m;i++){
		sumxi +=x[i];
		sumyi +=y[i];
		sumx2i +=(x[i]*x[i]);
		sumxiyi += (x[i]*y[i]);
		sumlogyi += log(y[i]);
		sumxilogyi += x[i]*log(y[i]);
		sumx3i += pow(x[i],3.0);
		sumx4i +=pow(x[i],4.0);
		sumx5i += pow(x[i],5.0);
		sumx6i +=pow(x[i],6.0);
		sumx2iyi += (x[i]*x[i] *y[i]);
		sumx3iyi +=(x[i]*x[i]*x[i]*y[i]);
	}
	//double A[4][4]= {{10,sumxi,sumx2i,sumx3i},{sumxi, sumx2i,sumx3i,sumx4i},{sumx2i,sumx3i,sumx4i,sumx5i},{sumx3i, sumx4i,sumx5i,sumx6i}};
	//double b[4] ={sumyi,sumxiyi,sumx2iyi,sumx3iyi};
	//double x0[4]={0.0f,0.0f,0.0f,0.0f};
    //double temp[4]={0.0f,0.0f,0.0f,0.0f};
	//double A[3][3]= {{m,sumxi,sumx2i},{sumxi, sumx2i,sumx3i},{sumx2i,sumx3i,sumx4i}};
	//double b[3] ={sumyi,sumxiyi,sumx2iyi};
	//double x0[3]={0.0f,0.0f,0.0f};
    //double temp[3]={0.0f,0.0f,0.0f};

	a0a=((sumx2i*sumyi)-(sumxiyi*sumxi))/((sumx2i*m)-(sumxi*sumxi));
	a1a=((m*sumxiyi)-(sumxi*sumyi))/((m*sumx2i)-(sumxi*sumxi));
	//Find Error
	double error=0;
	for (i=0;i<m;i++){
		double pol=0;
		pol=a0a + a1a*x[i];
		error +=pow(y[i]-pol,2.0);
	}

    cout<<"For Problem 5a, the polynomial of degree 1 is "<<a0a<<"+"<<a1a<<"x"<<endl;
	cout<<"The Error for 5a is "<<error<<endl;
	
//Problem 5D
    a0d=((m*sumxilogyi)-(sumlogyi*sumxi))/((sumx2i*m)-(sumxi*sumxi));
	a1d=exp(((sumx2i*sumlogyi)-(sumxilogyi*sumxi))/((m*sumx2i)-(sumxi*sumxi)));
    double errord=0;
	double errore=0;
	for (i=0;i<m;i++){
		double pol=0,pol1=0;
		pol=a1d * exp(a0d*x[i]);
		pol1= a1d* pow(x[i],a0d);
		errord +=pow(y[i]-pol,2.0);
		errore += pow(y[i]-pol1,2.0);
	}
//Problem 5E
    cout<<"For Problem 5d, the function is "<<a1d<<"e^"<<a0d<<"x"<<endl;
	cout<<"The Error for 5d is "<<errord<<endl;
	
	cout<<"For Problem 5E, the function is"<<a1d<<"x^"<<a0d<<endl;
	cout<<"The Error for 6d is "<<errore<<endl;
	
	//Problem 6
	double x6[8] = {0.2,0.3,0.6,0.9,1.1,1.3,1.4,1.6};
	double y6[8]= {0.050446,0.098426,0.33277,0.72660,1.0972,1.5697,1.8487,2.5015};
	sumxi=0, sumyi=0,sumx2i=0,sumxiyi=0,sumx3i=0,sumx4i=0,sumx5i=0,sumx6i=0,sumx2iyi=0,sumx3iyi=0,sumlogyi=0,sumxilogyi=0;
	a0a=0,a1a=0,a2=0,a3=0,a0d=0,a1d=0;
	//double m=5;
	m = 8;
	//Degree 1
	for(i=0;i<m;i++){
		sumxi +=x6[i];
		sumyi +=y6[i];
		sumx2i +=(x6[i]*x6[i]);
		sumxiyi += (x6[i]*y6[i]);
		sumlogyi += log(y6[i]);
		sumxilogyi += x6[i]*log(y6[i]);
		sumx3i += pow(x6[i],3.0);
		sumx4i +=pow(x6[i],4.0);
		sumx5i += pow(x6[i],5.0);
		sumx6i +=pow(x6[i],6.0);
		sumx2iyi += (x6[i]*x6[i] *y6[i]);
		sumx3iyi +=(x6[i]*x6[i]*x6[i]*y6[i]);
	}
	

	a0a=((sumx2i*sumyi)-(sumxiyi*sumxi))/((sumx2i*m)-(sumxi*sumxi));
	a1a=((m*sumxiyi)-(sumxi*sumyi))/((m*sumx2i)-(sumxi*sumxi));
	//Find Error
	error=0;
	for (i=0;i<m;i++){
		double pol=0;
		pol=a0a + a1a*x6[i];
		error +=pow(y6[i]-pol,2.0);
	}

    cout<<"For Problem 6a, the polynomial of degree 1 is "<<a0a<<"+"<<a1a<<"x"<<endl;
	cout<<"The Error for 6a is "<<error<<endl;
	
//Problem 6D
    a0d=((m*sumxilogyi)-(sumlogyi*sumxi))/((sumx2i*m)-(sumxi*sumxi));
	a1d=exp(((sumx2i*sumlogyi)-(sumxilogyi*sumxi))/((m*sumx2i)-(sumxi*sumxi)));
    errord=0;
	errore=0;
	for (i=0;i<m;i++){
		double pol=0,pol1=0;
		pol=a1d * exp(a0d*x6[i]);
		pol1= a1d* pow(x6[i],a0d);
		errord +=pow(y6[i]-pol,2.0);
		errore += pow(y6[i]-pol1,2.0);
	}
//Problem 6E
    cout<<"For Problem 6d, the function is "<<a1d<<"e^"<<a0d<<"x"<<endl;
	cout<<"The Error for 6d is "<<errord<<endl;
	
	cout<<"For Problem 6E, the function is"<<a1d<<"x^"<<a0d<<endl;
	cout<<"The Error for 6d is "<<errore<<endl;

	
	//*****************Problem 7
	//Problem7a
	double x3[3] = {2,4,6};
	double y3[3]= {7.0,9.4,12.3};
	sumxi=0, sumyi=0,sumx2i=0,sumxiyi=0,sumx3i=0,sumx4i=0,sumx5i=0,sumx6i=0,sumx2iyi=0,sumx3iyi=0,sumlogyi=0,sumxilogyi=0;
	a0a=0,a1a=0,a2=0,a3=0,a0d=0,a1d=0;
	//double m=5;
	m = 3;
	//Degree 1
	for(i=0;i<m;i++){
		sumxi +=x3[i];
		sumyi +=y3[i];
		sumx2i +=(x3[i]*x3[i]);
		sumxiyi += (x3[i]*y3[i]);
		sumy2i += y3[i]*y3[i];
		
	}
	

	a0a=((m*sumxiyi)-(sumyi*sumxi))/(pow((sumx2i*m)-(sumxi*sumxi),0.50000000)*pow((sumy2i*m)-(sumyi*sumyi),1/2.0));
	//a1a=((m*sumxiyi)-(sumxi*sumyi))/((m*sumx2i)-(sumxi*sumxi));
	//Find Error
	error=0;
	for (i=0;i<m;i++){
		double pol=0;
		pol=a0a*(x3[i]-5.3);
		error +=pow(y3[i]-pol,2.0);
	}

    //cout<<"For Problem 7a,K is "<<a0a<<"+"<<a1a<<"x"<<endl;
	cout<<"K is  for 7a is "<<a0a<<endl;
	cout<<"The error of K for 7a is "<<error<<endl;
//Problem 7b
	double y4[4] = {3,5,8,10};
	double x4[4]= {8.3,11.3,14.4,15.9};
	sumxi=0, sumyi=0,sumx2i=0,sumxiyi=0,sumx3i=0,sumx4i=0,sumx5i=0,sumx6i=0,sumx2iyi=0,sumx3iyi=0,sumlogyi=0,sumxilogyi=0,sumy2i=0;
	a0a=0,a1a=0,a2=0,a3=0,a0d=0,a1d=0;
	//double m=5;
	m = 4;
	//Degree 1
	for(i=0;i<m;i++){
		sumxi +=x4[i];
		sumyi +=y4[i];
		sumx2i +=(x4[i]*x4[i]);
		sumxiyi += (x4[i]*y4[i]);
		sumy2i += y4[i]*y4[i];
		
	}
	

	a0a=((m*sumxiyi)-(sumyi*sumxi))/(pow((sumx2i*m)-(sumxi*sumxi),0.50)*pow((sumy2i*m)-(sumyi*sumyi),0.50));
	//a1a=((m*sumxiyi)-(sumxi*sumyi))/((m*sumx2i)-(sumxi*sumxi));
	//Find Error
	
		error=0;
	for (i=0;i<m;i++){
		double pol=0;
		pol=a0a*(y4[i]-5.3);
		error +=pow(x4[i]-pol,2.0);
	}
    //cout<<"For Problem 7a,K is "<<a0a<<"+"<<a1a<<"x"<<endl;
	cout<<"K is  for 7b is "<<a0a<<endl;
	cout<<"The error of K for 7b is "<<error<<endl;	
	
	//*********Problem 11
	double x21[21] = {13,15,16,21,22,23,25,29,30,31,36,40,42,55,60,62,64,70,72,100,130};
	double y21[21]= {11,10,11,12,12,13,13,12,14,16,17,13,14,22,14,21,21,24,17,23,34};
	sumxi=0, sumyi=0,sumx2i=0,sumxiyi=0,sumx3i=0,sumx4i=0,sumx5i=0,sumx6i=0,sumx2iyi=0,sumx3iyi=0,sumlogyi=0,sumxilogyi=0;
	a0a=0,a1a=0,a2=0,a3=0,a0d=0,a1d=0;
	//double m=5;
	m = 21;
	//Degree 1
	for(i=0;i<m;i++){
		sumxi +=x21[i];
		sumyi +=y21[i];
		sumx2i +=(x21[i]*x21[i]);
		sumxiyi += (x21[i]*y21[i]);
	}
	

	a0a=((sumx2i*sumyi)-(sumxiyi*sumxi))/((sumx2i*m)-(sumxi*sumxi));
	a1a=((m*sumxiyi)-(sumxi*sumyi))/((m*sumx2i)-(sumxi*sumxi));
	//Find Error
	error=0;
	for (i=0;i<m;i++){
		double pol=0;
		pol=a0a + a1a*x21[i];
		error +=pow(y21[i]-pol,2.0);
	}

    cout<<"For Problem 11, the polynomial of degree 1 is "<<a0a<<"+"<<a1a<<"x"<<endl;
	cout<<"The Error for 11 is "<<error<<endl;
		

	/*
k= 0;
//double m=1.0f;
while(k<50){
for(i=0; i<3; i++){
 //cout<<temp[i]<<endl; 
 double tempSum =0.0f;
 double div=(1.0/A[i][i]);
 for (j=0;j<3;j++){
	 
    if(j !=i){
	   tempSum = tempSum+( -1.0f * A[i][j] * x0[j]);
	   
	}
 }
 temp[i] = div*(tempSum+b[i]);

 
}

k++;
memcpy(x0, temp, sizeof(temp));

}
//cout<<"The Solution to homework 9B after 25 iterations is:"<<endl;
for(i=0;i<3;i++){
	cout<<x0[i]<<endl;
	
}*/
   }
	


