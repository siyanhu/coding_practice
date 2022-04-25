import os


def intersection(num):
    print("input nums: ", num)
    if len(num) == 1:
        print("output intersections: ", num[0])
        # num[0].sort()
        return num[0]

    i = 1
    keys = num[0].copy()
    while i < len(num):
        if len(num[0]) == 0:
            return []
        for k in keys:
            if k in num[i]:
                continue
            elif k in num[0]:
                num[0].remove(k)
        i += 1
    num[0].sort()
    print("output intersections: ", num[0])
    return num[0]


if __name__ == "__main__":
    print("Running ", os.path.realpath(__file__))
    nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
    # nums = [[1,2,3],[4,5,6]]

    intersection(nums)