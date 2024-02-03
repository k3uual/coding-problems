#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        int s_sum=0,t_sum=0;
        if(t.length()==s.length()){
            for (int i = 0; s[i] != '\0'; i++){
                s_sum+= s[i];
                t_sum+= t[i];
            }
            if(s_sum==t_sum)
                return true;
        }
        return false;
    }
};

int main(){
    Solution sol;
    cout<<sol.isAnagram("anagram","gramana");
}