# 最长递增子数列
import bisect
nums = [4, 10, 4, 3, 8, 2, 9, 10]
      # 8
      #[1, 1, 1, 1, 1, 1, 1, 1]
      # [1, 2, 1, 1, 2, 1, 3, 4]


class Solution:
    def lenofLIS(self, nums):
        if not nums:
            return 0
        n = len(nums)

        memo = [1] * n
        for j in range(1, n):
            for i in range(j):

                if nums[j] > nums[i]:
                    memo[j] = max(memo[i] + 1, memo[j])

        return max(memo)

    def lenofLIS1(self, nums):
        lst = []
        for num in nums:
            p = bisect.bisect_left(lst, num)

            if p == len(lst):
                lst.append(num)
            else:
                lst[p] = num
        return len(lst)

s = Solution()
r = s.lenofLIS(nums)
print(r)

# r1 = s.lenofLIS1(nums)
# print(r1)
