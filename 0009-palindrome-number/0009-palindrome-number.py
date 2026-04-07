class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        # Example = 121

        original = x 
        rev = 0

        while x > 0:
            digit = x % 10 # 121 % 10 = 1
            rev = rev*10 + digit # 0*10 + 1 = 1
            x //= 10 # remaining 12

        if original == rev: 
            return True

        
        


        

           