from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        pre = [0] * n
        post = [0] * n

        pre[0] = height[0]
        for i in range(1, n):
            pre[i] = max(pre[i - 1], height[i])

        post[n - 1] = height[n - 1]
        for j in range(n - 2, -1, -1):
            post[j] = max(post[j + 1], height[j])

        total = 0
        for i in range(n):
            total += max(0, min(pre[i], post[i]) - height[i])

        return total


s = Solution()
print(s.trap([0, 2, 0, 3, 1, 0, 1, 3, 2, 1]))