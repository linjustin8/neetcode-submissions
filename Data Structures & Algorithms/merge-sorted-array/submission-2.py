class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i  = len(nums1) - 1
        for j in range(n):
            nums1[i], nums2[j] = nums2[j], nums1[i]
            i -= 1
            print(f"nums1 = {nums1}, nums2 = {nums2}")
        
        nums1.sort()
        return nums1