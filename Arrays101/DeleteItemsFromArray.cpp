//
// Created by HU Siyan on 7/5/2020.
//

#include <iostream>
#include "DeleteItemsFromArray.h"

int DeleteItemsFromArray::removeElement(std::vector<int> &nums, int val) {
    int i = 0;
    int max_size = nums.size();
    while (i < max_size) {
        if (nums[i] == val) {
            nums.erase(nums.begin() + i);
            max_size = max_size - 1;
        } else {
            i = i + 1;
        }
    }
    return nums.size();
}
