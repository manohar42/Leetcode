class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        List<List<Integer>> sol = new ArrayList<>();
        Arrays.sort(nums);
        int n = nums.length;
        for(int i=0;i<nums.length;i++){
            if(i>0 && nums[i]==nums[i-1]){
                continue;
            }
            int left = i+1;
            int right = n-1;
            while(left < right){
                int sum = nums[i]+nums[left]+nums[right];
                if(sum > 0){
                    right-=1;
                    }
                else if(sum <0){
                    left+=1;
                }
                else{
                    // List<Integer> k = new ArrayList<>();
                    // k.add(nums[i]);
                    // k.add(nums[left]);
                    // k.add(nums[right]);
                    
                    sol.add(Arrays.asList(nums[i],nums[left],nums[right]));
                    left++;
                    while(nums[left] == nums[left-1]&&left < right){
                        left++;
                    }

            }
            }
        }
        // for i in 
        return sol;
    }
}