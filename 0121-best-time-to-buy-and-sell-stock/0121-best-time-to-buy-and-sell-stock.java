class Solution {
    public int maxProfit(int[] prices) {
        int min_value = prices[0];
        int max_profit = 0;
        for(int i = 1;i < prices.length;i++){
            if(prices[i] < min_value){
                min_value = prices[i];
            }
            else{
                int profit_value = prices[i] - min_value;
                
                max_profit = Math.max(max_profit,profit_value);
            }
        }
        return max_profit;
    }
}