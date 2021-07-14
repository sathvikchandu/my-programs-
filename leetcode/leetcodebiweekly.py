s="lGaWqAkfVIFhqBzRs3 l2 bwKhelcNiyNBpjGUN1"
l=s.split()
print(l)
l2=[]
for i in l:
    l1=[char for char in i]
    n= l1[-1]
    n = int(n)
    Remove_last = i[:-1]
    l2.insert(n-1,Remove_last)
    print(l2)


st=""
for i in l2:
    st=st+i+" "
print(st)

