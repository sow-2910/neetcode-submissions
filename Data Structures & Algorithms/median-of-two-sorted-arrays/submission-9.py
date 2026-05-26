from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        # Đảm bảo mảng A luôn là mảng ngắn hơn
        if len(nums1) > len(nums2):
            A, B = B, A

        total_len = len(A) + len(B) # Nên dùng len(A) + len(B) sau khi đã hoán đổi vị trí
        half_len = (total_len + 1) // 2

        left, right = 0, len(A)
        while left <= right:
            cutA = (left + right) // 2
            cutB = half_len - cutA

            # SỬA: Thay '-infinity' bằng '-inf', 'infinity' bằng 'inf'
            leftA = A[cutA - 1] if cutA > 0  else float('-inf')
            rightA = A[cutA] if cutA < len(A) else float('inf')

            # SỬA: Nếu cutB == 0, leftB phải là giá trị âm vô cực '-inf'
            leftB = B[cutB - 1] if cutB > 0 else float('-inf')
            rightB = B[cutB] if cutB < len(B) else float('inf')

            # Kiểm tra vách ngăn hợp lệ
            if leftA <= rightB and leftB <= rightA:
                if total_len % 2 != 0:
                    # SỬA: Tổng lẻ thì trung vị nằm ở phần tử lớn nhất bên tay TRÁI
                    return max(leftA, leftB)
                else:
                    # Tổng chẵn: trung bình cộng của số lớn nhất bên trái và nhỏ nhất bên phải
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
            
            elif leftA > rightB:
                # Vách ngăn của A quá tiến về bên phải, cần dịch sang trái
                right = cutA - 1
            else:
                # Vách ngăn của A quá lùi về bên trái, cần dịch sang phải
                left = cutA + 1