class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats=0
        n=len(people)
        j=n-1
        i=0
        people.sort()
        while(i<j):
            if(people[j]+people[i]<=limit):
                boats+=1
                i+=1
                j-=1
            else:
                boats+=1
                j-=1
        if(i==j):
            boats+=1
        return boats