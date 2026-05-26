class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr.sort()
        mean = 0
        if (len(nums1) + len(nums2)) % 2 == 0:
            mean = (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2
        else:
            mean = arr[len(arr) // 2]

        return mean
