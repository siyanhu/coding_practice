import os


def findDisappearedNumbers(nums):
    n = len(nums)
    nums = list(set(nums))
    nums.sort()
    disp_nums = list()
    if nums[0] > 1:
        disp_nums = list(range(1, nums[0]))
    for i in range(len(nums) - 1):
        if nums[i + 1] - nums[i] > 1:
            disp_nums = disp_nums + list(range(nums[i] + 1, nums[i + 1]))

    if nums[-1] < n:
        disp_nums += list(range(nums[-1] + 1, n + 1))
    return disp_nums



if __name__ == "__main__":
    print("Running ", os.path.realpath(__file__))
    nums = [1, 1]
    # nums = [4, 3, 2, 7, 8, 2, 3, 1]
    rslt = findDisappearedNumbers(nums)
    print(rslt)