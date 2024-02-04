#include <string>
#include<string.h>
#include<iostream>
using std::string;
using namespace std;

class Solution {
public:
    
    bool isValid(string s) {
        int max = s.length();
        char stack[max];
        int top = 0, i = 0;
        while(i < max){
            //pop:
            if(top > 0 && check(stack[top-1],s[i])){
                top--;
            }
            //push:
            else{
                if(i == max){
                    return 0;
                }
                stack[top] = s[i];
                top++;
            }
            i++;
        }
        if(top == 0)
            return 1;
        return 0;
    }
    bool check(char st,char s){
        if(st == '(' && s == ')')
            return 1;
        if(st == '[' && s == ']')
            return 1;
        if(st == '{' && s == '}')
            return 1;
        return 0;
    }
};

int main(){
    Solution s;
    cout << s.isValid("()[]{}");

}