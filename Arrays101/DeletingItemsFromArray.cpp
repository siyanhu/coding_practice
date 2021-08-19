//
// Created by HU Siyan on 7/5/2020.
//

#include "DeletingItemsFromArray.h"

int DeletingItemsFromArray::removeDuplicates(std::vector<int> &nums) {
    if (nums.size() <= 1)
        return nums.size();
    int last = nums[0];
    int i = 1;
    int max_size = nums.size();
    while (i < max_size) {
        if (nums[i] == last) {
            nums.erase(nums.begin() + i);
            max_size = max_size - 1;
        } else {
            last = nums[i];
            i = i + 1;
        }
    }
    return nums.size();
}
