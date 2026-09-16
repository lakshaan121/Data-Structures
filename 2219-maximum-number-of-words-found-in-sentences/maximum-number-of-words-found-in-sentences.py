class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_len=0
        for i in sentences:
            list1=i.split(' ')
            max_len=max(max_len,len(list1))
        return max_len