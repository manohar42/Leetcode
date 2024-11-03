class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        hashmap = {}
        for i in hashmap:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i] = 1
        n = len(s)
        if s == goal:
            return True
        st = s
        for i in range(n):
            my_list = list(st)
            k = my_list.pop(0)
            my_list.append(k)
            st = "".join(my_list)
            if st == goal:
                return True
        return False