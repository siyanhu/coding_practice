import os

def sortArrayByParity(nums):
    to_swith_index = len(nums) - 1
    for i in range(len(nums)):
        if nums[i] % 2 != 0:
            j = to_swith_index
            while j > i:
                if nums[j] % 2 == 0:
                    to_swith_index = j
                    break
                j = j - 1
            mid = nums[j]
            nums[j] = nums[i]
            nums[i] = mid
        # print(nums)
    return nums


if __name__ == "__main__":
    print("Running ", os.path.realpath(__file__))
    nums = [0]
    # nums = [1]
    # nums = [2]
    # nums = [2, 3]
    # nums = [3, 2]
    # nums = [1,0,2]
    nums = [3, 1, 2, 4]
    # nums = [1,0,2,4]
    # nums = [1,0,2,4,6]
    rslt = sortArrayByParity(nums)
    print(rslt)
