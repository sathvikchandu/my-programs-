class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        ini0=0
        op=0
        for i in rungs:
            if (i-ini0)%dist==0:
                op+=(i-ini0)//dist-1
            else:
                op+=(i-ini0)//dist
            ini0=i
        return op