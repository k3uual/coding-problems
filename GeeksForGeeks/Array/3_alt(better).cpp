using namespace std;
#include<iostream>
#include<vector>

class Solution {
  public:	
	    // code here
    int print2largest(int arr[], int n) {
        int largest = arr[0];
        int secondLargest = -1;
        for(int i=1; i<n; i++){
            if(arr[i]>largest){
                secondLargest=largest;
                largest = arr[i];
            }
            if(arr[i] < largest && arr[i] > secondLargest)
                secondLargest = arr[i];
        }
        return secondLargest;
    }
};

int main(){
    int ar[]={10,20,30,40,50};
    Solution s;
    cout<<s.print2largest(ar,5);
}