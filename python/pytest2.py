
x= -23450
"""
if(x>0):
    x= str(x)
    l = list(x)
    l1=l[::-1]
    st=""
    for i in l1:
        st=st+i
    st.lstrip("0")
    print(st)

elif(x<0):
    x= str(x)
    l = list(x)
    l1=l[::-1]
    l1.pop()
    
    st="-"
    for i in l1:
        st=st+i
    st.lstrip("0")
    print(st)

reverse = str(x)[1:][::-1]
print(reverse)
reverse = int(reverse)
print(reverse)
reverse*=-1
print(reverse)


reverse = str(x)[:][::-1]
print(reverse)
"""


print(int(x))