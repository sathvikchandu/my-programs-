class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self,data=None):
        self.head = Node()

    def append(self,data):          #appends data at the last of the linked list
        new_node = Node(data)
        curr= self.head            
        while curr.next!=None:   #traverses the linked list till the last node
            curr=curr.next
        curr.next = new_node      #assigns the new node to the last node
    
    def length(self):
        count=0
        curr=self.head
        while curr.next!=None: #traverses the linked list till the last node
            count+=1
            curr=curr.next
        return count            #returns the length of the linked list
    
    def display(self):
        curr=self.head
        while curr.next!=None: #traverses the linked list till the last node
            curr=curr.next
            print(curr.data, end=" ") #prints the data of the node
        print()
    
       


    def insert(self, data, position):
        new_node = Node(data)
        cur_pos = 0
        cur = self.head         
        while cur.next != None: #traverses the linked list till the last node
            if cur_pos == position:
                new_node.next = cur.next #assigns the new node to the last node
                cur.next = new_node
                break
            cur = cur.next 
            cur_pos += 1   #increments the position   
                


                



mylist= LinkedList() #creates an object of the class LinkedList
mylist.append(1)      #appends 1 at the last of the linked list
mylist.append(2)
mylist.append(3)
mylist.display()


mylist.insert(7,1)
mylist.display()  #displays the linked list.
    


        
