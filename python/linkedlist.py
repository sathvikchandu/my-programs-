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
    
    def erase(self,index):
        if index>=self.length():
            return "Index out of range"
        curr_idx=0
        curr=self.head
        while True:
            lst=curr
            curr= curr.next
            if curr_idx == index:
                lst.next= curr.next
                return 
            curr_idx+=1     


    def insert(self, data, position):
        new_node = Node(data)
        cur_pos = 0
        cur = self.head
        while cur.next != None:
            if cur_pos == position:
                new_node.next = cur.next
                cur.next = new_node
                break
            cur = cur.next
            cur_pos += 1
                


                



mylist= LinkedList()
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.display()
print("my ass")
print()
mylist.insert(7,1)
mylist.display()
    


        
