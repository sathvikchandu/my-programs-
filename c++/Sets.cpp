#include<iostream>  
#include<set>  
#include<iterator>  
#include<algorithm>    
using namespace std;  
int main(){
    set<int> s;
    s.insert(1);
    s.insert(2);
    s.insert(-5);  //sets on default sorts the elements in ascending order
    s.insert(10);
    for(int i: s){
        cout<<i<<" ";
    }

    auto it = s.find(2); // find finds the element requested if not found it returns set.end(), the same case goes for upper and lower bounds
    if(it==s.end()){
        cout<<"element not found"<<endl;
    }
    else{
        cout<<"element found at "<<*it<<endl;
    }

    auto it1 = s.lower_bound(-5);
    if(it1==s.end()){
        cout<<"element not found"<<endl;
    }
    else{
        cout<<*it1<<endl;
    }

    s.erase(*it1);    // erased at o(logn) time 
    
    for(int i: s){
        cout<<i<<" ";
    }

    



}