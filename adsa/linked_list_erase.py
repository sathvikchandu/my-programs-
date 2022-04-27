class Node:
    def __init__(self,data=None,next=None): #initializes the data and next of the node
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self,data=None):
        self.head = Node()      #initializes the head of the linked list

    def append(self,data):
        new_node = Node(data)
        curr= self.head
        while curr.next!=None:  #traverses the linked list till the last node
            curr=curr.next
        curr.next = new_node       #assigns the new node to the last node
    
    def length(self):
        count=0
        curr=self.head       
        while curr.next!=None:
            count+=1               #increments the position until the last node
            curr=curr.next
        return count       #returns the length
    
    def display(self):
        curr=self.head
        while curr.next!=None:
            curr=curr.next
            print(curr.data, end=" ") #prints the data of the node
        print()
    
    def erase(self,index):
        if index>=self.length():
            return "Index out of range"
        curr_idx=0
        curr=self.head
        while True:
            lst=curr
            curr= curr.next
            if curr_idx == index:       #if the index is found
                lst.next= curr.next       #assigns the next node to the current node
                return "erased successfully"
            curr_idx+=1     


    def insert(self, data, position):
        new_node = Node(data)
        cur_pos = 0
        cur = self.head
        while cur.next != None: 
            if cur_pos == position:       #if the index is found
                new_node.next = cur.next
                cur.next = new_node
                break
            cur = cur.next
            cur_pos += 1

    def erase_at_end(self):
        if self.length()<1:
            return "List is empty"
        curr=self.head

        while curr.next!=None:
            lst=curr
            curr= curr.next               #traverses the linked list till the last node
        lst.next=None
        return "erased at the end successfully"
    
    def erase_at_beginning(self):
        if self.length()<1:
            return "List is empty"
        self.head=self.head.next        #assigns the next node to the head
        return "erased at the beginning successfully"

    


mylist= LinkedList()
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.display()

mylist.insert(7,1)
mylist.append(4)
mylist.append(5)
mylist.erase_at_end()
mylist.erase_at_beginning()
mylist.display()
    


        
