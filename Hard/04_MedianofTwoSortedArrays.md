### Tuesday, September 17th 2024, 2:28 pm

### Problem
_Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays._

The overall runtime complexity should be O(log(m+n)).
#### Example 1

> **Input:** nums1 = [1, 3], nums2 = [2]  
> **Output:** 2.00000  
> **Explanation:** Merged array = [1, 2, 3] and the median is 2.

#### Example 2

> **Input:** nums1 = [1, 2], nums2 = [3, 4]  
> **Output:** 2.50000  
> **Explanation:** Merged array = [1, 2, 3, 4] and the median is (2 + 3) / 2 = 2.5.
---
### Solution
```
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        int arr1Counter = 0;
        int arr2Counter = 0;
        int largestArr = m + n;
        double median = 0;
        int[] combinedArr = new int[largestArr];

        for (int i = 0; i < largestArr; i++) {
            if (arr1Counter >= m) {
                combinedArr[i] = nums2[arr2Counter];
                arr2Counter++;
            } else if (arr2Counter >= n) {
                combinedArr[i] = nums1[arr1Counter];
                arr1Counter++;
            } else if (nums1[arr1Counter] <= nums2[arr2Counter]) {
                combinedArr[i] = nums1[arr1Counter];
                arr1Counter++;
            } else {
                combinedArr[i] = nums2[arr2Counter];
                arr2Counter++;
            }
        }

        if (combinedArr.length % 2 == 0) {
            median = ((double) combinedArr[combinedArr.length / 2] + (double) combinedArr[combinedArr.length / 2 - 1]) / 2;
        } else {
            median = (double) combinedArr[combinedArr.length / 2];
        }
        return median;
    }
}
```

This solution is a pure brute force on how to solve the problem, there is better ways of solving this problem, such as using a binary search algorithm, however I was low on time today. 
