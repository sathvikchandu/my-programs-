import math
n = int(input())
for i in range(n):
    c=int(input())
    
    d= (math.log(c)/math.log(2))+1
    d=int(d)
    lower=math.pow(2,d-1)
    lower=int(lower)
    upper=math.pow(2,d)-1
    upper=int(upper)
    a=upper-lower
    b=a^c
    print(a*b)

