class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)

        min_i=nums.index(min(nums))
        max_i=nums.index(max(nums))

        left=min(min_i,max_i)
        right=max(min_i,max_i)

        #Remove both from front
        front=right+1

        #Remove both from back
        back=n-left

        #Remove from both the sides
        both=(left+1)+(n-right)
        return min(front, back, both)