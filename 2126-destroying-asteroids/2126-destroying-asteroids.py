class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        

        asteroids.sort()

        for i in range(0,len(asteroids)):
            if mass >= asteroids[i]:
                mass+=asteroids[i]
            else:
                return False
        return True