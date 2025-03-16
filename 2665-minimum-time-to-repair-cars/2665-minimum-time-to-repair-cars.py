class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        start = 1
        end = min(ranks)*(cars*cars)
        def check(mid,ranks,cars):
            car_count = 0
            for i in range(len(ranks)):
                num_squared_count = mid//ranks[i]
                num_count = int(math.sqrt(num_squared_count))
                car_count+=num_count
                if car_count>=cars:
                    return True
            return False



        while start < end:
            mid = (start+end)//2
            # print(mid,start,end)
            if check(mid,ranks,cars):
                end = mid
            else:
                start = mid+1
        
        return start