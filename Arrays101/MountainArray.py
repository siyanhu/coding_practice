import os

def compare_norm(arr, current_index, ascending=True):
    current_elem = arr[current_index]

    if current_index == len(arr) - 1:
        prev_elem = arr[current_index - 1]
        if prev_elem > current_elem:
            return True
        else:
            return False

    next_elem = arr[current_index + 1]
    if ascending:
        if (next_elem > current_elem):
            return True
    else:
        if (current_elem > next_elem):
            return True

    if current_elem == next_elem:
        return False

    return False


def validMountainArray(arr):
    if len(arr) < 3:
        return False

    i = 0
    has_switched = False
    to_ascend = (arr[1] > arr[0])
    if to_ascend == False:
        return False

    to_continue = True
    while i < len(arr):
        to_continue = compare_norm(arr, current_index=i, ascending=to_ascend)

        if to_continue == False:
            if has_switched == False:
                to_ascend = False
                has_switched = True
            else:
                return False
        i = i + 1

    return to_continue



if __name__ == "__main__":
    print("Running ", os.path.realpath(__file__))

    # test = [1, 3, 2]
    # test = [3, 5, 5]
    # test = [0, 3, 2, 1]
    test = [6, 7, 7, 8, 6]
    # test = [0, 1, 2, 3, 4, 5]
    # test = [0, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 0]
    # test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 1, 0]
    # test = [9, 8 , 7, 6, 5, 4, 3, 2, 1, 0]
    # test = [3, 7, 6, 4, 3, 0, 1, 0]
    result = validMountainArray(test)
    print(result)