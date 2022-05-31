class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def sorted(self, s):
        # Code here
        def insertatcorrect(s,temp):
            if(not(s)):
                s.append(temp)
                return
            if(temp>s[-1]):
                s.append(temp)
                return
            p=s.pop()
            insertatcorrect(s,temp)
            s.append(p)
        def solve(s):
            if(not(s)):
                return
            temp=s.pop()
            solve(s)
            insertatcorrect(s,temp)
        solve(s)

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends