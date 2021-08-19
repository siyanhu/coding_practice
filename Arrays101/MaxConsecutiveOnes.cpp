//
// Created by HU Siyan on 4/5/2020.
//

#include "MaxConsecutiveOnes.h"

int MaxConsecutiveOnes::findMaxConsecutiveOnes(std::vector<int> &nums) {
    int i = 0;
    int start = -1;
    int end = -1;
    int valid_count = 0;
    while (i < nums.size()) {
        if (nums[i] == 1) {
            if (start == -1) {
                start = i;
                end = i;
            } else {
                end = i;
            }
            int currentValid = end - start + 1;
            if (currentValid > valid_count)
                valid_count = currentValid;
        } else {
            start = -1;
            end = -1;
        }
        i = i + 1;
    }

    return valid_count;
}
