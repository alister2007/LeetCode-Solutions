from collections import Counter
class Solution:
    def __init__(self):
        self.MAX = 10 ** 6 + 1
    def smallestPalindrome(self, s: str, k: int) -> str:
        count = Counter(s)

        half = [0] * 26
        mid = ""

        for ch, f in count.items():
            half[ord(ch) - ord('a')] = f // 2
            if f & 1:
                mid = ch

        if self.countWays(half) < k:
            return ""

        left = []
        m = sum(half)

        for _ in range(m):
            for c in range(26):
                if half[c] == 0:
                    continue

                half[c] -= 1
                ways = self.countWays(half)

                if ways >= k:
                    left.append(chr(c + ord('a')))
                    break

                k -= ways
                half[c] += 1

        left = "".join(left)
        return left + mid + left[::-1]

    def countWays(self, cnt):
        total = sum(cnt)
        res = 1

        for f in cnt:
            if f == 0:
                continue

            res *= self.nCr(total, f)

            if res >= self.MAX:
                return self.MAX

            total -= f

        return res

    def nCr(self, n, r):
        r = min(r, n - r)
        ans = 1

        for i in range(1, r + 1):
            ans = ans * (n - i + 1) // i

            if ans >= self.MAX:
                return self.MAX

        return ans
        