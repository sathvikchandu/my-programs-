order="kqep"
stri="pekeq"
l1= list(order)
fst=""
l2= list(stri)
for i in l1:
    
    if i in l2:
        fst+=i
        l2.remove(i)
l3= list(fst)
l4=[]
for i in l3:
    l4.append(ord(i))
l5=[]
for i in l2:

    if ord(i) in l4:
        ind= l3.index(i)
        l3.insert(ind+1,i)
fstr=""
for i in l3:
    fstr+=i
print(fstr)