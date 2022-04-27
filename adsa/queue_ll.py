

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def enqueue(self,data):
        if self.head is None:
            self.head=Node(data) # create a new node
        
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next    # move to the last node
            curr.next=Node(data)
    def dequeue(self):
        if self.head is None:
            print("queue is empty")
        else:
            self.head=self.head.next
            print("popped element")
        
    
    def print(self):
        if self.head is None:
            print("stack is empty")
        else:
            curr=self.head
            while curr.next!=None:
                
                print(curr.data, end=" ")
                curr=curr.next
            print(curr.data)
            print()


l=LinkedList()
a=int(input("press 1 to enqueue and 0 to dequeue from the queue"))
while a==1 or a==0:
    if a==1:
        b=int(input("enter the number"))
        l.enqueue(b)
    else:
        l.dequeue()
    a=int(input("press 1 to append and 0 to pop from the stack"))
l.print()