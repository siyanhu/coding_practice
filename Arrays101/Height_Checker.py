import os


def heightChecker(heights):
    diff_count = 0
    ori = heights[:]
    heights.sort()
    for i in range(len(heights)):
        if ori[i] != heights[i]:
            diff_count += 1
    # print(heights)
    return diff_count

if __name__ == "__main__":
    print("Running ", os.path.realpath(__file__))
    heights = [1, 1, 4, 2, 1, 3]
    rslt = heightChecker(heights)
    print(rslt)