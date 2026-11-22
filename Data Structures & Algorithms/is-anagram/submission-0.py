class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for i in range(len(s)):
            if s[i] in count:
                count[s[i]] +=1
            else:
                count[s[i]] = 1
            
        for j in range(len(t)):
            if t[j] in count:
                count[t[j]] -= 1
            else:
                count[t[j]] = -1
        
        return all(value == 0 for value in count.values())