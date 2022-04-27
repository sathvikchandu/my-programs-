def insort(res):
    for z in range(1, len(res)):
        temp=res[z]
        q=z-1
        while q>=0 and res[q]>temp:
            res[q+1]=res[q]
            q-=1
        res[q+1]=temp
        print("after",z,"iteration the list is ",res)
    return res



print("Enter the number of elements as spaced integers: ")
l=list(map(int,input().split()))
print("The sorted list is: ",insort(l))