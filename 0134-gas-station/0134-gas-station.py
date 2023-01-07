class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        return ((stationResults := list(accumulate(gas[i]-cost[i] for i in range(0, len(gas))))).index(min(stationResults))+1) % len(gas) if sum(cost) <= sum(gas) else -1
