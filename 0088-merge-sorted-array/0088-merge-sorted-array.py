class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for _ in range(m, len(nums1)):
            nums1.pop(m)
        
        i, j = 0, 0
        while i < len(nums1) and j < n:
            if nums2[j] <= nums1[i]:
                nums1.insert(i, nums2[j])
                j += 1
            else:
                i += 1
        
        for j in range(j, n):
            nums1.append(nums2[j])