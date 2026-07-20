class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if len(s1) > len(s2):
            return False

        s1counter = [0] * 26
        s2counter = [0] * 26
        for i in range(l1):
            s1counter[ord(s1[i])-ord('a')] += 1
            s2counter[ord(s2[i])-ord('a')] += 1
        matches = 0
        for i in range(26):
            if(s1counter[i] == s2counter[i]):
                matches+=1
        l = 0
        for r in range(l1, l2):
            if matches  == 26:
                return True
     
            index  =  ord(s2[r]) - ord('a')
            if s1counter[index] == s2counter[index]:
                matches -= 1
            s2counter[index] += 1
            if s2counter[index] == s1counter[index]:
                matches += 1

            index  =  ord(s2[l])-ord('a')
            if s1counter[index] == s2counter[index]:
                matches -= 1
            s2counter[index] -= 1
            if s2counter[index] == s1counter[index]:
                matches += 1
            l+=1
        return matches == 26

            
            
s = Solution()
print(s.checkInclusion(s1 = "abc", s2 = "lecabee"))