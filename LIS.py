from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        substr = []

        # Generate all possible subsequences
        for num in range(1 << n):
            sub = [nums[i] for i in range(n) if num & (1 << i)]
            substr.append(sub)

        # Filter valid increasing subsequences
        increasing_subsequences = [subseq for subseq in substr if all(subseq[i] < subseq[i+1] for i in range(len(subseq)-1))]

        # Find the longest increasing subsequence based on the length of subsequences
        longest_increasing_subsequence = max(increasing_subsequences, key=len, default=[])

        # Return the length of the Longest Increasing Subsequence
        print(longest_increasing_subsequence)
        return len(longest_increasing_subsequence)

# Example usage for LeetCode
solution_instance = Solution()

# LeetCode will provide inputs, and you process each test case
# The output will be automatically checked by LeetCode
# You don't need to manually create instances or ask for user input

# Example:
# input_nums_1 = [10, 9, 2, 5, 3, 7, 101, 18]
# output_1 = solution_instance.lengthOfLIS(input_nums_1)
# LeetCode will check if output_1 matches the expected result for the given input
