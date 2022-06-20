def two_sum_quadratic(nums: list, target: int) -> list:
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

def two_sum_linear(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    """
    nums_dict = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in nums_dict:
            return [nums_dict[diff], i]
        nums_dict[n] = i
    return
