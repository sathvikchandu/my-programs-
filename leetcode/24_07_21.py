import collections
l= [1,2,132,1321,321,32,1,1,1,1]
d=collections.Counter(l)
l1=[]


res = {key: val for key, val in sorted(d.items(), key = lambda ele: ele[0], reverse = True)}
for val,key in res.items():
    for i in range(key):
        print(val)
#for value,key in d.items():
    

