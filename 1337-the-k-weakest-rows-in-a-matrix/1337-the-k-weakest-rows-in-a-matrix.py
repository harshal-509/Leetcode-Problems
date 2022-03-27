class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        freq = {}
        row = 0
        for arr in mat:
            soldiers = 0
            for i in arr:
                if i == 1:
                    soldiers += 1
            freq[row] = soldiers
            row += 1
        freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1])}
        res = []
        for i in freq:
            # print(i)
            res.append(i)
        return res[0:k]