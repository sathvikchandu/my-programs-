def all_perms(elements):
    if len(elements) <=1:
        return elements
    else:
        tmp = []
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                tmp.append(perm[:i] + elements[0:1] + perm[i:])
        return tmp

for _ in range(int(input())):
    st=input()

    l= all_perms(st)
    flag=0
    for i in l:
        count=0
        for j in range(len(i)):
            if i[j]==st[j]:
                count+=1
        if count>0:
            continue
        if count==0:
            print("Case #"+str(_+1)+": "+i)
            flag=1
            break
    if flag==0:
        print("Case #"+str(_+1)+": "+"IMPOSSIBLE")




