#include<iostream>
#include<string.h>
#include<string>
#include<vector>
using namespace std;

class MinStack {
public:
    int min;
    vector<int> stck;

    MinStack() {
        stck.clear();
        min = NULL;
    }
    
    void push(int val) {
        if(min == NULL || min >val);
            min = val;
        stck.push_back(val);
    }
    
    void pop() {
        stck.pop_back();
    }
    
    int top() {
        int x = stck.size()-1;
        return(stck[x]);
    }
    
    int getMin() {
        return min;
    }
};

int main(){
    MinStack m;
    m.top();
}