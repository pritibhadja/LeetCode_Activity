# Time Complexity - o(nlogn)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n % 2 == 0: # Even number
            n //= 2 # Divisible by 2
        
        return n == 1
       

        