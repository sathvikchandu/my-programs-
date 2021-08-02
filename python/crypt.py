"""
file1 = open("myfile.txt", "w")
L = ["Hello, I am sathvik"]
  

file1.writelines(L)
file1.close()  
  
file1 = open("myfile.txt", "r+")
  
l=file1.read()



l1= list(l)
l2=[]
print(len(l1))
for i in l1:
    o=ord(i)
    l2.append(o)
print(l2)
l3=[]
for i in l1:
    o=ord(i)+4
    l3.append(o)
print(l3)
stri=""
for i in l3:
    op= chr(i)
    stri+=op
print(l)
print(stri)
"""

for i in range(int(input())):
    x,y=input().split()
    x= int(x)
    y= int(y)
    ans=0
    if x%2==0 and y%2==0:
        ans=0
    
    elif x%2==0 and y%2==1 :
        ans=1
    elif x%2==1 and y%2==0:
        ans=1
    else:
        ans=2
    print(ans)
    
    
        



