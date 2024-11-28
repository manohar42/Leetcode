class Solution:
    def reorderSpaces(self, text: str) -> str:
        
        words = text.split()
        spaces = text.count(' ')
        len_words = len(words)

        if len_words == 1:
            
            return "".join([words, ' ' * spaces])
        
        separator = " "*(spaces // (len_words-1))
        trail = " "*(spaces % (len_words-1))
        sentence = separator.join(words)
        return "".join([sentence,trail])
