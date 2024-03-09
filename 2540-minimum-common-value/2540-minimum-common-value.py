class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        idx1 = 0
        idx2 = 0
        
        while idx1 < len(nums1) and idx2 <len(nums2):
            if nums1[idx1] < nums2[idx2]:
                idx1 += 1
            elif nums2[idx2] < nums1[idx1]:
                idx2 += 1
            else:
                return nums1[idx1]
        
        return -1
        
        