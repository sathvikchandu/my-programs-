class Node:
    def __init__(self,data):
        self.data = data
        self.l = None
        self.r = None
    
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.l is None:
                    self.l = Node(data)
                else:
                    self.l.insert(data)
            elif data>self.data:
                if self.r is None:
                    self.r = Node(data)
                else:
                    self.r.insert(data)
            else:
                self.data = data
    def print_tree(self):

        
        print(self.data)
        if self.l:
            self.l.print_tree()
        
        if self.r:
            self.r.print_tree()

    def find_max(self):
        max= self.data
        min= self.data
        if self.l:
            if max<self.l.data:
                max = self.l.data
            if min>self.l.data:
                min = self.l.data
            self.l.find_max()
        if self.r:
            if max<self.r.data:
                max = self.r.data
            if min>self.r.data:
                min = self.r.data
            self.r.find_max()
        return max,min
       

print("Enter the root node :")
root=Node(int(input())) 

print("Enter the elements as spaced integers :")

l=list(map(int,input().split()))
k=int(input("Enter the Kth smallest and largest element u wanna find :"))

l.sort()

print("The Kth smallest element is :",l[k])
l=l[::-1]
print("The Kth largest element is :",l[k])

for i in l:
    root.insert(i)
print("The tree is :")
print(root.print_tree())   


