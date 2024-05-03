class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        temp = version1.split('.')
        temp1 = version2.split('.')
        
        n=max(len(temp),len(temp1))
        
        for i in range(len(temp),n):
            temp.append(0)
            
        for i in range(len(temp1),n):
            temp1.append(0)

        for i in range(n):
            if(int(temp[i])<int(temp1[i])):
                return -1
            if(int(temp[i])>int(temp1[i])):
                return 1
        return 0