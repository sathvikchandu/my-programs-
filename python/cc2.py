t=int(input())
for i in range(t):
    a=0 
    b=0 
    c=0 
    l=[]
    for i in range(3):
        tic=input()
        l.append(tic)
    for i in range(3):
        for j in range(3):
            if l[i][j]=='X':
                a+=1
            elif l[i][j]=='O':
                b+=1
            elif l[i][j]=='_':
                c+=1
    
    d=0 
    e=0 

    if l[0][0]=='X' and l[0][1]=='X' and l[0][2]=='X':
        d=1
    if l[1][0]=='X' and l[1][1]=='X' and l[1][2]=='X':
        d=1
    if l[2][0]=='X' and l[2][1]=='X' and l[2][2]=='X':
        d=1
    if l[0][0]=='X' and l[1][0]=='X' and l[2][0]=='X':
        d=1
    if l[0][1]=='X' and l[1][1]=='X' and l[2][1]=='X':
        d=1
    if l[0][2]=='X' and l[1][2]=='X' and l[2][2]=='X':
        d=1
    if l[0][0]=='X' and l[1][1]=='X' and l[2][2]=='X':
        d=1
    if l[0][2]=='X' and l[1][1]=='X' and l[2][0]=='X':
        d=1
    
    if l[0][0]=='O' and l[0][1]=='O' and l[0][2]=='O':
        e=1
    if l[1][0]=='O' and l[1][1]=='O' and l[1][2]=='O':
        e=1
    if l[2][0]=='O' and l[2][1]=='O' and l[2][2]=='O':
        e=1
    if l[0][0]=='O' and l[1][0]=='O' and l[2][0]=='O':
        e=1
    if l[0][1]=='O' and l[1][1]=='O' and l[2][1]=='O':
        e=1
    if l[0][2]=='O' and l[1][2]=='O' and l[2][2]=='O':
        e=1
    if l[0][0]=='O' and l[1][1]=='O' and l[2][2]=='O':
        e=1
    if l[0][2]=='O' and l[1][1]=='O' and l[2][1]=='O':
        e=1
    
    if(d==1 and e==1) or (a-b<0) or(a-b>1):
        print(3)
    
    elif d==1 and e==0 and a>b:
        print(1)
    elif a==0 and b==0 and c==9:    
        print(2)
    elif d==0 and e==1 and a==b:
        print(1)
    elif d==0 and d==0 and c==0:
        print(1)
    elif d==0 and e==0 and c>0:
        print(2)
    else:
        print(3)