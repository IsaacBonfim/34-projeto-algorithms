def find_duplicate(nums):
    if (len(nums) <= 1):
        return False

    nums.sort()
    leng = len(nums)

    for i in range(0, leng):
        if (
            not isinstance(nums[i], int)
            or nums[i] < 0
        ):
            return False
        elif i + 1 != leng:
            if nums[i] == nums[i + 1]:
                return nums[i]

    return False
