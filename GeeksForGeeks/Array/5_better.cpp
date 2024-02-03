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
        int a[d],i;
        for(i=0;i<d;i++)
            a[i] = arr[i];
        for (i = 0; i < n-d; i++)
            arr[i] = arr[i + d];
        for(int j=0;j<d;j++){
            arr[i]=a[j];
            i++;
        }
    }
};

int main(){
    Solution s;
    int a[]={40,3,29,4,1,82,48,39,60,52,36,35,40,93,16,28,5,30,50,65,86,30,44,36,78,1,39,72,50,90,68,89,93,96,44,45,30,91,83,41,42,70,27,33,62,43,61,18,24,62,82,10,91,26,97,68,78,35,91,27,25,58,15,69,6,59,13,87,1,47,27,95,17,53,79,30,47,91,48,71,52,81,32,94,58,28,13,87,15,56,13,91,13,80,11,70,90,75,56,42};
    s.rotateArr(a,44,100);
    for(int i=0;i<100;i++)
        cout<<a[i]<<",";
}