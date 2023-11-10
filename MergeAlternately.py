class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        for i in range(100):
            if(i < len(word1)):
                output += word1[i]
            if(i < len(word2)):
                output += word2[i]

            
        return output
