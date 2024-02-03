#include <bits/stdc++.h>
using namespace std;

class Solution{
    public:
    void bubbleSort(int arr[], int n)
    {
        // Your code here 
        int temp;
        for(int i=0;i<n-1;i++){
            for(int j=0;j<n-i-1;j++){
                if(arr[j]>arr[j+1]){
                    temp=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=temp;
                }
            }
        }
    }
};
int main(){
    Solution s;
    int a[]={24,18,38,43,14,40,1,54};
    s.bubbleSort(a,8);
    for(int i=0;i<8;i++)
        cout<<a[i]<<",";
}
