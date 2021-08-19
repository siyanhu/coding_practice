#include <vector>
#include "MountainArray.h"

int main() {
    std::vector<int> nums = {9,8,7,6,5,4,3,2,1,0};
    MountainArray test;
    test.validMountainArray(nums);
    return 0;
}
