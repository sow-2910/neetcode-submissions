class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)):
            # Tối ưu: Nếu số nhỏ nhất > 0, tổng 3 số không thể bằng 0
            if nums[i] > 0: 
                break
                
            # Chặn trùng lặp cho số thứ nhất
            if i > 0 and nums[i] == nums[i-1]: 
                continue
                
            mySet = set()
            for j in range(i + 1, len(nums)):
                # Công thức: nums[i] + nums[j] + target = 0
                target = -(nums[i] + nums[j])
                
                if target in mySet:
                    # Lưu dưới dạng tuple để set có thể nhận
                    res.add((nums[i], target, nums[j])) 
                
                # Thêm số hiện tại vào set để các vòng lặp sau tìm
                mySet.add(nums[j])

        return [list(t) for t in res]