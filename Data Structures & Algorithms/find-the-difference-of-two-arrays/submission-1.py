class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)

        one = [n for n in s1 if n not in s2]
        two = [n for n in s2 if n not in s1]
        return [one, two]
