class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill)-1
        pair_sum = skill[left]+skill[right]
        skill_sum = 0
        while left < right:
            check_sum = skill[left]+skill[right]
            if check_sum == pair_sum:
                skill_sum +=(skill[left]*skill[right])
            else:
                return -1
                
            left+=1
            right-=1
        return skill_sum
            
            


