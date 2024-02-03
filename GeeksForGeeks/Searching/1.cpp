#include <bits/stdc++.h>
using namespace std;

class Solution{
    public:
    int search(int arr[], int n, int k) {
	    // code here
	    int i;
	    for(i=0; i<n && arr[i]!=k; i++);
	    if(i==n)
	        return -1;
	    return i+1;
	}
};
int main(){
    Solution s;
    int a[]={9,7,2,16,4};
    cout<< s.search(a,5,16);
}