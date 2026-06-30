class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s = set(nums)
        print("set = ", s)

        max_count = 0

        for n in nums:
            if n-1 not in s:
                flag = True
                val = n + 1
                count = 1
                while(flag):
                    if val in s:
                        count += 1
                        val += 1
                    else:
                        flag = False

                max_count = max(max_count, count)
        return max_count


s  = Solution()
result = s.longestConsecutive([100, 4, 200, 1, 3, 2])

print(result)