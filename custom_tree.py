import networkx as nx
import pygraphviz as pgv
from nxpd import draw, nxpdParams
import matplotlib.pyplot as plt
nxpdParams['show'] = 'ipynb'
import matplotlib.pyplot as plt
 
# Get current size
fig_size = plt.rcParams["figure.figsize"]
 
# Prints: [8.0, 6.0]
print ("Current size:", fig_size)
 
# Set figure width to 12 and height to 9
fig_size[0] = 12
fig_size[1] = 9
plt.rcParams["figure.figsize"] = fig_size


class Tree():
    
    def __init__(self, arr):
        self.length=len(arr)
        self.root=Node(arr[0])        
        for i in range(1,self.length):
            self.insert(arr[i])
    
    def insert(self, ele):
        curr_node=self.root
        node=Node(ele)
        inserted=1
        while inserted:
            if ele>=curr_node.data:                
                if curr_node.right==None:
                    curr_node.right=node 
                    node.parent=curr_node
                    inserted=0
                else:
                    curr_node=curr_node.right
            else:                
                if curr_node.left==None:
                    curr_node.left=node
                    node.parent=curr_node
                    inserted=0
                else:
                    curr_node=curr_node.left
                    
    def find(self, ele, root=0 ):
        if root==0:
            root=self.root
        if root==None:
            return False
        if root.data==ele:
            return root
        else:
            return self.find(ele, root=root.left) or self.find(ele, root.right)
    
    def plot(self):
        def sub(c, dic):
            if dic.get(c)==None:
                dic[c]=1
                return str(c)
            else:
                dic[c]=dic[c]+1
                return str(c)+'_'+str(dic[c])
        print('function invoked')
        graph=nx.Graph()
        nodes=[self.root]
        for node in nodes:      
            graph.add_node(node.data)
            if node.parent!=None:
                graph.add_edge(node.parent.data, node.data)
            if node.left!=None:
                nodes.append(node.left)
            if node.right!=None:
                nodes.append(node.right)
                    
        draw(graph,'ada.png')
        
    def inorder(self, root=0):
        if root==0:
            root=self.root
            
            
            
        if root!=None:
           
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
            
        
        
    def __str__(self):
        return "Tree object with Root Node : "+str(self.root)
        
        
    def tree_max(self, root=0, return_node=False):
        if root==0:
            root=self.root   
        maxi=root.data
        while root.right is not None:
            root=root.right
            maxi=root.data
            
        if return_node:
            return root
        else:    
            return maxi
        
    def tree_min(self, root=0, return_node=False):
        if root==0:
            root=self.root   
        maxi=root.data
        while root.right is not None:
            root=root.left
            maxi=root.data
            
        if return_node:
            return root
        else:    
            return maxi
    
    def delete(self, ele):
        node=self.find(ele)
        print(node)
        if node==False:
            print('not found')
        if node.left==None and node.right==None:
            node.data=None

        elif node.left==None:
            node.data=node.right.data
            node.right.data=None
      
        elif node.right==None:
            node.data=node.left.data
            node.left.data=None
        else:

            
            
            ino_suc=self.tree_min(node.right, return_node=True)
            temp=ino_suc.data
            self.delete(ino_suc.data)
            node.data=temp
        
        
            
        
        
        
    
        
        

class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
        self.parent=None
        

        
    