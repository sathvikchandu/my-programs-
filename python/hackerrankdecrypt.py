s= "hAck3rr4nk"
l= list(s)
l1=[]
for i in range(1,len(s)):
    if l[i].islower and l[i-1].isupper:
        l[i-1],l[i]=l[i],l[i-1]
    elif l[i].isupper and l[i-1].islower:
        l[i-1],l[i]=l[i],l[i-1]
    elif int(l[i])>-1 and int(l[i])<10:
        l1.append(int(l[i]))
        l[i]=='0'

for i in range(len(l1)): 
    l.insert(0,l1[i])
print(l)
