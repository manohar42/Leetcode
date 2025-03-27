class Solution {
    public int majorityElement(int[] nums) {
        
        HashMap<Integer,Integer> hm = new HashMap<>();

        for(int i = 0;i < nums.length;i++){
            
            hm.put(nums[i],hm.getOrDefault(nums[i],0)+1);
        }

        int n = nums.length/2; 
        for(int i = 0;i<nums.length;i++){

            if(hm.get(nums[i])>n){
                return nums[i];
            }
        }
        return 1;
    }
}