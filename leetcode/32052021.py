n = input()
l=list(n)
print(l)
le=len(l)
l1=[]
l2=[]
count=0
count1=0
uk=0
if(le=='1'):
    if(l[0]=='0'):
        print("false")
    if(l[0]=='1'):
        print("TRUE")

for i in range(0,le,uk):
    print(uk)
    if(l[i]=='1'):
        while(l[count]!='0'):
            i=i+1
            count=count+1
        l1.append(count-1)
        i=count
    
    if(l[i]=='0'):
        while(l[count1]!='1'):
            i=i+1
            count1=count1+1
        l1.append(count1-1)
        i=count1
    if(count==0):
        uk=count1
    if(count1==0):
        uk=count
a=max(l1)
b=max(l2)
if(a>b):
    print("True")
if(b>a):
    print("false")