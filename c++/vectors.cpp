#include<iostream>  
#include<vector>  
#include<iterator>  
#include<algorithm>    // for running of the sorting algorithms we need to include this
using namespace std;  
int main()  
{  
vector<int> v;  
v.push_back(1);  
v.push_back(2);  
v.push_back(3);  
v.push_back(4);  // for appending elements to the vector
v.push_back(5);  
for(auto i =v.cbegin();i!=v.end();++i)  
cout<<*i;  
cout<<"enter the size of the vector"<<endl;
int n;
cin>>n;
for(int i =0;i<n;i++){
    int temp=0;
    cin>>temp;
    v.push_back(temp);
}
sort(v.rbegin(),v.rend());
bool isth=binary_search(v.begin(),v.end(),11);  //returns 1 if the elent is present 
cout<<isth<<endl;

for(int i =0;i<v.size();i++){
    cout<<v[i]<<" ";
}
cout<<endl;

//vector<int>::iterator it= lower_bound(v.begin(), v.end(),2);    // it returns the element greater than or equal to the number choosen
//vector<int>::iterator it2= upper_bound(v.begin(),v.end(),5);    // returs the number greter than the number choosen from the vector
//cout<<*it2<<" "<<*it<<endl;
for(int i: v){  //his is an alternative than writing all the for loop shit
    cout<<i<<" ";
}

//instead of writing vector<int>::iterator, we can simply write auto
return 0;   

}

/**  THESE ARE ALL THE INBUILT FUNCTIONS IN VECTORS
begin() – Returns an iterator pointing to the first element in the vector
end() – Returns an iterator pointing to the theoretical element that follows the last element in the vector
rbegin() – Returns a reverse iterator pointing to the last element in the vector (reverse beginning). It moves from last to first element
rend() – Returns a reverse iterator pointing to the theoretical element preceding the first element in the vector (considered as reverse end)
cbegin() – Returns a constant iterator pointing to the first element in the vector.
cend() – Returns a constant iterator pointing to the theoretical element that follows the last element in the vector.
crbegin() – Returns a constant reverse iterator pointing to the last element in the vector (reverse beginning). It moves from last to first element
crend() – Returns a constant reverse iterator pointing to the theoretical element preceding the first element in the vector (considered as reverse end)
**/
