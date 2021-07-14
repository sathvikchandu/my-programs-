s = "111000"

lis=list(s)
m = len(s)
if(len(lis)==1):
    if(lis[0]=='0'):
        print("false")
    if(lis[0]=='1'):
        print("true")
l = []
for i in range(m+1):
    for j in range(m+1):
        l.append(s[i:j])
zerol= []
onel = []
for i in l:
    if "0" not in i:
        onel.append(i)
    elif "1" not in i:
        zerol.append(i)
longest_zero = max(zerol, key=len)  
longest_one =   max(onel, key=len)
print(longest_one)
print(longest_zero)
a=list(longest_one)
b=list(longest_zero)

if(len(longest_one)>len(longest_zero)):
    print("true")
else:
    print("false")