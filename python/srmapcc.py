s= input()
l= list(s)
l1=[]
l2=[]
for i in l:
    if ord(i)>=48 and ord(i)<58:
        l1.append(ord(i))
    elif ord(i)>=97 and ord(i)<123:
        l1.append(ord(i))
for i in range(48,58):
    if i not in l1:
        l2.append(i)
for i in range(97,123):
    if i not in l1:
        l2.append(i)
l2.sort()
st=""
for i in l2:
    st+=chr(i)
print(st)