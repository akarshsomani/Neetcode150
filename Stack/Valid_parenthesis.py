class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        if len(s) % 2 == 1:
            return False
        i = 0
        st.append(s[i])
        i+=1
        while(i < len(s)):
            if len(st) > 0 and ((st[-1] == '(' and s[i] == ')') or (st[-1] == '[' and s[i] == ']') or (st[-1] == '{' and s[i] == '}')):
                st.pop()
            else:
                st.append(s[i])
            
            i+=1
        
        return len(st) == 0

s = Solution()
print(s.isValid("({[]})"))
print(s.isValid("({[])}"))