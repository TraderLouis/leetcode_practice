class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        now_array = nums
        mid = len(now_array) // 2
        t_index = mid

        while(target != nums[t_index] and len(now_array) > 3):
            if target < nums[t_index]:
                now_array = nums[0 : t_index]
                mid = len(now_array) // 2
                t_index -= mid
            elif target > nums[t_index]:
                now_array = nums[t_index + 1 :]
                mid = len(now_array) // 2
                t_index += mid
            else:
                return t_index

        if nums[t_index] == target:
            return t_index
        else:
            return -1



