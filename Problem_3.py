# // Time Complexity : O(n) 
# // Space Complexity : O(1)


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        
        if(len(s) != len(pattern)):
            return False
        
        hash1={}
        hash2={}

        for i in range(len(s)):
            if(s[i] in hash1):
                if(hash1[s[i]] != pattern[i]):
                    return False
            
            else:
                hash1[s[i]] = pattern[i]

                if(pattern[i] in hash2):
                    return False
                else:
                    hash2[pattern[i]] = s[i]


        return True
        