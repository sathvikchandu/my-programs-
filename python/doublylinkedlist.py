class Node:
    def __init__(self,data):
         self.data=data
         self.next=None
         self.prev=None
class dll:
    def __init__(self):
        self.head=None
    

    def append(self,data):
        if self.head is None:
            nn=Node(data)
            nn.prev=None
            self.head=nn
        
        else:
            nn=Node(data)
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=nn
            nn.prev=curr
            nn.next=None


    def prepend(self,data):
        if self.head is None:
            curr=Node(data)
            curr.prev=None
            self.head= curr
        
        else:
            curr=Node(data)
            self.head.prev=curr
            curr.next=self.head
            curr.prev=None
            curr=self.head


    def length(self):
        curr= self.head
        le=0
        while curr:
            curr=curr.next
            le=le+1
        return le


    def printl(self):
        curr=self.head
        while curr!=None:
            print(curr.data)
            curr=curr.next
    
    def delete(self,pos):
    
        
        if(self.length()==0):               #should get corrected
            print("the list is empty")
        
        elif pos==1:
            curr=self.head
            curr.next=curr
            ne=curr.next
            self.head.next=ne
            ne.prev=None
            
            

dl=dll()

dl.append(2)
dl.append(3)
dl.append(4)
dl.prepend(9)
dl.printl()



