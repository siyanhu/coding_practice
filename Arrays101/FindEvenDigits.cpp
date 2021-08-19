//
// Created by HU Siyan on 4/5/2020.
//

#include <iostream>
#include "FindEvenDigits.h"

int findDigit(int num) {
    int i = 0;
    int quotient = num;
    while (quotient != 0) {
        quotient = quotient / 10;
        i = i + 1;
    }
    return i;
}

int FindEvenDigits::findNumbers(std::vector<int> &nums) {
    int i = 0;
    int valid_count = 0;
    while (i < nums.size()) {
        int digit = findDigit(nums[i]);
        if (digit % 2 == 0)
            valid_count = valid_count + 1;
        i = i + 1;
    }
    return 0;
}
