# // Time Complexity : O(n) x (k log k) where k is length of string
# // Space Complexity : O(n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = {}
        for i in strs:
            temp = "".join(sorted(i))
            if(temp not in hashMap):
                hashMap[temp] = []
            hashMap[temp].append(i)
        return (list(hashMap.values()))
        