class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dirs = [d for d in path.split('/') if d]
        
        for d in dirs:
            
            if d == ".":
                continue
            
            elif d != "..":
                stack.append(d)
                continue
             
            if(len(stack) > 0):
                stack.pop()
        
        return "/"+"/".join(stack)