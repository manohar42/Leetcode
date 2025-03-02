class Solution {
    public int[][] mergeArrays(int[][] nums1, int[][] nums2) {
        
        

        int i = 0;
        int j = 0;
        int n = nums1.length;
        int m = nums2.length;
        int[][] res = new int[n+m][2];
        int count = 0;
        while(i<n && j< m){
            if(nums1[i][0] == nums2[j][0]){
                res[count][0] = nums1[i][0];
                res[count][1] = nums1[i][1]+nums2[j][1];
                count++;
                i++;
                j++;
            }
            else if(nums1[i][0] < nums2[j][0]){
                res[count][0] = nums1[i][0];
                res[count][1] = nums1[i][1];
                count++;
                i++;
            }
            else{
                res[count][0] =nums2[j][0];
                res[count][1] = nums2[j][1];
                count++;
                j++;
            }
        }
        while(i<n){
            res[count][0] = nums1[i][0];
            res[count][1] = nums1[i][1];
            i++;
            count++;
        }
        while(j<m){
            res[count][0] = nums2[j][0];
            res[count][1] = nums2[j][1];
            j++;
            count++;
        }

         return Arrays.copyOf(res, count);


    }
}