import functools
import copy
nums=[1,2,3,4,5,6,7,8,9,10]
subsets = [[]]
l1=[]
for n in nums:
    prev = copy.deepcopy(subsets)
    [k.append(n) for k in subsets]
    subsets.extend(prev)
print(subsets)
for i in subsets:
    if(len(i)>1):
        res = functools.reduce(lambda x, y: x ^ y, i)

        l1.append(res)
    if(len(i)==0):
        continue
    
    if(len(i)==1):
        l1.append(i[0])
print(l1)
print(sum(l1))