class Solution:
    def letterCombinations(self, digits: str) -> List[str]:



        dict1 = {
        '2': ['a','b','c'],
        '3': ['d','e','f'],
        '4': ['g','h','i'],
        '5': ['j','k','l'],
        '6': ['m','n','o'],
        '7': ['p','q','r','s'],
        '8': ['t','u','v'],
        '9': ['w','x','y','z'],
        '0': [' ']}
        old1=[""]
        list1=[]
        for i in digits:
            temp=[]
            for old in old1:
                for letter in dict1[i]:
                    temp.append(old+letter)
            old1=temp
        return temp


                 
            



        



