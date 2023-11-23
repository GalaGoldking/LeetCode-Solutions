class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        allNums = sorted(nums1+nums2)
        if len(allNums) % 2 == 0:
            mid = int(len(allNums)/2)
            ans = (allNums[mid-1]+allNums[mid])/2
            return float(ans)
        else:
            mid = int(len(allNums)/2)
            ans = allNums[mid]
            return float(ans)