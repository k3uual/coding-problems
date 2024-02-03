#include <bits/stdc++.h>
using namespace std;

class Solution{
    public:
    int count(int arr[], int n, int x) {
	    // code here'
	    int occur=0;
	    for(int i=0;i<n;i++){
	        if(arr[i]==x)
	            occur++;
	        if(arr[i]>x)
	            break;
	    }
	    return occur;
	}
};
int main(){
    Solution s;
    int a[]={1,2,2,2,4,5};
    cout<<s.count(a,6,2);
}