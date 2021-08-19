//
// Created by HU Siyan on 5/5/2020.
//

#include <iostream>
#include "MergedSortedArray.h"

void MergedSortedArray::merge(std::vector<int> &nums1, int m, std::vector<int> &nums2, int n) {
    if (nums1.size() < m + n) {
        return;
    }
    for (int i = m; i < n + m; i++) {
        nums1[i] = nums2[i - m];
    }

    for (int gap = nums1.size()/2; gap > 0; gap/=2) {
        for (int i = gap; i < nums1.size(); i++) {
            int j = i;
            while (j - gap >= 0 && nums1[j] < nums1[j - gap]) {
                int temp = nums1[j - gap];
                nums1[j - gap] = nums1[j];
                nums1[j] = temp;
                j = j - gap;
            }
        }
    }
}
