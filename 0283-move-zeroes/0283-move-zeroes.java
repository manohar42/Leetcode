class Solution {

    public void moveZeroes(int[] nums) {
        ArrayList<Integer> alist = new ArrayList<Integer>();

        int left = 0;
        int right = 0;
        for(int i = 0;i<nums.length;i++){
            if(nums[i] == 0){
                alist.add(i);
            }
            else{
                if(alist.size() > 0){
                    // int k = ;
                    nums[alist.get(0)] = nums[i];
                    alist.remove(0);
                    nums[i] = 0;
                    alist.add(i);
                }
            }
        }
        

    }
}