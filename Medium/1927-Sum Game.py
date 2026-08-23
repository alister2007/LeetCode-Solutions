class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n=len(num)//2
        diff=0
        left_q=0
        right_q=0

        for i in range (n):
            if num[i]=="?":
                left_q+=1
            else:
                diff=diff+int(num[i])
        for i in range (n,len(num)):
            if num[i]=="?":
                right_q+=1
            else:
                diff=diff-int(num[i])
            
        q_diff=left_q-right_q

        if q_diff==0:
            return diff!=0
        if q_diff%2!=0:
            return True
        
        return diff != -9 * q_diff // 2