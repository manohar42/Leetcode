class Solution {
    public int minOperations(int[][] grid, int x) {
        int m = grid.length;
        int n = grid[0].length;
        int[] nums = new int[m*n];
        int k = 0;
        for(int i= 0;i<m;i++){
            for(int j = 0;j<n;j++){
                nums[k] = grid[i][j];
                k+=1;
            }
        }
        Arrays.sort(nums);
        int mid_length = (int)nums.length/2;
        // System.out.println(mid_length);
        int median_value = nums[mid_length];
        // System.out.println(median_value);
        int result = 0; 
        for(int i =0;i<m*n;i++){
            
            if(nums[i]%x != median_value%x){
                return -1;
            } 
            result+=Math.abs(nums[i]-median_value)/x;
        }
    
        return result;

    }
}