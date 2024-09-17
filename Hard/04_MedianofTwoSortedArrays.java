class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        int arr1Counter = 0;
        int arr2Counter = 0;
        int largestArr =  m + n;
        double median = 0;
        int[] combinedArr = new int[largestArr]; 
        for (int i = 0; i < largestArr; i++){
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

        if (combinedArr.length % 2 == 0){
            median = ((double)combinedArr[combinedArr.length/2] + (double)combinedArr[combinedArr.length/2 - 1])/2;
        }
        else {
            median = (double) combinedArr[combinedArr.length/2];
        }
        for (int i = 0; i < combinedArr.length; i++) {
        System.out.println(combinedArr[i]);
}
        return median;
    }
}