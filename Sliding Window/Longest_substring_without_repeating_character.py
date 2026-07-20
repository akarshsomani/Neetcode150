class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0 :
            return 0 

        i = 0
        j = 1

        st = set()
        st.add(s[0])
        max_length = 1

        while(i <= j and j < len(s)):
            if ( s[j] in st ):
                st.remove(s[i])
                i += 1
            else:
                st.add(s[j])
                max_length = max(max_length, len(st))
                j += 1
        
        return max_length
    

s = Solution()
print("Length of longest substring without repeating characters : ", s.lengthOfLongestSubstring("abcabcbb")) # Output: 3