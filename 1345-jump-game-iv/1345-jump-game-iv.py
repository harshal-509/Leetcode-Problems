class Solution(object):
    def minJumps(self, arr):
        if len(arr) == 1: return 0
        adj = defaultdict(list)
        for i, n in enumerate(arr):
            adj[n].append(i)
        ans = [0] * len(arr)
        dq = deque([len(arr) - 1])
        while dq:
            i = dq.popleft()
            if i < len(arr) - 1 and ans[i + 1] == 0 and i + 1 < len(arr) - 1:
                ans[i + 1] = ans[i] + 1
                dq.append(i + 1)
            if i > 0 and ans[i - 1] == 0:
                ans[i - 1] = ans[i] + 1
                if i - 1 == 0: return ans[0]
                dq.append(i - 1)
            for j in adj[arr[i]]:
                if ans[j] == 0 and j < len(arr) - 1:
                    ans[j] = ans[i] + 1
                    if j == 0: return ans[0]
                    dq.append(j)