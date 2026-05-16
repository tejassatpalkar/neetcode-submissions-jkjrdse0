class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Find the l,r that maximizes area. 
        Container area = min(heights[l],heights[r]) * (r,l)
        """
        maxArea = 0
        for l in range(len(heights)):
            for r in range(1,len(heights)):
                area = min(heights[l], heights[r]) * (r -l)
                maxArea = max(area, maxArea)
        
        return maxArea
                