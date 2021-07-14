class node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

class ll:
    def __init__(self):
        self.head=node()
    
    def append(self,pos,data):
        new_node=node(data)
        
        if(pos==1):
            x=node()
            y=node()
            x=self.head
            y= x.next
            new_node.next=y
            x.next=new_node

        elif(pos>1 and pos<self.length()):
            x=self.head
            y=x.next
            while(pos>0):
                x=x.next
                y=y.next
                pos=pos-1
            new_node.next=y
            x.next=new_node
        
        else:

            curr= self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=new_node
       
    
    def length(self):
        curr=self.head
        count=0
        while curr.next!=None:
            count=count+1
            curr=curr.next
        return count
    
    def display(self):
        curr= self.head
        li=[]
        while curr.next!=None:
            curr=curr.next
            li.append(curr.data)
        return li
    
    def get(self,pos):
        if(pos>self.length()):
            print("not possible")
        else:
            curr=self.head
            r=pos
            while r>0:
                curr=curr.next
                r=r-1
            return curr.data
    
    def remo(self,ele):
        if(ele>=self.length() or ele<0):
            print("Not possible")
        else:
            
            curr= self.head
            while ele>0:
                lastnode=curr
                curr=curr.next
                ele=ele-1
            lastnode.next=curr.next




l = ll()
l.append(1,2)
l.append(2,3)
l.append(3,4)
l.append(2,5)
l.append(4,3)
l.append(3,7)
print(l.length())
print(l.display())

l.remo(4)
print(l.display())
