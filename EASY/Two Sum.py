class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = [(i, j) for i in range(len(nums)) for j in range(len(nums)) if nums[i] + nums[j] == target and i != j]
        return result[0]
        