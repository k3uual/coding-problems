using namespace std;
#include<iostream>
#include<vector>

pair<long long, long long> getMinMax(long long a[], int n) {
    int max=a[0],min=a[0];
    for(int i=0;i<n;i++){
        if(a[i]>max)
            max=a[i];
        if(a[i]<min)
            min=a[i];
    }
    return make_pair(min,max);
}

int main(){
    long long ar[]={10,20,30,40,50};
    pair<long long,long long> p= getMinMax(ar,5);
    cout<<p.first<<" "<<p.second;
}