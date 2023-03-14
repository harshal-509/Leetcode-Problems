# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def hs(h,par,root,ans,temp):
            if(root==None):
                if(h!=par):
                    ans.append(temp)
                return
            temp+=str(root.val)
            if(root.left==None):
                hs(h,root,root.right,ans,temp)
            elif(root.right==None):
                hs(h,root,root.left,ans,temp)
            else:
                hs(h,root,root.left,ans,temp)
                hs(h,root,root.right,ans,temp)
        ans=[]
        temp=""
        h=root
        if(root.left ==None and root.right==None):
            return root.val
        hs(h,-1,root,ans,temp)
        res=0
        for i in range(0,len(ans)):
            res+=int(ans[i])
        return res