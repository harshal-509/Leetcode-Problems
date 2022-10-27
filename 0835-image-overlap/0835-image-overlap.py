class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        counter = defaultdict(lambda:0)
        for i1, row1 in enumerate(img1):
            for j1 , v1 in enumerate(row1):
                if v1:
                    for i2, row2 in enumerate(img2):
                        for j2 , v2 in enumerate(row2):
                            if v2:
                                counter[(i1-i2, j1-j2)] += 1
        return max(counter.values()) if counter else 0