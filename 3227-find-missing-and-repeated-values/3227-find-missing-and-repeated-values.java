class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        
        int n = grid.length;
        double Cell_count = Math.pow(n,2);
        int sum_val = (int)(Cell_count*(Cell_count+1))/2;
        // System.out.println((int)Cell_count);
        HashSet<Integer> hashset = new HashSet<Integer>();
        
        int[] arr = new int[2];
        for(int i = 0; i<n;i++){
            for(int j =0;j<n;j++){
                if(hashset.contains(grid[i][j])){
                    arr[0] = grid[i][j];
                    continue;
                }
                sum_val-=grid[i][j];
                hashset.add(grid[i][j]);
            }
        }
        arr[1] = sum_val;
        return arr;
    }
}