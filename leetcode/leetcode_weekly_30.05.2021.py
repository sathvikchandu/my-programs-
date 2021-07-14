
fw="aaa"
sw="cba"
tw="cdb"
temp1=""
temp2=""
temp3=""
f1w=fw.lstrip("a")
s2w=sw.lstrip("a")
t2w=tw.lstrip("a")
l1=list(f1w)
l2= list(s2w)
l3= list(t2w)
for i in l1:
    temp1+=str(ord(i)-ord("a"))

for i in l2:
    temp2+=str(ord(i)-ord("a"))
for i in l3:
    temp3+=str(ord(i)-ord("a"))
if(temp1==""):
    temp1=int(0)
if(temp2==""):
    temp2=int(0)

if(int(temp1)+int(temp2)==int(temp3)):
    print("true")

