nums= [1,2,4,5,6,7,8,9]
target=11

for idx,num in enumerate(nums):
    diff = target -num
    if diff in nums: ## check if diff exists in nums list. this will take O(logN) time
        idx2 = nums.index(diff) ## this will return the index of where the second number, equal to diff is found. This will also take O(logN)
        if idx==idx2: ## if the two indexes are the same. ignore the solution because we cannot use same element in list twice to get to target
            continue
        print([idx,idx2]) ## if the two indexes are not the same return the two indexes. 