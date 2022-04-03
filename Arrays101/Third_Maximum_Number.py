import os

def thirdMax(nums):
    nums = list(set(nums))
    nums.sort()
    if len(nums) < 3:
        return nums[-1]
    else:
        return nums[-3]



if __name__ == "__main__":
    print("Running ", os.path.realpath(__file__))
    nums = [3, 2, 1]
    nums = [1, 2]
    nums = [2, 2, 3, 1, 4, 4, 3, 6, 2]
    rstl = thirdMax(nums)
    print(rstl)