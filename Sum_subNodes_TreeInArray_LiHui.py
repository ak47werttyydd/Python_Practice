def calc_subtree_sum(tree:list[int])->None:
    n=len(tree)//2
    all_children_sum=[0]*n
    parent_idx=n
    node_idx=n-1
    for i,val in enumerate(reversed(tree)): #from right to left of tree. i=0 is the last element of tree
        if val==-1:   #the last -1 and the second last -1 embrace subnodes of the last node. ==> the subnodes between two -1 have the same parent
            parent_idx-=1
        else:
            tree[-i-1]+=all_children_sum[node_idx] #update current node with its all_children_sum
            all_children_sum[parent_idx]+=tree[-i-1] #add the current node to its parent's all_children_sum
            node_idx-=1
def calc_subtree_sum_noAllChildrenSum(tree:list[int])->None:
    n = len(tree) // 2 #n=6
    nodeIdx2arrIdx={}
    node_idx=0
    for i in range(len(tree)):
        if tree[i]!=-1:
            nodeIdx2arrIdx[node_idx]=i
            node_idx+=1
    # node_idx will be  n - 1
    parent_idx = n #n-1 is the last node

    # Traverse the array in reverse to handle each node's subtree sum before its parent
    # i is the reversed index of the tree array, i=0 indices the last element
    for i, val in enumerate(reversed(tree)):
        arr_idx = len(tree) - i - 1  # The actual index in the original tree array
        if val == -1: # a "-1" corresponds to a parent node
            parent_idx -= 1
            if parent_idx == -1: #"-1" is 1 more than node number, when we ecounter the first "-1", we have traversed all nodes.
            #e.g. the correct result is [26,-1,2,11,8,-1,-1,1,7,-1,-1,-1,-1] and the parent_idx is -1 now.
                break
        else:
            tree[nodeIdx2arrIdx[parent_idx]]+=tree[arr_idx]  # Update the current node with its subtree sum

tree=[5, -1, 2, 3, 8, -1, -1, 1, 7, -1, -1, -1,-1]
calc_subtree_sum(tree)
print("with all_children_sum: ",tree) #[26, -1, 2, 11, 8, -1, -1, 1, 7, -1, -1, -1, -1]

tree=[5, -1, 2, 3, 8, -1, -1, 1, 7, -1, -1, -1,-1]
calc_subtree_sum_noAllChildrenSum(tree)
print("without all_children_sum",tree) #[26, -1, 2, 11, 8, -1, -1, 1, 7, -1, -1, -1, -1]

