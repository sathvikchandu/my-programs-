import collections
s="aaabb"
l= list(s)
d=collections.Counter(l)
l1=[]
for value,key in d.items():
    l1.append(key)
s= set(l1)
if len(s)==1:
    print("yes")  #this shouldn't work because it ain't correct but i donno how it accepted the wrong answer and rejected the right answer!!!
