class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Find the l,r that maximizes area. 
        Container area = min(heights[l],heights[r]) * (r,l)
        """

        ## Concise Naive Solution O(n^2)
        # maxArea = 0
        # for l in range(len(heights)):
        #     for r in range(1,len(heights)):
        #         area = min(heights[l], heights[r]) * (r -l)
        #         maxArea = max(area, maxArea)
        
        # return maxArea

        l = 0
        r = len(heights)-1
        maxArea = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r -l)
            maxArea = max(area, maxArea)
            
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        
        return maxArea

                

