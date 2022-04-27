class Bst_Node:
    def __init__(self, key):
        self.left_side = None
        self.right_side = None
        self.value = key
 
 

def in_order(root):
 
    if root:
 
        
        in_order(root.left_side)
 
        
        print(root.value),
 
       
        in_order(root.right_side)
 

 
root = Bst_Node(1)
root.left_side = Bst_Node(2)
root.right_side = Bst_Node(3)
root.left_side.left_side = Bst_Node(4)
root.left_side.right_side = Bst_Node(5)

 
print ("in_order traversal is")
in_order(root)
 
