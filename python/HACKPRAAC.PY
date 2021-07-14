"""
l1= [[1,2,3],[4,5,6],[7,8,9]]
l=[]
for i in l1:
    for j in i:
        l.append(j)
print(l)
"""
"""
x= -121
y= str(x)
l= list(y)
l1= l[::-1]
z=""
for i in l1:
    z=z+i
if y==z:
    print("true")
else:
    print("false")

"""
"""
s= "heeladasd sad asd asd sad sadsadas"
l= s.split()

print(len(l[len(l)-1]))
"""
import math

def pythagorean_triplet(n):
    count=0
    for b in range(n):
        for a in range(1, b):
            c = int(math.sqrt( a * a + b * b))
            if c % 1 == 0 and c<=n:
                count+=1
                print(count, a,b,c)
            
            
pythagorean_triplet(10)