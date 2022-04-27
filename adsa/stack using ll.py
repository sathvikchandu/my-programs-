

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        if self.head is None:
            self.head=Node(data)
        
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=Node(data)
    def pop(self):
        if self.head is None:
            print("stack is empty")
        else:
            curr=self.head.next
            c=self.head
            while curr.next!=None:
                curr=curr.next
                c=c.next
            data= c.data
            c.next=None
            return data
    
    def print(self):
        if self.head is None:
            print("stack is empty")
        else:
            curr=self.head
            while curr.next!=None:
                print(str(curr.data)+"->",end="")
                curr=curr.next
            print(curr.data)
            print()



l=LinkedList()
a=int(input("press 1 to append and 0 to pop from the stack"))
while a==1 or a==0:
    if a==1:
        b=int(input("enter the number"))
        l.append(b)
    else:
        l.pop()
    a=int(input("press 1 to append and 0 to pop from the stack"))
l.print()