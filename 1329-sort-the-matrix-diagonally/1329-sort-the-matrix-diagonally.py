class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n=len(mat)
        m=len(mat[0])
        j=0
        i=n-1
        while(i>=0):
            ans=[mat[i][j]]
            k=i
            o=j
            while(1):
                if(k+1<n and o+1<m):
                    ans.append(mat[k+1][o+1])
                    k+=1
                    o+=1
                else:
                    break
            k=i
            o=j
            ans.sort()
            p=0
            while(1):
                if(k<n and o<m):
                    mat[k][o]=ans[p]
                    k+=1
                    o+=1
                    p+=1
                else:
                    break
            i-=1
        j=0
        i=0
        while(j<m):
            ans=[mat[i][j]]
            k=i
            o=j
            while(1):
                if(k+1<n and o+1<m):
                    ans.append(mat[k+1][o+1])
                    k+=1
                    o+=1
                else:
                    break
            k=i
            o=j
            ans.sort()
            p=0
            while(1):
                if(k<n and o<m):
                    mat[k][o]=ans[p]
                    k+=1
                    o+=1
                    p+=1
                else:
                    break
            j+=1
        return mat