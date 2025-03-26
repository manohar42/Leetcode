class Solution {
    public int minMoves2(int[] nums) {
        
        Arrays.sort(nums);
        int sum = 0;
        for(int i =0; i<nums.length;i++){
            sum+=nums[i];
        }
        int mid = nums.length/2;
        int median = nums[mid];
        int number_of_operations = 0;
        for(int i = 0;i<nums.length;i++){
            number_of_operations+=Math.abs(median - nums[i]);
        }
        return number_of_operations;
    }
}