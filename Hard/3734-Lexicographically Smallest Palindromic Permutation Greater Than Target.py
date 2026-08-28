class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n = len(s)

        # Count characters.
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # A palindrome can have at most one character
        # with an odd frequency.
        odd = 0
        middle = ''

        for i in range(26):
            if cnt[i] % 2:
                odd += 1
                middle = chr(ord('a') + i)

        if odd > 1:
            return ""

        # Number of characters in the left half.
        half_len = n // 2

        # half_cnt[c] = how many copies of character c
        # are available in the left half.
        half_cnt = [x // 2 for x in cnt]

        prefix = []

        def build_max_palindrome():
            """
            Given the current prefix, fill the remaining
            left half with the largest possible characters.
            This produces the lexicographically largest
            palindrome having the current prefix.
            """
            left = prefix[:]

            for c in range(25, -1, -1):
                left.extend(
                    [chr(ord('a') + c)] * half_cnt[c]
                )

            left = ''.join(left)

            if n % 2:
                return left + middle + left[::-1]
            else:
                return left + left[::-1]

        # Greedily construct the left half.
        for _ in range(half_len):
            chosen = False

            # Try the smallest available character first.
            for c in range(26):
                if half_cnt[c] == 0:
                    continue

                ch = chr(ord('a') + c)

                # Temporarily use this character.
                half_cnt[c] -= 1
                prefix.append(ch)

                # If the maximum possible completion is still
                # <= target, this choice can never work.
                if build_max_palindrome() > target:
                    chosen = True
                    break

                # Undo the choice.
                prefix.pop()
                half_cnt[c] += 1

            if not chosen:
                return ""

        # Construct the final palindrome.
        left = ''.join(prefix)

        if n % 2:
            ans = left + middle + left[::-1]
        else:
            ans = left + left[::-1]

        return ans if ans > target else ""