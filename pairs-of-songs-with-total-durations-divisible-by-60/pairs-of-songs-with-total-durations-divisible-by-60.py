class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        needed_dict = dict()
        count = 0
        
        for i in time:
            remainder = i % 60 
            if remainder in needed_dict:
                count += needed_dict[remainder]
            
            needed = (60 - remainder) % 60
            
            if needed in needed_dict:
                needed_dict[needed] += 1
            else:
                needed_dict[needed] = 1
        
        return count