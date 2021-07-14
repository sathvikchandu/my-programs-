s="32"
x=3
l= list(s)
pos=0
temp=""
if(int(s)>0):
    for i in l:
        if(x>int(i)):
            l.insert(pos,str(x))
    
    for i in l:
        temp=temp+i
    pos=pos+1
print(int(temp))    


