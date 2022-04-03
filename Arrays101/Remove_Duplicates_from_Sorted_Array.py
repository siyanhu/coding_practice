import os

def removeDuplicates(nums):
    unique_nums = 0
    for i in range(len(nums) - 1):
        if (i == 0) | (nums[i] != nums[i - 1]):
            unique_nums += 1
    unique_nums += 1
    print(unique_nums)

    real_index = 0
    for i in range(len(nums)):
        if (i == 0) | (nums[i] != nums[i - 1]):
            nums[real_index] = nums[i]
            real_index += 1
        print(i, real_index, nums)
    del nums[real_index:len(nums)]
    print(real_index, nums)
    return nums


if __name__ == "__main__":
    print("Running ", os.path.realpath(__file__))

    nums = [1, 1, 2]
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    removeDuplicates(nums)