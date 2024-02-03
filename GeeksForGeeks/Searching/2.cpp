#include <bits/stdc++.h>
using namespace std;

class Solution{
    public:
    int countBuildings(int h[], int n) {
	    // code here
	    int sun_bld=h[0],count=1;
	    for(int i=1;i<n;i++){
	        if(h[i]>sun_bld){
	            count++;
	            sun_bld=h[i];
	        }
	    }
	    return count;
	}
};
int main(){
    Solution s;
    int a[]={9,7,2,16,4};
    cout<< s.countBuildings(a,5);
}