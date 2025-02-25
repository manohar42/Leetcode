class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:

        even_subarray_count = 1
        odd_subarray_count = 0
        n = len(arr)
        Mod = math.pow(10,9)+7
        count = 0
        array_sum = 0
        for i in range(0,n):
            array_sum+=arr[i]
            if array_sum%2 == 0:
                count += odd_subarray_count
                even_subarray_count+=1
            else:
                count+=even_subarray_count
                odd_subarray_count+=1
            count %= Mod
        return int(count)