print("Enter the list values to sort them in bubble sort: ")
l= list(map(int,input().split()))
print("the sorted order is: ")

for i in range(len(l)-1):
    mi=i
    for j in range(i+1,len(l)):
        if l[j]<l[mi]:
            mi=j
    l[i],l[mi]=l[mi],l[i]
    print("after",i,"step the output is ",l)
