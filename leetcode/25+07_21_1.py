class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def sumdigi(su):
            su= str(su)
            l3=list(su)
            so=0
            for i in l3:
                so+=int(i)
            return so 
    
    
        l1=""
        
        l=list(s)
        for i in l:
            o=ord(i)%96
            o=ord(i)%96
            l1+=str(o)
    

        su=int(l1)
        for i in range(k):
            st=sumdigi(su)
            su=st
        return su
