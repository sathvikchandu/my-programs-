n = int(input())
l=[]
l1=[]
for i in range(n):
    ele= int(input())
    l.append(ele)
if(l[0]<=l[1]):
    l1.append(1)
    l1.append(2)
else:
    l1.append(2)
    l1.append(1)
for i in range(2,n):
    if(l[i]<=l[i-1]):
        if(l1[i-1]>2):
            l1.append(2)
        elif(l1[i-1]==2):
            l1.append(l1[i-1]-1)
    else:
        l1.append(l1[i-1]+1)
print(sum(l1))