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
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None 
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
    
    def addafter(self,key,data):
        cur=self.head
        while cur:
            if cur.next is None and cur.data==key:
                self.append(data)
                return
            elif cur.data==key:
                new_node= Node(data)
                nxt=cur.next
                cur.next=new_node
                new_node.next=nxt
                new_node.prev=cur
                nxt.prev=new_node
            cur=cur.next
    
    def addbefore(self,key,data):
        cur=self.head
        while cur:
            if cur.prev is None and cur.data==key:
                self.prepend(data)
                return
            elif cur.data==key:
                new_node=Node(data)
                prev= cur.prev
                prev.next= new_node
                cur.prev= new_node
                new_node.next= cur
                new_node.prev= prev


            cur=cur.next
        
    def delete(self,key):
        cur=self.head
        while cur:
            if cur.data==key and cur==self.head:
                if not cur.next:
                    cur=None
                    self.head=None
                    return
                else:
                    nxt=cur.next
                    cur.next= None
                    nxt.prev=None

                    cur=None
                    self.head=nxt
                    return
            
            elif cur.data==key:
                if cur.next:
                    nxt= cur.next
                    prev= cur.prev
                    prev.next=nxt
                    nxt.prev=prev
                    cur.next=None
                    cur.prev=None
                    cur=None
                    return
                else:
                    prev=cur.prev
                    prev.next=None
                    cur.prev=None
                    cur=None
                    return
            cur=cur.next
    
    def reverse(self):
        tmp = None
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        if tmp:
            self.head = tmp.prev

    def deletenode(self,node):
        cur=self.head
        while cur:
            if cur==node and cur==self.head:
                if not cur.next:
                    cur=None
                    self.head=None
                    return
                else:
                    nxt=cur.next
                    cur.next= None
                    nxt.prev=None

                    cur=None
                    self.head=nxt
                    return
            
            elif cur==node:
                if cur.next:
                    nxt= cur.next
                    prev= cur.prev
                    prev.next=nxt
                    nxt.prev=prev
                    cur.next=None
                    cur.prev=None
                    cur=None
                    return
                else:
                    prev=cur.prev
                    prev.next=None
                    cur.prev=None
                    cur=None
                    return
            cur=cur.next


    def remduplicates(self):
        seen={}
        cur = self.head
        if cur.data not in seen:
            seen[cur.data]=1
            cur = cur.next
        else:
            nxt = cur.next
            self.deletenode(cur)
            cur=nxt


    






dllist = DoublyLinkedList()
dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)

dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)


dllist.addafter(1,9)
dllist.addbefore(4,10)
dllist.delete(2)
dllist.remduplicates()



dllist.reverse()
dllist.print_list()