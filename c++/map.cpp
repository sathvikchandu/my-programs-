#include<iostream>  
#include<map>  
#include<iterator>  
#include<algorithm>    
using namespace std;  
int main(){
    map<int,int> a;
    a[1] = 1;
    a[2] = 100;
    a[100]=101;
    
    map<char,int> cnt;
    string x = "siva sathvik chandu";

    for(char c:x){
        cnt[c]++;
    } 
    cout<< cnt['a'] << endl;
}