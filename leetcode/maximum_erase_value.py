from itertools import combinations
nums=[4]
if(len(nums)==1):
    print(nums[0])
else:
    m= len(nums)
    l=[]

    k = len(nums)**2
    i = 0
    j = 0
    m=0
    while(i<len(nums)+1 and m<k):
        if(len(nums[i:j])>0):
            l.append(nums[i:j])
        j+=1
        if(j==len(nums)+1):
            i+=1
            j=0
        m+=1
    print(l) 
    l1=[]
    for i in l:
        if(any(i.count(element) > 1 for element in i)):
            pass
        else:
            l1.append(i)
    print(l1)
    l2=[]
    for i in l1:
        if(len(i)>1):
            l2.append(sum(i))
        else:
            l2.append(i[0])
    print(l2)
    print(max(l2))