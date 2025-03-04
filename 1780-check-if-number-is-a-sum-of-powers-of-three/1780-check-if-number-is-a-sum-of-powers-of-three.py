class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n>0:
            d = n%3
            if d == 2:
                return False
            n //=3
        return True

    
        