class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        sumOdd= n*n
        sumEven= n*(n+1)
        
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        return gcd(sumOdd,sumEven)