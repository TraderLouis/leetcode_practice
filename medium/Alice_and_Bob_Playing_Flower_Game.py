class Solution(object):
    def flowerGame(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        return ((n/2 + n%2) * (m/2)) + ((m/2 + m%2) * (n/2))
