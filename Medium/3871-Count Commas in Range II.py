class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        total=0
        power=1000
        commas=1

        while power<=n:
            next_power=power*1000
            if next_power<=n:
                count=next_power-power
            else:
                count=n-power+1
            total+=count*commas
            power=next_power
            commas+=1
        return total