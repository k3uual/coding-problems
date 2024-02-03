#include<iostream>
using namespace std;

int findMissing(int arr[], int n) {
    // code here
    int miss=arr[1]-arr[0];
    if(arr[2]-arr[1]<miss)
        miss=arr[2]-arr[1];
    
    if(n==2)
        return miss/2+arr[0];
    
    for(int i=0;i<n-1;i++)
        if(arr[i+1]-arr[i]>miss)
            return arr[i]+miss;
}
int main(){
    int arr[]={-42,-16};
    cout<<findMissing(arr,2);
}