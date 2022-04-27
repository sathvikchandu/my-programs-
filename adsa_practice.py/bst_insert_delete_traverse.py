class Bst: 
  
    def __init__(node, value): 
        node.value = value  
        node.left_side = None
        node.right_side = None
    
    def in_order( node, root ): 
        if( root is None ): 
            return
        node.in_order(root.left_side) 
        print(root.value,end = ' ') 
        node.in_order(root.right_side) 

    def pre_order(node,root):
 
        if(root is None):
            return 
        print(root.value,end=" ")

        node.pre_order(root.left_side)
        node.pre_order(root.right_side)
  
    def insert_node(node, value): 
        if node is None: 
            node = Bst(value)
        elif value < node.value:
            if node.left_side is None:
                node.left_side = Bst(value)
            else:
               node.left_side.insert_node(value) 
        else:
            if node.right_side is None:
                node.right_side = Bst(value)
            else:
                node.right_side.insert_node(value)

    def delete_node(node,temp, value): 
        if value < node.value:
            temp = node
            node.left_side.delete_node(temp,value)
        elif(value > node.value):
            temp = node
            node.right_side.delete_node(temp, value)
            
        else:
            if (node.left_side is None and node.right_side is None):
                if(temp.left_side == node):
                    temp.left_side = None
                else:
                    temp.right_side = None
                node = None
        
            elif node.right_side is None :
                if(temp.left_side == node):
                    temp.left_side = node.left_side
                else:
                    temp.right_side = node.left_side
                node = None
    
            elif node.left_side is None :
                if(temp.left_side == node):
                    temp.left_side = node.right_side
                else:
                    temp.right_side = node.right_side
                node = None
                
            else:
                temp = node.right_side
                while(temp.left_side is not None):
                    temp = temp.left_side 
                node.value = temp.value
                node.right_side.delete_node(temp,temp.value)   
root = Bst(9) 
root.insert_node(5) 
root.insert_node(3) 
root.insert_node(8) 
root.insert_node(2) 
root.insert_node(43) 
root.insert_node(21) 
  
print ("pre-order traversal is ",end = '')
root.pre_order(root) 

root.delete_node(root, 21) 
print ('\n 21 removed: ',end ='')
root.in_order(root) 
  
root.delete_node(root, 5) 
print ('\n 5 removed: ',end ='')
root.in_order(root) 
  

