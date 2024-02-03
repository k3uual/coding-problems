using namespace std;
#include<iostream>
#include<vector>


int loc=0;
bool searchEle(vector<int>&a,int x){
    for(int i=0;i<a.size();i++){
        if(a[i]==x)
            return 1;
        loc++;
    }
    return 0;
}

void insertEle(vector<int>&a, int y, int yi) {
    a.insert(a.begin() + yi, y);
}

bool deleteEle(vector<int>&a,int z){
    if(searchEle(a,z)){
        a.erase(a.begin()+loc);
        return 1;
    }  
    return 0;
}

int main(){
    vector <int>a={10,20,30,40,50,60};
    insertEle(a,22,2);
    std::cout<<"element deleted: "<<deleteEle(a,50)<<"\n";
    cout<<"element searched: "<<searchEle(a,22)<<"\n";
    for(int i=0;i<a.size();i++)
        cout<<a[i]<<"  ";
}