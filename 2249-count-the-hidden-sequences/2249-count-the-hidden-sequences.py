class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        
        min_value = 0
        max_value = 0
        value = 0
        count = 0
        for i in differences:
            value +=i
            if value < min_value:
                min_value = value
            if value > max_value:
                max_value = value
        # print(min_value,max_value)
        gap = upper-lower+1
        value_gap = max_value-min_value
        total_gap = gap-value_gap
        return total_gap if total_gap>0 else 0