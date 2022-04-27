class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data) #initializes the head of the linked list
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next #assigns the new node to the last node
            cur.next = new_node
            new_node.prev = cur #joins the created node link to the last node
            new_node.next = None 

   

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")  #prints the data of the node
            cur = cur.next
        
    def reverse_dll(self):
        l=[]
        curr=self.head
        while curr:
            l.append(curr.data)
            curr=curr.next 
        for i in l[::-1]:     #reverses the list
            print(i,end=" ")  #prints the data of the node
        print()
    
   
        
    
    
  

    
dllist = DoublyLinkedList()
n= int(input("Enter the numbers you want to append in doubly linked list using spaced integers: "))
l=list(map(int,input().split()))
for i in l:
    dllist.append(i)
dllist.print_list()
print()
print("The reversed doubly linked list is: ")
dllist.reverse_dll()