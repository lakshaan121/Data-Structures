class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        a=list(answerKey)
        count=0
        left=0
        max_len=float('-inf')
        def solve(ch):
            count=0
            left=0
            max_len=float('-inf')
            for right in range(len(a)):
                if a[right]!=ch:
                    count+=1
                while count>k:
                    if a[left]!=ch:
                        count-=1
                    left+=1
                max_len=max(max_len,right-left+1)
            return max_len
        return max(solve('T'),solve('F'))

            
