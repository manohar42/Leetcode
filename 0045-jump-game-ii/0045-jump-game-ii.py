class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # max_reach = 0
        # count = 0
        # n= len(nums)-1
        # cur = n-1
        # jump=[0]*(n+1)
        # target = n

        # while cur >=0:
        #     cur_reach = cur+nums[cur]

        #     if cur_reach >= target:
        #         jump[cur] = 1
        #     elif nums[cur] > 0:
        #         jump[cur] = min(jump[cur+1:cur_reach+1])+1
        #     else:
        #         jump[cur] = n

        #     cur-=1

        # return jump[0]

        n = len(nums)-1
        jump = [0]*(n+1)
        cur = n-1
        target = n
        while cur >= 0:
            cur_reach = nums[cur]+cur
            if cur_reach >= target:
                jump[cur] = 1
            elif nums[cur] > 0:
                jump[cur] = 1+min(jump[cur+1 : cur_reach+1])
            else:
                jump[cur]= n
            cur -=1
        return jump[0]

