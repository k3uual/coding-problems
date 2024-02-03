using namespace std;
#include<iostream>
#include<vector>

int sumElement(int arr[],int n){
    for(int i=1;i<n;i++)
        arr[i]+=arr[i-1];
    return arr[n-1];
}

int main(){
    int ar[]={10,20,30,40,50};
    cout<<sumElement(ar,5);
}