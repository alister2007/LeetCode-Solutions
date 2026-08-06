class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            product=1
            for digit in str(n):
                product=product*int(digit)
            if product%t==0:
                return n
            n=n+1