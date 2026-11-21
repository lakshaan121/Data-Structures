class Solution:
    def assignUmbrella(self, rain: list[int]) -> list[str]:
        alice=0
        bob=0
        i=0
        nums=["-1"]*len(rain)
        while i<len(rain):
            if (i+1)<len(rain):
                if rain[i]==1 and rain[i+1]==1:
                    if alice<bob:
                        alice+=1
                        nums[i]="Alice"
                    elif alice==bob:
                        alice+=1
                        nums[i]="Alice"
                    elif bob<alice:
                        nums[i]="Bob"
                        bob+=1
                elif rain[i]==1:
                    nums[i]="Bob"
                    bob+=1
                else:
                    nums[i]="None"
            elif i==len(rain)-1:
                if rain[i]==1:
                    nums[i]="Bob"
                else:
                    nums[i]="None"
            i+=1
        return nums
                        
        