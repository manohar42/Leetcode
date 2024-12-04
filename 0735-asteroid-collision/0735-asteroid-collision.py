class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        res = []
        n = len(asteroids)
        for i in range(n):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            else:
                check = False
                
                while len(stack) > 0:
                    # print(stack,asteroids[i])
                    k = stack.pop()
                    if k > 0:
                        if k > abs(asteroids[i]):
                            stack.append(k)
                            check = True
                            break
                        elif k == abs(asteroids[i]):
                            check = True
                            break
                        else:
                            continue
                    else:
                        stack.append(k)
                        break
                
                if check == False:
                    stack.append(asteroids[i])
                # print(stack)
                
        return stack
                        