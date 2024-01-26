from typing import List

def lengthOfLIS(nums: List[int]) -> int:
        n = len(nums)
        substr = []

        # Generate all possible subsequences
        for num in range(1 << n):
            sub = [nums[i] for i in range(n) if num & (1 << i)]
            substr.append(sub)

        # Filter valid increasing subsequences
        increasing_subsequences = [subseq for subseq in substr if all(subseq[i] < subseq[i+1] for i in range(len(subseq)-1))]
        print("increasing subsequences",increasing_subsequences)

        # Find the longest increasing subsequence based on the length of subsequences
        longest_increasing_subsequence = max(increasing_subsequences, key=len, default=[])

        # Return the length of the Longest Increasing Subsequence
        print("Longest Subsequence is ",longest_increasing_subsequence)
        return len(longest_increasing_subsequence)

# Ask the user to input a list of integers
input_nums_str = input("Enter a list of integers:\n")
# input_nums = [int(num) for num in input_nums_str.split()] wrong
# Parse the input string into a list of integers
input_nums = [int(num) for num in input_nums_str.replace("[", "").replace("]", "").split(",")]

print("Length of the longest increasing subsequence is ",lengthOfLIS(input_nums))
