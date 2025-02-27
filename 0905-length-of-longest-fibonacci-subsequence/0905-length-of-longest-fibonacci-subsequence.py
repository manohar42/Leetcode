class Solution:
    # def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
    #     class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        n = len(arr)
        max_len = 0
        dp = [[0] * n for _ in range(n)]

        hashmap = {num: idx for idx, num in enumerate(arr)}

       
        for curr in range(n):
            for prev in range(curr):
                # Find if there exists a previous number to form Fibonacci sequence
                diff = arr[curr] - arr[prev]
                prev_idx = hashmap.get(diff, -1)

                # Update dp if valid Fibonacci sequence possible
                # diff < arr[prev] ensures strictly increasing sequence
                dp[prev][curr] = (
                    dp[prev_idx][prev] + 1
                    if diff < arr[prev] and prev_idx >= 0
                    else 2
                )
                max_len = max(max_len, dp[prev][curr])

        # Return 0 if no sequence of length > 2 found
        return max_len if max_len > 2 else 0