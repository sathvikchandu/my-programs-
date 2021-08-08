"""
s="MCMXCIV"
d= {
            
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000,
    
}

count=0
n = len(s)
i= n-1

while i>=0:
    if (i<n-1 and (d[s[i]] < d[s[i+1]])):
        count-=d[s[i]]
        print(d[s[i]])
    else:
        count+=d[s[i]]
        print(d[s[i]])
    i-=1


print(count)


nums1=[1,2]
nums2=[3,4]
nums1.extend(nums2)
nums1.sort()
if len(nums1)==1:
    res=nums1[0]
elif len(nums1)%2==0:
    left=int(len(nums1)/2)-1
    right=int(len(nums1)/2)
    res= (nums1[left]+nums1[right])/2
    print(right)
    print(left)

elif len(nums1)%2!=0:
    res= nums1[int(len(nums1)/2)]
print(float(res))
"""
s= "aaabaaaa"
if len(s)<=3:
    if s[0]==s[1] and s[1]==s[2]:
        print(s[0]+s[1])
    else:
        
        print(s)
l=[]
s1=list(s)
for i in range(len(s)-2):
    if s1[i]==s1[i+1] and s1[i+1]==s1[i+2]:
        c=i
        l.append(i)

for i in l:
    s1[i]="#"
print(s1)
    
st=""
for i in range(len(s1)):
    if s1[i]!="#":
        st+=s1[i]
print(st)
