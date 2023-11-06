from sortedcontainers import SortedList
class SeatManager:
    def __init__(self, n: int):
        self.seats=SortedList([0])
        self.n=n
    def reserve(self) -> int:
        def findFirstMissing(array, start, end): 
            if (start > end): 
                return end + 1
            if (start != array[start]): 
                return start; 
            mid = int((start + end) / 2) 
            if (array[mid] == mid): 
                return findFirstMissing(array,mid+1, end) 
            return findFirstMissing(array,start, mid) 
        x=findFirstMissing(self.seats,0,len(self.seats)-1)
        self.seats.add(x)
        return x
    def unreserve(self, seatNumber: int) -> None:
        self.seats.discard(seatNumber)
                

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)