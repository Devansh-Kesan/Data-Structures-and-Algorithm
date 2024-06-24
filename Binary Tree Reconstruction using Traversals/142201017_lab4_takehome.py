class Treenode:
    def __init__(self,val,left=None,right=None):
        self.parent=None
        self.val=val
        self.left=left
        self.right=right
        self.depth=0

    def make_leftchild(self,lchild):
        lchild.parent=self
        self.left=lchild

    def make_rightchild(self,rchild):
        rchild.parent=self
        self.right=rchild

def build_tree_using_preorder_and_inorder(preorder,inorder,depth=0):
    if len(preorder)==0:
        return None

    root=preorder[0]
    root_node=Treenode(root)
    root_node.depth=depth

    ind_root_inorder=inorder.index(root)

    if ind_root_inorder!=0:
        new_left_preorder=preorder[1:1+ind_root_inorder]
        new_left_inorder=inorder[:ind_root_inorder]

        left_subroot=build_tree_using_preorder_and_inorder(new_left_preorder,new_left_inorder,depth + 1)
        root_node.make_leftchild(left_subroot)

    if ind_root_inorder!=len(preorder)-1:
        new_right_preorder=preorder[1+ind_root_inorder:]
        new_right_inorder=inorder[ind_root_inorder+1:]

        right_subroot=build_tree_using_preorder_and_inorder(new_right_preorder,new_right_inorder,depth + 1)
        root_node.make_rightchild(right_subroot)

    return root_node

def build_tree_using_postorder_and_inorder(postorder,inorder,depth=0):
    if len(postorder)==0:
        return None

    root=postorder[-1]
    root_node=Treenode(root)
    root_node.depth=depth

    ind_root_inorder=inorder.index(root)

    if ind_root_inorder!=0:
        new_left_postorder=postorder[:ind_root_inorder]
        new_left_inorder=inorder[:ind_root_inorder]

        left_subroot=build_tree_using_postorder_and_inorder(new_left_postorder,new_left_inorder,depth + 1)
        root_node.make_leftchild(left_subroot)

    if ind_root_inorder!=len(postorder)-1:
        new_right_postorder=postorder[ind_root_inorder:-1]
        new_right_inorder=inorder[ind_root_inorder+1:]

        right_subroot=build_tree_using_postorder_and_inorder(new_right_postorder,new_right_inorder,depth + 1)
        root_node.make_rightchild(right_subroot)

    return root_node

def build_tree_using_preorder_and_postorder(preorder,postorder,depth=0):
    if len(preorder)==0:
        return None

    root=preorder[0]
    root_node=Treenode(root)
    root_node.depth=depth

    if root != postorder[-1]:
        raise ValueError

    ind_left_root_postorder=postorder.index(preorder[1])

    if ind_left_root_postorder == 0:
        left = Treenode(postorder[0])
        root_node.make_leftchild(left)
        left.depth = 1 + root_node.depth
    else:
        new_left_preorder=preorder[1:1+ind_left_root_postorder+1]
        new_left_postorder=postorder[:ind_left_root_postorder+1]

        left_subroot=build_tree_using_preorder_and_postorder(new_left_preorder,new_left_postorder,depth + 1)
        root_node.make_leftchild(left_subroot)

    if ind_left_root_postorder == len(preorder)-1-2:
        right = Treenode(preorder[-1])
        root_node.make_rightchild(right)
        right.depth = 1 + root_node.depth

    else:
        new_right_preorder=preorder[1+ind_left_root_postorder+1:]
        new_right_postorder=postorder[ind_left_root_postorder+1:-1]

        right_subroot=build_tree_using_preorder_and_postorder(new_right_preorder,new_right_postorder,depth + 1)
        root_node.make_rightchild(right_subroot)

    return root_node

def print_tree(preorder1_or_postorder1,inorder1_or_postorder1):
    
    traversal1 = preorder1_or_postorder1[2:]
    traversal2 = inorder1_or_postorder1[2:]

    pos=["root"]
    depth=[0]

    def preorder_traversal(root):
        tab="   "
        if root is None:
            return None
        l=[]

        l.append(root.val)

        if root.left:
            pos.append("left")
            depth.append(root.left.depth)
            l=l+preorder_traversal(root.left)
            
        if root.right:
            pos.append("right")
            depth.append(root.right.depth)
            l=l+preorder_traversal(root.right)
            
        return l

    try:
        if preorder1_or_postorder1[0] == "preorder" and inorder1_or_postorder1[0] == "inorder":
            root = build_tree_using_preorder_and_inorder(traversal1,traversal2)
        elif preorder1_or_postorder1[0] == "postorder" and inorder1_or_postorder1[0] == "inorder":
            root = build_tree_using_postorder_and_inorder(traversal1,traversal2)
        elif preorder1_or_postorder1[0] == "preorder" and inorder1_or_postorder1[0] == "postorder":
            root = build_tree_using_preorder_and_postorder(traversal1,traversal2)
    except ValueError as err:
        print("error : Tree cannot be constructed using these two traversals") 
        return

    l=preorder_traversal(root)
    space="     "
    ind=0
    for i in zip(pos,l):
        print(depth[ind]*space+str(i))
        ind+=1

#input format
# you can't give both traversals as same traversal
# you have to give the type of traversal as mentioned in the variable name

preorder_or_postorder=input().split()       # give any one of it
inorder_or_postorder=input().split()        # give any one of it but different from above one
print_tree(preorder_or_postorder,inorder_or_postorder)



