# 7.
from typing import List
class Solution:
    def maxScore(self,cp: List[int], k: int)->int:
        tot_sum,subArrSum=sum(cp),sum(cp[:-k])
        ans=tot_sum-subArrSum
        for i in range(k):
            subArrSum=subArrSum+cp[len(cp)-k+1]-cp[i]
            ans=max(ans,tot_sum-subArrSum)
        return ans
    
if _name_=="_main_":
    solution:Solution()
    cp=[1,2,3,4,5,6,1]
    k=3
    print(solution.maxScore(cp,k))
