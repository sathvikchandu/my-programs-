x= "x+"
l= list(x)
l1=[]
l2=[] 
l3=[]
l4=[]
for i in l:
    if ord(i)>=48 and ord(i)<58:
        l1.append(i)
    elif ord(i)>=65 and ord(i)<91:
        l2.append(i)
    elif ord(i)>=97 and ord(i)<123:
        l2.append(i)
    elif ord(i)>=42 and ord(i)<47 and ord(i)!=44 and ord(i)!=46:
        l3.append(i)
    
    elif ord(i)>=58 and ord(i)<63:
        l3.append(i)
    elif ord(i)==44 or ord(i)==46 or ord(i)==41 or ord(i)==40:
        l4.append(i)


print("constants are :",l1)
print("identifiers are :",l2)
print("delimitor are : ",l4)
print("operators are : ",l3)
    
    