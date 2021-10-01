key= input("Enter key")
msg=input("ENTER MSG: ")
l=[]
for e in key.lower():    #only accepts lower case characters
    if e not in l:
        if e=='i' or e=='j': #we need to put i and j in the same block
            e= 'i/j'
            l.append(e)
        else:

            l.append(e)
alphab="abcdefghijklmnopqrstuvwxyz"
for a in alphab:    

    if a not in l:                      #if its not present in the key list, then append the characters
        if a=='i' or a=='j':
            a= 'i/j'                         #we donno here i or j comes so i added the loop above and below
            if a in l:
                continue
                
        
            l.append(a)
        else:

            l.append(a)
s1=l[0:5]
s2=l[5:10]
s3=l[10:15]                                             #splitting into arrays
s4=l[15:20]
s5=l[20:25]
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)


finalmat=[s1,s2,s3,s4,s5]

encrypt=[(msg[i:i+2]) for i in range(0,len(msg),2)]
for grp in encrypt:
    grp=list(grp)
    if len(grp)==1:
        grp[1]='z'
    a=grp[0]
    b=grp[1]

    for i in range(len(finalmat)):
        for j in range(len(finalmat)):
            if finalmat[i][j]==a:
                c=i
                d=j
            elif finalmat[i][j]==b:
                e=i
                f=j
    
    if d==f:
        c+=1
        c=c%5
        e+=1
        e=e%5

    elif c==e:
        d+=1
        d=d%5
        f+=1
        f=f%5
    elif c!=e or d!=f:
        e,d=d,e
        c,f=f,c
    
    
    grp[0]=finalmat[e][f]
    grp[1]=finalmat[c][d]



print("CIPHER TEXT: ",encrypt)



        



