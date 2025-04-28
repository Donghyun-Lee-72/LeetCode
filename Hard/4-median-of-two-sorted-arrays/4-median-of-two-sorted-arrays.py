class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        import numpy as np
        
        # nums1 = np.array(nums1)
        # nums2 = np.array(nums2)
        num = np.median(np.concatenate((nums1, nums2)))
        
        return num
        