#include<iostream>

int missingNumber(int A[], int N)
{
    /* the below equation find the sum of all the
    N numbers to find the one missing number*/
    int Total=((N)*(N+1))/2;
    int arr_sum=0;
    for(int i=0;i<N-1;i++)
        arr_sum+=A[i];
        
    return Total-arr_sum;
}

int main(){
    int a[]={2,1,3};
    std::cout<<"the one missing number is: "<<missingNumber(a,4);
}