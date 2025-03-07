class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        def isPrime(n):
            if n <= 1:
                return False
            if n<=3:
                return True
            if n%2 == 0 or n%3==0:
                return False
            for j in range(5, int(math.sqrt(n))+1,6):
                # print(n,j)
                if n%j == 0 or n%(j+2) == 0:
                    return False
            return True

        min_diff = float('inf') 
        res = [-1,-1]
        prev_prime = 0
        for i in range(left,right+1):
            if isPrime(i):
                if prev_prime == 0:
                    prev_prime = i
                    continue
                diff = i - prev_prime
                if diff < min_diff:
                    min_diff = diff
                    res = [prev_prime,i]
                prev_prime = i
                # prime_list.append(i)
        # for i in range(1,len(prime_list)):
        #     diff = prime_list[i] - prime_list[i-1]
        #     if diff < min_diff:
        #         min_diff = diff
        #         res = [prime_list[i-1],prime_list[i]]
        return res                
                