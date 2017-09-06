# Time:  O(n)
# Space: O(n)

# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup: 
            #Calculate the difference between the targer and current value - if it appears in previous list of values, then output those key values
                print target,num
                print lookup
                return [lookup[target - num], i]
            #Always store the num as key and index as val in it
            lookup[num] = i
        return []

if __name__ == '__main__':
    print Solution().twoSum((1, 7, 11, 15,12), 27)
