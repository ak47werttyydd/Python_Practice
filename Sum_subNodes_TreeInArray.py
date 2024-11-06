# 一棵树，存储在N+N+1大小的数组中，N个节点各自存储的值均大于等于零，且逐层并以从左到右的顺序存储在数组中比如根节点（第一个节点）存了5，第二个节点存2，第三个节点存8，第四个节点存4。 N+1 个-1是分隔符，用于指示节点的父子关系，比如夹在第一个-1和第二个-1 之间的节点都是第一个节点（根节点）的子节点，以此类推第i个-1和第i+1个-1之间的节点都是第i个节点的子节点。如果第i个-1和第i+1个-1之间没有节点，说明第i个节点是叶子节点
# import sys
from collections import defaultdict
arr =[5, -1, 2, 3, 8, -1, -1, 1, 7, -1, -1, -1,-1]
m1_p=[position for position,value in enumerate(arr) if value == -1] # -1's position
nodeIdx=0  #node index w.r.t pure nodes with values (disregarding -1)
arrIdx_nodeIdx_map=defaultdict(int)
for arrIdx,node in enumerate(arr):
    if node!=-1:
        arrIdx_nodeIdx_map[arrIdx]=nodeIdx
        nodeIdx+=1
#if nodeIdx have subnodes:  [ m1_p[nodeIdx]+1 , m1_p[nodeIdx+1]-1 ] is the range(arrIdices) of subnodes
#have no subnode: m1_p[nodeIdx]+1==m1_p[nodeIdx+1]

#recursion to get the sum of cur_node and its subnodes
result=[-1]*len(arr) #result[i] is the sum of node i and its all subnodes
def get_sum(arrIdx)->int:
    #pre
    if result[arrIdx]!=-1: #current node has calculated
        return result[arrIdx] #return current node's sum

    #if no subnodes （leaf nodes）
    if m1_p[arrIdx_nodeIdx_map[arrIdx]]+1==m1_p[arrIdx_nodeIdx_map[arrIdx]+1]:
        result[arrIdx]=arr[arrIdx]
        return arr[arrIdx]

    subsum = 0
    #in  #scanning subnodes
    for sub_arrIdx in range(m1_p[arrIdx_nodeIdx_map[arrIdx]]+1,m1_p[arrIdx_nodeIdx_map[arrIdx]+1],1):
        subsum+=get_sum(sub_arrIdx)

    #post
    result[arrIdx]=arr[arrIdx]+subsum
    return result[arrIdx]
get_sum(0)
print(result)
