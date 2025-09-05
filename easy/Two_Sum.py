class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dic = {}
        nums_dic[nums[0]] = 0
        answer_list = []
        for i in range(1, len(nums)):
            discount = target - nums[i]
            value = nums_dic.get(discount)
            if value is not None:
                answer_list.append(i)
                answer_list.append(nums_dic.get(discount))
                return answer_list
            else:
                nums_dic[nums[i]] = i
            
            
        





