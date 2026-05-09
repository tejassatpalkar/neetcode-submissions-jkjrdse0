class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        totalNums = set(nums)
        maxLCS = 0
        for val in totalNums:
            if val -1 in totalNums:
                continue
            curVal = val
            while curVal in totalNums:
                curVal+=1
                maxLCS = max(maxLCS,curVal-val)
        return maxLCS
                




            



       

        