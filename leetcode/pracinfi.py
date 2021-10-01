l= [1,2,3,1,2]
st=""
for i in l:
    st+=i
if l==l[::-1]:
    print("yes")
elif l!=l[::-1]:
    print("no")