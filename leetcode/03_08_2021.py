import copy
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
         
        
        subsets=[[]]
        for n in nums:
            prev = copy.deepcopy(subsets)
            [k.append(n) for k in subsets]
            subsets.extend(prev)
        l=copy.deepcopy(subsets)

        new_subsets=[]
        for i in l:
            i.sort()
        for i in l:
            if i not in new_subsets:
                new_subsets.append(i)
        return new_subsets
