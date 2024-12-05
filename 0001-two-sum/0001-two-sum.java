class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashmap = new HashMap<>();
        int[] output = new int[2];
        for(int i = 0; i < nums.length;i++){
            hashmap.put(nums[i],i);
        }
        for(int i = 0; i < nums.length; i++){
            int k = target - nums[i];
            if(hashmap.get(k) != null && hashmap.get(k) != i){
                output[0] = i;
                output[1] = hashmap.get(k);
                return output;
            }
        }
        return output;
    }
}