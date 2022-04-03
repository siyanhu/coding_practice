import os

def sortedSquares(nums):
    nums =[s * s for s in nums]
    nums.sort()
    return nums


if __name__ == "__main__":
    print("Running ", os.path.realpath(__file__))
    nums = [-7, -3, 2, 3, 11]
    nums = [-4, -1, 0, 3, 10]
    rslt = sortedSquares(nums)
    print(rslt)