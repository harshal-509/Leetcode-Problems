#User function Template for python3
import functools
class Solution:
    def sortBySetBitCount(self, arr, n):
        # Your code goes here
        arr1=[]
        for i in range(n):
            arr1.append([arr[i],bin(arr[i]).count("1")])
        arr1=sorted(arr1,key=lambda x:x[1],reverse=True)
        for i in range(n):
            arr[i]=arr1[i][0]
#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sortBySetBitCount(arr, n)
        print(*arr)

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends