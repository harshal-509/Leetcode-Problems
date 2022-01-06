class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr=[0 for i in range(1001)]
        for i in trips:
            for j in range(i[1],i[2]):
                arr[j]+=i[0]
                if(arr[j]>capacity):
                    return 0
        return 1