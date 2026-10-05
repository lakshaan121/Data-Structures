# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        dict1={}
        def make_parent(node,par):
            if not node:
                return
            dict1[node]=par
            make_parent(node.left,node)
            make_parent(node.right,node)
        make_parent(root,None)
        result=[]
        visited=set()
        def f(node,distance):
            if not node or node in visited:
                return
            if distance==k:
                result.append(node.val)
            visited.add(node)
            f(node.left,distance+1)
            f(node.right,distance+1)
            f(dict1[node],distance+1)
        f(target,0)
        return result