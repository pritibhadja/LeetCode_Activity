#Time complexity- 2^n
class Solution:
    def fib(self, n: int) -> int:

        # base case
        if n==0 or n==1:
            return n

        # Recursive case
        else:
            return self.fib(n-1) + self.fib(n-2)