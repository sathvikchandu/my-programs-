
"""
n= 4
count=0
for i in range(1,n//2+1):
    if n%i==0:
        count+=1
count=count+1
        
if count==3:
    print("true")

else:
    print("false")
    
l= [213,213,213,13,213,21,1,1,21,3,2]
l.sort()
l= l[::-1]
print(l)
"""

milestones=[9,3,6,8,2,1]
count=0
 
l=milestones
l= milestones[::-1]
first=0
last= len(l)-1

while last>first:
    while l[first]>0 and l[last]>0:
        a=l[first]
        a= a-1
        l[first]=a

        count=count+1
        #print("the output is genrated by l[i] and the value of first and count are : ",l[first],count)
        print(l)
        b=l[last]
        b=b-1
        l[last]=b
        count=count+1
        #print("the output is genrated by l[i] and the value of last and count are : ",l[last],count)
        print(l)
    if l[first]==0:
        first=first+1
    elif l[last]==0:
        last=last-1
if l[first]>0:
    count=count+1
print(count)
