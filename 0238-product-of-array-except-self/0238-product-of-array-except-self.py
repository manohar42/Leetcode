class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        zero_count=0
        for i in nums:
            if i!=0:
                product*=i
            else:
                zero_count+=1
        if zero_count > 1:
            return [0 for i in nums]
        answers = []
        for i in nums:
            if i!=0 and zero_count == 0:
                answers.append(product//i)
            elif i==0:
                answers.append(product)
            else:
                answers.append(0)
        return answers