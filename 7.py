# 7.
class Solution:
    def maxScore(self, cardPoints:List[int],k:int)->:
        sum_left, sum_right=sum(cardPoints[:k]), 0
        res=sum_left
        for i in range(k):
            sum_lefy-=cardPoints[k-1-i]
            sum_right+=cardPoints[len(cardPoints)-1-i]
            res=max(res,sum_left+sum_right)
        return res
