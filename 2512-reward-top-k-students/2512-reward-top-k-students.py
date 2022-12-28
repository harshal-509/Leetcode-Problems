class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        z=Counter(positive_feedback)
        z1=Counter(negative_feedback)
        n=len(report)
        ans=Counter([])
        for i in range(n):
            ans[student_id[i]]=0
            for j in report[i].split(' '):
                if(z[j]):
                    ans[student_id[i]]+=3
                if(z1[j]):
                    ans[student_id[i]]-=1
        t=ans.most_common(n)
        t.sort()
        t.sort(key=lambda x:x[1],reverse=True)
        ans=[]
        for i in t:
            ans.append(i[0])
        return ans[:k]