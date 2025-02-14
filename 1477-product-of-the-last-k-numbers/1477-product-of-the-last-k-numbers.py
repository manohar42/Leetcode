class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.prefix_sum = []
        self.product = 0
    def add(self, num: int) -> None:
        self.nums.append(num)
        if num == 0:
            self.product = 0
            self.prefix_sum = []
            return
        if self.product == 0:
            self.product = num
        else:
            self.product *= num
        self.prefix_sum.append(self.product)
        
    def getProduct(self, k: int) -> int:
        # n = len(self.nums)
        # product = 1
        n = len(self.prefix_sum)
        # print(self.prefix_sum,n,k)
        if n == k:
            return self.prefix_sum[-1]
        
        if n>k and self.prefix_sum[n-k-1]!= 0:
            return self.prefix_sum[-1]//self.prefix_sum[n-k-1]
        else:
            return 0
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)