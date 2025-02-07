class Solution {
    public boolean isAnagram(String s, String t) {

        int[] chars = new int[26];
        int n = s.length();
        int m = t.length();
        if(n!=m){
            return false;
        }
        for(int i = 0; i < n; i++){
            int a = s.charAt(i);
            int b = t.charAt(i);
            chars[a-97] +=1;
            chars[b-97] -=1;

        }
        for(int nums : chars){
        if(nums != 0){
            return false;
        }
        }
        return true;
    }
    
}