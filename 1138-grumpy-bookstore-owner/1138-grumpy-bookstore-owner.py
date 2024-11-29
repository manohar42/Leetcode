class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        left = 0
        max_customers_satisified = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                max_customers_satisified+=customers[i]

        Lsum = max_customers_satisified
        for i in range(minutes):
            if grumpy[i] ==1:
                Lsum+=customers[i]
        right = minutes
        max_customers_satisified = max(max_customers_satisified,Lsum)
        while right < len(grumpy):       
            if grumpy[left] == 1:
                Lsum-=customers[left]
            left+=1
            
            if grumpy[right] == 1:
                Lsum+=customers[right]
            right+=1  
            max_customers_satisified = max(max_customers_satisified,Lsum)
            
        return max_customers_satisified