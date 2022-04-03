import os


def moveZeroes(nums, val):
    real_index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[real_index] = nums[i]
            if real_index < i:
                nums[i] = 0
            real_index += 1
    del nums[real_index:len(nums)]
    return nums


if __name__ == "__main__":
    print("Running ", os.path.realpath(__file__))

    # nums = [0]
    # nums = [1]
    nums = [0, 1, 0, 3, 12]
    nums = [3, 2, 2, 3]
    val = 3
    rslt = moveZeroes(nums, val=val)
    print(rslt)