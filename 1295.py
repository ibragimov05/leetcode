class Solution(object):
    @staticmethod
    def findNumbers(nums):
        return sum(1 for i in nums if len(str(i)) % 2 == 0)
