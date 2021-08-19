//
// Created by HU Siyan on 4/5/2020.
//

#include <math.h>
#include "SquareSortedArray.h"

std::vector<int> InsertedSorted(std::vector<int> &A) {
    if (A.size() <= 0)
        return A;
    std::vector<int> squared(A.size());
    squared[0] = pow(A[0], 2);
    for (int i = 1; i < A.size();i++) {
        squared[i] = pow(A[i], 2);
        for (int j = i; j > 0; j--) {
            if (squared[j] < squared[j - 1]) {
                int temp = squared[j - 1];
                squared[j - 1] = squared[j];
                squared[j] = temp;
            }
        }
    }
    return squared;
}

std::vector<int> SquareSortedArray::sortedSquares(std::vector<int> &A) {
    if (A.size() <= 0)
        return A;
    std::vector<int> powed(A.size());
    for (int i = 0; i < A.size(); i++) {
        powed[i] = pow(A[i], 2);
    }

    if (powed.size() <= 0)
        return A;

    for (int gap = powed.size()/2; gap > 0; gap/=2) {
        for (int i = gap; i < powed.size(); i++) {
            int j = i;
            while (j - gap >= 0 && powed[j] < powed[j - gap]) {
                int temp = powed[j - gap];
                powed[j - gap] = powed[j];
                powed[j] = temp;
                j = j - gap;
            }
        }
    }

    return powed;
}
