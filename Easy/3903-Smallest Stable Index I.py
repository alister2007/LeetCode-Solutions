class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        for i in range(n):
            max_left=max(nums[:i+1])
            min_right=min(nums[i:])

            if max_left-min_right<=k:
                return i
        return -1