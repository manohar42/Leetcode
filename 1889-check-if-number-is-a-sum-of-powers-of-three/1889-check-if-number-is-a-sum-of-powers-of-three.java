class Solution {
    public boolean checkPowersOfThree(int n) {
        int start = 1;
        
        List <Long> power_of_3 = new ArrayList<Long>();
        
        power_of_3.add(1L);
        long value = 1;
        for(int i = 1;i<17;i++){
            value *=3;
            power_of_3.add(value);
            
        }
        // System.out.println(power_of_3);
        for(int i = power_of_3.size()-1;i>=0;i--){
            if(n >= power_of_3.get(i)){
                n-= power_of_3.get(i);
                // System.out.println(n+" "+ power_of_3.get(i));
                if(n==0){
                    return true;
                }
            }
        }
        return false;
    }
}