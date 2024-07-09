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
def main():
    solution=Solution()
    cardPoints=[1,2,3,4,5,6,1]
    k=3
    result=solution.maxScore(cardPoints,k)
    print(f"Maximum score: {result}")
    
if _name_=="_main_":
    main()
