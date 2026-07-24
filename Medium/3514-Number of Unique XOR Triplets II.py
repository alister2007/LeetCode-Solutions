class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = 2048

        poly = [0] * N
        for x in set(nums):
            poly[x] = 1

        self.fwht(poly)

        for i in range(N):
            poly[i] = poly[i] * poly[i] * poly[i]

        self.fwht(poly)

        inv = N
        ans = 0
        for x in poly:
            if x // inv:
                ans += 1

        return ans

    def fwht(self, a):
        n = len(a)
        h = 1
        while h < n:
            for i in range(0, n, h * 2):
                for j in range(i, i + h):
                    x = a[j]
                    y = a[j + h]
                    a[j] = x + y
                    a[j + h] = x - y
            h <<= 1