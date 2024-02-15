#include<iostream>
#include<vector>
#include<string>

using namespace std;
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        int stck[tokens.size()];
        int res = 0, Top = 0;
        for(int i = 0; i < tokens.size(); i++){
            int count = 0;
            if(tokens[i] == "+") {
                stck[Top-2] = stck[Top-2] + stck[Top-1];
                Top = Top - 1;
            }
            else if(tokens[i] == "-") {
                stck[Top-2] = stck[Top-2] - stck[Top-1];
                Top = Top - 1;
            }
            else if(tokens[i] == "*") {
                stck[Top-2] = stck[Top-2] * stck[Top-1];
                Top = Top - 1;
            }
            else if(tokens[i] == "/") {
                stck[Top-2] = stck[Top-2] / stck[Top-1];
                Top = Top - 1;
            }
            else {
                stck[Top] = stoi(tokens[i]);
                Top++;
            }
        }
        return stck[0];
    }
};

int main(){
    Solution s;
    vector<string> a = {"10","6","9","3","+","-11","*","/","*","17","+","5","+"};
    cout<<s.evalRPN(a);
}