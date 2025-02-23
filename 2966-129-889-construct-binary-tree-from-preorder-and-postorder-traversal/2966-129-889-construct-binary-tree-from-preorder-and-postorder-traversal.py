# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def solve(root,flag):
            # print(root,flag)
            if(len(root)==0):
                return None
            if(flag==0):
                z=root[0]
            else:
                z=root[-1]
            l = []
            l1 = []
            x=-1
            y=-1
            for i in range(len(preorder)):
                if(preorder[i]==z):
                    x=i
                    break
            for i in range(len(postorder)):
                if(postorder[i]==z):
                    y=i
                    break
            # print(x,y)
            for i in preorder:
                if(i in preorder[x+1:] and i in postorder[:y]):
                    l.append(i)
            for i in postorder:
                if(i in preorder[x+1:] and i in postorder[:y]):
                    l1.append(i)
            if(flag==0):
                ans=TreeNode(z)
            else:
                ans=TreeNode(z)
            if(l and l1[-1] and l[0]!=l1[-1]):
                ans.right = solve(l1,1)
            ans.left = solve(l,0)
            return ans
        return solve(preorder,0)