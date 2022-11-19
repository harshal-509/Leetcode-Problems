class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # def check(C,A,B):
        #     if(A==C or B==C):
        #         return 0
        #     if (A[0] == C[0]): return B[0] == C[0]
        #     if (A[1] == C[1]): return B[1] == C[1]
        #     return (A[0] - C[0])*(A[1] - C[1]) == (C[0] - B[0])*(C[1] - B[1])
        # xmin=float('inf')
        # xmax=0
        # ymin=float('inf')
        # ymax=0
        # d=defaultdict(list)
        # n=len(trees)
        # for i in range(n):
        #     xmin=min(xmin,trees[i][0])
        #     xmax=max(xmax,trees[i][0])
        #     ymin=min(ymin,trees[i][1])
        #     ymax=max(ymax,trees[i][1])
        # for i in range(n):
        #     if(xmin==trees[i][0]):
        #         d['xmin'].append(trees[i])
        #     if(ymin==trees[i][1]):
        #         d['ymin'].append(trees[i])
        #     if(xmax==trees[i][0]):
        #         d['xmax'].append(trees[i])
        #     if(ymax==trees[i][1]):
        #         d['ymax'].append(trees[i])
        # d['xmin'].sort()
        # d['xmax'].sort()
        # d['ymin'].sort(key=lambda x:x[1])
        # d['ymax'].sort(key=lambda x:x[1])
        # ans=[]
        # z=Counter([])
        # for i in range(n):
        #     if(check(trees[i],d['xmin'][0],d['ymin'][0])):
        #         if(z[tuple(trees[i])]==0):
        #             ans.append(trees[i])
        #             z[tuple(trees[i])]=1
        #     if(check(trees[i],d['xmin'][-1],d['ymax'][0])):
        #         if(z[tuple(trees[i])]==0):
        #             ans.append(trees[i])
        #             z[tuple(trees[i])]=1
        #     if(check(trees[i],d['ymax'][-1],d['xmax'][-1])):
        #         if(z[tuple(trees[i])]==0):
        #             ans.append(trees[i])
        #             z[tuple(trees[i])]=1
        #     if(check(trees[i],d['xmax'][0],d['ymin'][-1])):
        #         if(z[tuple(trees[i])]==0):
        #             ans.append(trees[i])
        #             z[tuple(trees[i])]=1
        # for i in d:
        #     for j in d[i]:
        #         if(z[tuple(j)]==0):
        #             ans.append(j)
        #             z[tuple(j)]=1
        # return ans
        def compare_slopes(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            return (y3-y2)*(x2-x1) - (y2-y1)*(x3-x2) 
        upper, lower  = [], []
        for point in sorted(trees):
            while len(lower) >= 2 and compare_slopes(lower[-2], lower[-1], point) < 0: lower.pop()
            while len(upper) >= 2 and compare_slopes(upper[-2], upper[-1], point) > 0: upper.pop()
            lower.append(tuple(point))
            upper.append(tuple(point))   
        return list(set(lower + upper))