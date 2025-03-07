class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        def isPrimes(n):
            isPrime = [True for i in range(0,n)]
            primes = []
            isPrime[0] =False
            isPrime[1] = False
            for i in range(2,n):
                primes.append(i)
                for j in range(i*i,n,i):
                    isPrime[j] = False
            return isPrime

        min_diff = float('inf') 
        res = [-1,-1]
        prev_prime = 0
        # for i in range(left,right+1):
        #     if (i%2 == 0 and i >2) or (i%3 == 0  and i > 3):
        #         continue
        #     if isPrime(i):
        #         if prev_prime == 0:
        #             prev_prime = i
        #             continue
        #         diff = i - prev_prime
        #         if diff < min_diff:
        #             min_diff = diff
        #             res = [prev_prime,i]
        #         prev_prime = i
        # return res                
        primes = isPrimes(right+1)

        for i in range(left,right+1):
            if primes[i] == True:
                if prev_prime == 0:
                    prev_prime = i
                    continue
                diff = i - prev_prime
                if diff < min_diff:
                    min_diff = diff
                    res = [prev_prime,i]
                prev_prime = i
        return res        