#include<iostream>
#include<string.h>
#include<string>
#include<vector>
using namespace std;

class MinStack {
public:
    vector<int> stck; 
    vector<int> min;

    MinStack() {
        cout<<"minstack\n";
        stck.clear();
        min.clear();
        min.push_back(2147483647);
    }
    
    void push(int val) {
        int x = min.size()-1;
        if(min[x] >= val)
            min.push_back(val);
        stck.push_back(val);
    }
    
    void pop() {
        int x = stck[stck.size()-1];
        int min_top = min[min.size()-1];
        if(min_top == x)
            min.pop_back();
        stck.pop_back();
    }
    
    int top() {
        int x = stck.size()-1;
        return(stck[x]);
    }
    
    int getMin() {
        int x = min.size()-1;
        if(x == 0){
            cout<<"run";
            return NULL;
        }
        return min.at(x);
    }
};

int main(){
    MinStack m;
    int choice, val;
    // printf("Enter choice:\n");
    // scanf("&%d",choice);
    // while(choice < 5){
    //     switch (choice){
    //         case 1:
    //             printf("enter data: ");
    //             scanf("&%d",val);
    //             m.push(val);
    //             break;
    //         case 2:
    //             m.pop();
    //             break;
    //         case 3:
    //             m.top();
    //             break;
    //         case 4:
    //             m.getMin();
    //             break;
    //         default:
    //             printf("exit");
    //             break;
    //     }
    // }
    m.push(-2);
    m.push(0);
    m.push(-3);
    cout<<m.getMin();
    m.pop();
    cout<<m.top();
    cout<<m.getMin();
    m.pop();
    m.pop();
    cout<<m.getMin();
}