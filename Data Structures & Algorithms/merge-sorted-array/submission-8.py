class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        m, n = m - 1, n - 1 # minus one to get index vals
        for i in range(len(nums1) - 1, -1, -1):
            if m < 0 or n < 0:
                nums1[i] = nums1[m] if m > -1 else nums2[n]
                m, n = m - 1, n - 1 
            elif nums1[m] >= nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
        


