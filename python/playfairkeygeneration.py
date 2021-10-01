key= input("Enter key")
msg=
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