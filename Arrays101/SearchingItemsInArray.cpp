//
// Created by HU Siyan on 7/5/2020.
//

#include "SearchingItemsInArray.h"

bool hasRelation(int n, int m) {
    //relation: check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
    int m2 = m * 2;
    int n2 = n * 2;
    return (m2 == n) || (n2 == m);
}

bool SearchingItemsInArray::checkIfExist(std::vector<int> &arr) {
    if (arr.size() <= 1)
        return false;
    int i = 0;
    while (i < arr.size() - 1) {
        int cur = arr[i];
        for (int j = i + 1; j < arr.size(); j++) {
            int cur1 = arr[j];
            bool has = hasRelation(cur, cur1);
            if (has)
                return true;
        }
        i = i + 1;
    }

    return false;
}
