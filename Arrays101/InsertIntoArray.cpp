//
// Created by HU Siyan on 5/5/2020.
//

#include <iostream>
#include "InsertIntoArray.h"

void InsertIntoArray::duplicateZeros(std::vector<int> &arr) {
    std::vector<int> result(arr.size());
    int i = 0;
    int result_index = 0;
    while (result_index < arr.size()) {
        result[result_index] = arr[i];
        if (arr[i] == 0) {
            result_index = result_index + 1;
            if (result_index >= arr.size() - 1) {
                break;
            }
            result[result_index] = 0;
            result_index = result_index + 1;
        } else {
            result_index = result_index + 1;
        }
        i = i + 1;
    }
    if (i - 1 != arr.size() - 1) {
        arr = result;
        std::cout<<"";
    }
}
