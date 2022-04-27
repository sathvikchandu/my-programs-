class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self,data=None):
        self.head = Node()

    def append(self,data):
        new_node = Node(data)
        curr= self.head
        while curr.next!=None:
            curr=curr.next
        curr.next = new_node
    
    def length(self):
        count=0
        curr=self.head
        while curr.next!=None:
            count+=1
            curr=curr.next
        return count
    
    def display(self):
        curr=self.head
        while curr.next!=None:
            curr=curr.next
            print(curr.data, end=" ")
        print()
    
    def display_reverse(self):
        l=[]
        curr=self.head
        while curr.next!=None:
            curr=curr.next
            l.append(curr.data)
        for i in l[::-1]:
            print(i, end=" ")

    
mylist= LinkedList()
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.display()


mylist.display_reverse()

        
