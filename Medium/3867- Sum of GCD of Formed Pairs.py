class Solution(object):
    def gcd(self,a,b):
        while b != 0:
            a,b=b,a%b
        return a

    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefixGcd=[]
        mxi=0

        #Constuct prefixgcd
        for i in range(len(nums)):
            if nums[i]>mxi:
                mxi=nums[i]
            prefixGcd.append(self.gcd(nums[i], mxi))

        #Sort prefixgcd
        prefixGcd.sort()

        ans=0
        left=0
        right=len(prefixGcd)-1

        #Forming the pairs
        while left<right:
            ans+=self.gcd(prefixGcd[left], prefixGcd[right])
            left=left+1
            right=right-1
        return ans