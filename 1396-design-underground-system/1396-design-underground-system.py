class UndergroundSystem:

    def __init__(self):
        self.d=defaultdict(list)
        self.h={}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.h[id]=(stationName,t)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        x=self.h[id]
        self.d[(x[0],stationName)].append(t-x[1])
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        ans=0
        t=0
        for i in self.d[(startStation,endStation)]:
            ans+=i
            t+=1
        return ans/t


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)