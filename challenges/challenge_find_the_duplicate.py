def find_duplicate(nums):
    nums.sort()
    leng = len(nums)

    for i in range(0, leng):
        if (
            leng <= 1
            or not isinstance(nums[i], int)
            or nums[i] < 0
        ):
            return False
        elif i + 1 != leng:
            if nums[i] == nums[i + 1]:
                return nums[i]

    return False
