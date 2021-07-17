
        
nums=[1,-1,12,21321,321]
target=250        
        
if not nums or len(nums)<4:
    print([])


res=[]
nums.sort()
for i in range(len(nums)-3):
    if i>0 and nums[i]==nums[i-1]:
        continue
    for j in range(i+1,len(nums)-2):
        if j>i+1 and nums[j]==nums[j-1]:
            continue
        l=j+1
        r=len(nums)-1
        sum1=nums[i]+nums[j]
        while(l<r):
            sum2 = sum1+nums[l]+nums[r]
            if sum2==target:
                res.append([nums[i],nums[j],nums[l],nums[r]])
                l+=1
                r-=1
                
                while l<r and nums[l]==nums[l-1]:
                    l+=1
                while l<r and nums[r]==nums[r+1]:
                    r-=1
            elif sum2 < target:
                l+=1
            else:
                r-=1
print(res)