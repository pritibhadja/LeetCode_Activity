class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        size = len(nums)
        neg = []
        pos = []

        #seprate two arrays
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)

        # case:1 if neg array is empty
        if len(neg) == 0:
            return [ x * x for x in pos ]

        # case:2 if pos array is empty
        if len(pos) == 0:
            res = [ x * x for x in neg ]
            res.reverse()
            return res

        # case:3 if both exist
        neg = [ x * x for x in neg][::-1] # square, reverse
        pos = [ x * x for x in pos] # square

        i = j = 0
        n = len(neg)
        m = len(pos)
        res = []

        while i < n and j < m:
            if neg[i] <= pos[j]:
                res.append(neg[i])
                i += 1

            else:
                res.append(pos[j])
                j += 1

        #jo neg/pos khali thai jai to

        while i<n:
            res.append(neg[i]) 
            i += 1 

        while j<m:
            res.append(pos[j])
            j += 1

        return res