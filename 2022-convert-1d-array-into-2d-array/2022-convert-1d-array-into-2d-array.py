import numpy as np
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        arr = np.array(original)
        try:
            return (arr.reshape(m,n))
        except:
            return []