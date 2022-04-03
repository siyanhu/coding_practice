import os

def replaceElements(arr):
    i = 0
    while i < len(arr) - 1:
        right_side_max = max(arr[i+1:len(arr)])
        arr[i] = right_side_max
        i = i + 1
    arr[-1] = -1
    return arr


if __name__ == "__main__":
    print("Running ", os.path.realpath(__file__))
    test = [17,18,5,4,6,1]
    replaceElements(test)