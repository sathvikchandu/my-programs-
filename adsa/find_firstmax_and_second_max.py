print("Enter the list values to find the first and second max: ")
l= list(map(int,input().split()))
s=set(l)
l=list(s)
print("The first max is: ",max(s))
print("The second max is: ",l[len(s)-1])