from tkinter import W


class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self,data=None):
        self.head = Node()

    def append(self,data):
        new_node = Node(data)        #appends data at the last of the linked list
        curr= self.head
        while curr.next!=None:
            curr=curr.next
        curr.next = new_node
    
    def length(self):
        count=0
        curr=self.head             #traverses the linked list till the last node and finds it's length
        while curr.next!=None:
            count+=1
            curr=curr.next
        return count
    
    def display(self):
        curr=self.head
        while curr.next!=None:
            curr=curr.next                
            print(curr.data, end=" ")   #prints the data of the node
        print()
    
    def features(self):
        l=[]
        curr=self.head
        while curr.next!=None:
            curr=curr.next
            l.append(curr.data)         #this function prints the min and max and their difference
        a=max(l)
        b=min(l)
        c=a-b
        print("max value in the linked list is ",a)
        print("min value in the linked list is ",b)
        print("difference between max and min value is ",c)

    
mylist= LinkedList()
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.display()

mylist.features()


        
