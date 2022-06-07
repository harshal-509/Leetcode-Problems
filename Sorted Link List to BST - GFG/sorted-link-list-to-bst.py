#User function Template for python3

'''
#LinkedList Node
class LNode:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
#Tree Node        
class TNode:
    def __init__(self, data):
        self.data=data
        self.left = self.right = None
'''
class Solution:
    def sortedListToBST(self, head):
        nodes = []
        while head:
            nodes.append(head.data)
            head = head.next
        
        
        def make_tree(nodes):
            n = len(nodes)
            if n == 0:
                return None
            if n == 1:
                return TNode(nodes[0])
            
            
            root = TNode(nodes[n//2])
            root.left = make_tree(nodes[:n//2])
            root.right = make_tree(nodes[n//2+1:])
            return root
            
        return make_tree(nodes)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3
# Node Class
class LNode:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
class TNode:
    def __init__(self, data):
        self.data=data
        self.left = self.right = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = LNode(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node
        
# prints the elements of linked list
def preOrder(root):
    if root == None:
        return
    
    print(root.data, end=" ")
    preOrder(root.left)
    preOrder(root.right)

if __name__ == '__main__':
    for _ in range(int(input())):
       
        n=int(input())
        
        a = LinkedList() # create a new linked list 'a'.
        #b = LinkedList() # create a new linked list 'b'.
        
        nodes_a = list(map(int, input().strip().split()))
        #nodes_b = list(map(int, input().strip().split()))
        
        for x in nodes_a:
            a.append(x)
        
        ob= Solution()
        root= ob.sortedListToBST(a.head)
        preOrder(root)
        
        print()

# } Driver Code Ends