class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self,data):
        self.head=None

    def append(self,data):
        if self.head is None:
            nn= node(data)
            nn.prev=None
            self.head=nn
        else:
            nn=node(data)
            curr= self.head
            while curr:
                curr= curr.next
            nn.prev=curr


