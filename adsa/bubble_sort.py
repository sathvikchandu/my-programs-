print("Enter the elements to sort them in bubbble sort: ")
l= list(map(int,input().split()))

le=len(l)
for p in range(0,le-1):
    for j in range(0,le-1-p):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
    print("after",p,"step the output is",l)
        