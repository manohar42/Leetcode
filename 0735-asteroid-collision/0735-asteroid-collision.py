class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = [] 
        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            else:
                check = False
                while len(stack) > 0 and stack[-1] > 0:
                    k = stack.pop()
                    if k > abs(asteroids[i]):
                        stack.append(k)
                        check = True
                        break
                    elif k == abs(asteroids[i]):
                        check = True
                        break
                    else:
                        continue
                
                if check == False:
                    stack.append(asteroids[i])                
        return stack
                        