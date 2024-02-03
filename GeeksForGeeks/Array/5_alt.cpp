using namespace std;
#include<iostream>

class Solution {
  public:
    public:
    //Function to rotate an array by d elements in counter-clockwise direction. 
    void rotateArr(int arr[], int d, int n){
        if(d>n)
            while(n<d)
                d-=n;
        for (int i = 0; i < d; i++) {
        int x = arr[0]; 
        for (int j = 0; j < n - 1; ++j) 
            arr[j] = arr[j + 1]; 
        arr[n - 1] = x; 
        } 
    }
};

int main(){
    Solution s;
    int a[]={1,2,3,4,5};
    s.rotateArr(a,103,5);
    for(int i=0;i<5;i++)
        cout<<a[i];
}