class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""

        expected = {}
        for char in t:
            expected[char] = expected.get(char, 0) + 1
        
        # FIX 1: 'need' is the count of unique characters in t
        have = 0
        need = len(expected) 

        window = {}
        left = 0
        
        # FIX 2: Use min_len for a minimum window problem
        min_len = float('inf')
        sol = [-1, -1] 

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in expected and window[char] == expected[char]:
                have += 1
            
            while have == need:
                # FIX 3: Record the valid window INSIDE the while loop
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    sol = [left, right]
                
                # FIX 4: Process the left character BEFORE incrementing left
                left_char = s[left]
                window[left_char] -= 1
                if left_char in expected and window[left_char] < expected[left_char]:
                    have -= 1
                
                left += 1
                
        # FIX 5: Handle the no-match edge case and include the right-most character (+1)
        return s[sol[0]:sol[1]+1] if min_len != float('inf') else ""