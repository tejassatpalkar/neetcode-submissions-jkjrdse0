class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, iv in enumerate(numbers):
            for j, jv in enumerate(numbers):
                if i != j and iv + jv == target:
                    return [i+1,j+1]
        return []