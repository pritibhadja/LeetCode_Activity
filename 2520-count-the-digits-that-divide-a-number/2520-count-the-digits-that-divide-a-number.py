class Solution:
    def countDigits(self, num: int) -> int:
        #take example 121
        temp = num # temp = 121
        ans = 0  # start from 1
        while temp>0:  
            reminder = temp % 10 # if 121 % 10 reminder=1
            if num % reminder==0:  # if 121 divided by 1
                ans+=1
            temp//=10 # Next number become 12 and loop continued

        return ans