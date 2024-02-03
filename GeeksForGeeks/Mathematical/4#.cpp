#include<iostream>
#include<vector>

class Solution{
	public:
	long long power (int b, int p) {
	    if (p == 0)
	        return 1;
	    if (p % 2 == 0) {
	        long long ans = power(b, p/2) % 1000000007;
	        return (ans * ans)  % 1000000007;
	    } else if (p % 2 == 1) {
	        return (b * (power(b, p-1) % 1000000007)) % 1000000007;
	    }
	}
   	int Nth_term(int a, int r, int n){
   	    // Code here
   	    return (a * power(r, n-1)) % 1000000007;
   	}
};

int main(){
    Solution s;
    std::cout<<s.Nth_term(5,6,10);
}