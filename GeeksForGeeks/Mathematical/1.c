#include<stdio.h>
#include<stdlib.h>

void printPat(int n)
{
    int temp=n;
    while(temp>0){
        for(int i=n; i>0; i--){
            for(int j=temp; j>0; j--){
                printf("%d ",i);
            }
        }
        printf("$");
        temp--;
    }
}

int main(){
    printPat(5);
}