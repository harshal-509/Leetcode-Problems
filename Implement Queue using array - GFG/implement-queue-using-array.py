#User function Template for python3

class MyQueue:
    
    #Function to push an element x in a queue.
    def __init__(self):
        self.arr=[-1]*(100001)
        self.rear=-1
        self.front=-1
    def push(self, x):
         
         #add code here
        if(self.rear==-1 and self.front==-1):
            self.rear+=1
            self.front+=1
            self.arr[self.rear]=x
        else:
            self.rear+=1
            self.arr[self.rear]=x
    #Function to pop an element from queue and return that element.
    def pop(self): 
        if(self.front>self.rear):
            return -1
        d=self.arr[self.front]
        self.front+=1
        return d
         # add code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   

# } Driver Code Ends