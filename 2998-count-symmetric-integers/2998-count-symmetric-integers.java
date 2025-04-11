class Solution {
    public int countSymmetricIntegers(int low, int high) {
        int sym_count = 0;
        for(int i =low;i<=high;i++){

            int digit_count = odd_Check(i);
            int left = 0;
            int right = 0;
            if(digit_count%2==0){
                // System.out.println(digit_count+" "+i);
                int k = digit_count/2;
                int j = i;
                while(k>0){
                    left+=j%10;
                    k-=1;
                    j=j/10;
                    
                }
                k = digit_count/2;
                while(k>0){
                    right+=j%10;
                    k-=1;
                    j=j/10;
                }
                // System.out.println(left+" "+right);
                if(left==right && left != 0){
                    sym_count+=1;
                }

            }
        }
        return sym_count;
    }

    public static int odd_Check(int n){

        int count = 0;
        while(n>0){
            n = n/10;
            count++;
        }
        return count;
    }
}