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
            new_node = Node(data)
            new_node.prev = None        #initializes the head of the linked list
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node          #assigns the new node to the last node
            new_node.prev = cur         #joins the created node link to the last node
            new_node.next = None 

   

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")   #prints the data of the node
            cur = cur.next
    
   
        
    
    
  

    
dllist = DoublyLinkedList()
n= int(input("Enter the numbers you want to append in doubly linked list using spaced integers: "))
l=list(map(int,input().split()))
for i in l:
    dllist.append(i)
dllist.print_list()