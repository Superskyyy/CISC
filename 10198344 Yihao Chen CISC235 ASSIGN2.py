
#initialize global variables
path = [] #for binary tree SearchPath function
rbPath = [] #for red and black tree SearchPath function
import random

class BinaryTreeVertex: #node class for bst
    def __init__(self,value):
        self.left = None 
        self.right = None
        self.value = value #data

class BinarySearchTree: #binary search tree class
    def __init__(self):
        self.root = None #root 
        
    def insert(self,value): #insert function
        if (self.root == None):
            self.root = BinaryTreeVertex(value) #initialize tree root
        else:#if tree not empty
            self._insert(value,self.root) 

    def _insert(self,value,node): #insertion help 

        if (value < node.value): #if value should be place on left
            if (node.left != None):
                self._insert(value,node.left)
            else:
                node.left = BinaryTreeVertex(value)
        else: #value should be on right
            if (node.right != None):
                self._insert(value,node.right)
            else:
                node.right = BinaryTreeVertex(value)
                
#for testing only delete whole tree
    def deleteTree(self):
        self.root = None

#SearchPath function using global        
    def SearchPath(self,value):
        global path
        if (self.root != None): #if tree exists
            return self._SearchPath(self.root,value) #call help
        else:
            return None
        
    def _SearchPath(self,current,value): #search help
        if (current.value == value):
            path.append(value) #if value is root.value
        #elif value is on the right
        #continue search on right side
        elif current.value < value and current.right != None:
            path.append(current.value) #first put value in path
            #then recursion
            self._SearchPath(current.right,value)
        #else on left: vice versa
        elif current.value > value and current.left != None:
            path.append(current.value)
            
            self._SearchPath(current.left,value)
        if value in path: #if value is in the tree
            return path
        else:
            return "Not in Tree at all" #else return error msg
        
    def Total_Depth(self): #calculate the total depth of tree
        if self.root == None: #if tree not exist return 0
            return 0
        else:
            return self._Total_Depth(self.root,0) #call help function
        
    def _Total_Depth(self,current,depth):#help of depth
        deepcount = depth #counter
        if current.left != None: #if tree has left branch
            deepcount += self._Total_Depth(current.left,depth+1)
        if current.right != None: #if has right branch
            deepcount += self._Total_Depth(current.right,depth+1)
        return deepcount #return total counter


#Below is for red black tree code
count = 0 #global counter for experiement 3

class RB_Vertex: #rb tree node class
    def __init__(self,value):
        self.value = value
        self.color = "Red" #initialize color to red
        self.left = None
        self.right = None
        self.count = 0 #counter for exp3
        
class RB_Tree:
    def __init__(self):
        self.root = None

    def RB_insert(self,val): #same as bst
        if (self.root == None):
           self.root =  RB_Vertex(val)     
        else:
            self.root = self.rec_RB_insert(self.root,val)
            self.root.color = "Black" #color root "Black"

    def rec_RB_insert(self,vertex,val):
        if vertex == None: #if vertex == none then build new tree
            return RB_Vertex(val)
        if val > vertex.value:
            vertex.right = self.rec_RB_insert(vertex.right,val)
            if vertex.color == "Red": # don't have to check for balance at Red  
                return vertex
            else:
                if vertex.right.color == "Red":
                    # if right is Red, check grandchildren
                    if  vertex.right.right!= None and vertex.right.right.color == "Red":
                        return self.RB_right_right_fix(vertex)
                    elif vertex.right.left != None and vertex.right.left.color  == "Red":
                        return self.RB_right_left_fix(vertex)
                    else:
                        return vertex #no problem exist in color
                else:
                    return vertex # right is "Black"
            
        else: # else val is smaller than vertex.value
            #go to left side
            vertex.left = self.rec_RB_insert(vertex.left,val)
            if vertex.color == "Red":
                return vertex
            else:
                 #look at its left subtree 
                 if vertex.left.color == "Red":
                    if vertex.left.left != None and vertex.left.left.color == "Red":
                        return self.RB_left_left_fix(vertex)
                    elif vertex.left.right != None and vertex.left.right.color == "Red":
                        return self.RB_left_right_fix(vertex)
                    else:
                        return vertex #no problem exist in color
                 else:
                    return vertex # right is "Black"

    def RB_right_right_fix(self,current):
        # current's right child is Red, right right also red, need fix
        child = current.right
        sib = current.left
        
        if sib!= None and sib.color == "Red": #make sure sib is not None
            # no rotation, need recolour and return

            child.color = "Black"
            sib.color ="Black"
            current.color = "Red"
            return current
        else: # its black need single rotation
            current.count += 1 # increase count by 1
            current.right = child.left
            child.left = current
            #fix coloring
            child.color = "Black"
            current.color = "Red"
        return child

    def RB_right_left_fix(self,current):
        # right is red and right left also red
        child = current.right
        sib = current.left
        if sib!= None and sib.color == "Red": #same as others
            child.color = "Black"
            sib.color = "Black"
            current.color = "Red"
            return current
        else:
         # Black,  double rotation
            current.count += 1  #increase count by 1
            grandchild = child.left
            child.left= grandchild.right
            current.right = grandchild.left
            grandchild.left = current
            grandchild.right = child
            #color fix
            grandchild.color = "Black"
            current.color = "Red"
            #return root of subtree
            return grandchild
        
    def RB_left_left_fix(self,current): #mirror image
        child = current.left
        sib = current.right
        if sib!= None and sib.color == "Red":
            child.color = "Black"
            sib.color ="Black"
            current.color = "Red"
            return current
        else: #sib color = "Black"
            current.count += 1 #increase count by 1
            current.left = child.right
            child.right = current
            #fix coloring
            child.color = "Black"
            current.color = "Red"
        return child
    
    def RB_left_right_fix(self,current):#mirror image same algorithm
        child = current.left
        sib = current.right
        if sib!= None and sib.color == "Red":
            child.color = "Black"
            sib.color = "Black"
            current.color = "Red"
            return current
        else:
            current.count += 1 #increase count by 1
            grandchild = child.right
            child.right= grandchild.left
            current.left = grandchild.right
            grandchild.right = current
            grandchild.left = child
            #color fix
            grandchild.color = "Black"
            current.color = "Red"
            #return root of subtree
            return grandchild
        
    def Total_Depth(self): #calculate the total depth of tree
        if self.root == None:
            return 0
        else:
            return self._Total_Depth(self.root,0)
        
    def _Total_Depth(self,current,depth): #depth help function
        deepcount = depth
        if current.left != None:
            deepcount += self._Total_Depth(current.left,depth+1)
        if current.right != None:
            deepcount += self._Total_Depth(current.right,depth+1)
        return deepcount
    
    def SearchPath(self,value): #search for the path to a value
        if (self.root != None): #same as bst algorithm. 
            return self.rec_SearchPath(self.root,value)
        else:#root == none
            return None

    def rec_SearchPath(self,current,value):
        
        if (current.value == value): #if the root is wt we looking for
            alist = [] #initial a sublist
            alist.append(value)# first put value into sublist
            if current.color == "Red":
                alist.append("Red") #attach color to a sublist
            else:#current color = black
                alist.append("Black")
            rbPath.append(alist)
        elif current.value < value and current.right != None:#the value is on the right
            alist = []
            alist.append(current.value)
            if current.color == "Red":
                alist.append("Red")
            else:
                alist.append("Black")
            rbPath.append(alist)
            self.rec_SearchPath(current.right,value)

        elif current.value > value and current.left != None:
            #when value is on the left
            alist = [] #same as above

            alist.append(current.value)
            if current.color == "Red":
                alist.append("Red")
            else:
                alist.append("Black")
                
            rbPath.append(alist)# put sub into main
            self.rec_SearchPath(current.left,value)
        else:
            return None
        
#return checking:
        
        for item in rbPath: #check if item is in tree 
            if value in item: #go over sublists
                return rbPath
            
        
        print( "Not In Tree At All!")

#part 3 EXPERIMENT1
        

    def count(self): #cpunt the rotates
        if (self.root == None): #if theres no tree at all
            return 0
        else:
            return self._count(self.root)
    def _count(self,root):
        if root == None:
            return 0
        else:
            #calculate total rotate
            return root.count + self._count(root.left) + self._count(root.right)

# this is experiment 1 code below
def EXP1():
     #initial all nums
    num1 =0
    num2 =0
    num3 =0
    num4 =0
    num5 =0
    for tree in range(0,500): #redo 500 times
        rbtree = RB_Tree() #reinitial tree
        for i in range(1,501): #500insertions
            rbtree.RB_insert(random.randint(1,1000)) #insert random 1-1000 nums
            if i == 100: #when checkpoint at 100
                num1 += rbtree.count() #num1 add count
            if i == 200:
                num2 += rbtree.count()
            if i == 300:
                num3 += rbtree.count()
            if i == 400:
                num4 += rbtree.count()            
            if i == 500:
                num5 += rbtree.count()
    #output subtract last checkpoint and div 500
    print("EXP01: ")
    print(num1/500,(num2-num1)/500,(num3-num2)/500,(num4-num3)/500,(num5-num4)/500)

EXP1() #for test only 

#this is experiment 2 code below for testing
def ratio(list1):
    r1=0 #initial ratio holders
    r2=0
    r3=0
    r4=0
    r5=0
    for item in list1: #for R in all lists
        if item < 0.5:
            r1 += 1
        elif 0.5 <= item < 0.75:
            r2 += 1
        elif 0.75 <=item<= 1.25:
            r3 += 1
        elif 1.25<item<=1.5:
            r4 += 1
        elif item >1.5:
            r5 += 1
    print("list: ",r1/500,r2/500,r3/500,r4/500,r5/500) #calculate ratios

def EXP2():
    rslt1=[] #initialize all 5 lists
    rslt2=[]
    rslt4=[]
    rslt8=[]
    rslt16=[]

    for n in [1000,2000,4000,8000,16000]: # 5 cases,
        print ("EXP02: RUNNING CASE_NUMBER, Please wait few moments: ",n)

        for i in range (1,501): # initialize 500 trees * 2
            bst = BinarySearchTree()
            rbt = RB_Tree()
            for item in range (0,n): #bst insert n nums randomly
                bst.insert(random.randint(1,n))
            for item in range (0,n): #insert into red black tree
                rbt.RB_insert(random.randint(1,n))

            if n == 1000: #case 1000 insertions
                #calculate R and append it to rslt lists.
                rslt1.append(bst.Total_Depth()/rbt.Total_Depth()) 
            elif n == 2000:
                rslt2.append(bst.Total_Depth()/rbt.Total_Depth())
            elif n == 4000:
                rslt4.append(bst.Total_Depth()/rbt.Total_Depth())
            elif n == 8000:
                rslt8.append(bst.Total_Depth()/rbt.Total_Depth())        
            elif n == 16000:
                rslt16.append(bst.Total_Depth()/rbt.Total_Depth())
#output area:
    print("THE ANSWER FOR 1000:")
    ratio(rslt1) #calculate the ratio individually
    print("THE ANSWER FOR 2000:")
    ratio(rslt2)
    print("THE ANSWER FOR 4000:")
    ratio(rslt4)
    print("THE ANSWER FOR 8000:")
    ratio(rslt8)
    print("THE ANSWER FOR 16000:")
    ratio(rslt16)
    
EXP2() #run test
