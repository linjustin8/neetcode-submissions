class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        half = length // 2
        A, B = nums1, nums2
        if len(A) < len(B):
            A, B = B, A

        l, r = 0, len(B) - 1
        while True:
            m = (l + r) // 2
            m2 = half - m - 2

            BPrev = B[m] if m >= 0 else -math.inf
            APrev = A[m2] if m2 >= 0 else -math.inf
            BNext = B[m + 1] if m + 1 < len(B) else math.inf
            ANext = A[m2+ 1] if m2 + 1 < len(A) else math.inf

            if APrev <= BNext and BPrev <= ANext:
                if length % 2 == 0:
                    return (max(APrev, BPrev) + min(ANext, BNext)) / 2.0
                else:
                    return min(ANext, BNext)
            elif BPrev > ANext:
                r = m - 1
            else:
                l = m + 1
        