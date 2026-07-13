class Solution(object):
    def sequentialDigits(self, low, high):
        s = "123456789"
        ans = []

        for length in range(2, 10):
            for start in range(10 - length):
                num = int(s[start:start + length])
                if low <= num <= high:
                    ans.append(num)

        return ans


low = int(input("Enter low: "))
high = int(input("Enter high: "))

sol = Solution()
print(sol.sequentialDigits(low, high))
