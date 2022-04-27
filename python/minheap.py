from turtle import right


class Maxheap:
    def __init__(self,size):
        self.size=size
        self.heap = [0]*(size+1)
        self.count = 0
    
    def insert(self,data):
        
        self.count+=1
        

        if self.count>self.size:
            self.count-=1
            return "overflow"
            

        self.heap[self.count]=data

        idx=self.count

        while idx>1 and self.heap[idx]>self.heap[idx//2]:
            self.heap[idx],self.heap[idx//2]=self.heap[idx//2],self.heap[idx]
            idx=idx//2
    def prin(self):
        return self.heap[1:self.count+1]

    def pop(self):
        if self.count<1:
            return "underflow"
        relem=self.heap[1]
        self.heap[1]=self.heap[self.count]
        self.count-=1
        idx=1
        while idx<=self.count//2:
            left= idx*2
            right= idx*2+1
            if self.heap[idx]<self.heap[left] or self.heap[idx]<self.heap[right]:
                if self.heap[left]>self.heap[right]:
                    self.heap[idx],self.heap[left]=self.heap[left],self.heap[idx]
                    idx=left
                else:
                    self.heap[idx],self.heap[right]=self.heap[right],self.heap[idx]
                    idx=right
            else:
                break
        return relem

          
    


class Minheap:
    def __init__(self,size):
        self.size=size
        self.heap = [0]*(size+1)
        self.count = 0
    
    def insert(self,data):
        self.count+=1
        if self.count>self.size:
            return "overflow"
        self.heap[self.count]=data

        idx=self.count
        while idx>1 and self.heap[idx]<self.heap[idx//2]:
            self.heap[idx],self.heap[idx//2]=self.heap[idx//2],self.heap[idx]
            idx=idx//2
    def prin(self):
        return self.heap[1:self.count+1]

    def pop(self):
        relem=self.heap[1]
        self.heap[1]=self.heap[self.count]
        self.count-=1
        idx=1

        while idx<=self.count//2:
            left = idx*2
            right = idx*2+1

            if self.heap[idx]>self.heap[left] or self.heap[idx]>self.heap[right]:
                if self.heap[left]<self.heap[right]:
                    self.heap[idx],self.heap[left]=self.heap[left],self.heap[idx]
                    idx=left
                else:
                    self.heap[idx],self.heap[right]=self.heap[right],self.heap[idx]
                    idx=right
            else:
                break
        return relem
    





if __name__ == '__main__':
    maxheap= Maxheap(5)
    maxheap.insert(3)
    maxheap.insert(1)
    maxheap.insert(2)
    print(maxheap.prin())

    minheap= Minheap(5)
    minheap.insert(3)
    minheap.insert(1)
    minheap.insert(2)
    print(minheap.prin())



