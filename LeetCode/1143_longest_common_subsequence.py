"""
Solution for 1143. Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence/
"""

class Solution:
    """
    Runtime: 408 ms, faster than 58.59% of Python3 online submissions for Longest Common Subsequence.
    Memory Usage: 22.6 MB, less than 100.00% of Python3 online submissions for Longest Common Subsequence.
    """
    def longestCommonSubsequence(self, text1, text2):
        """
        Given two strings text1 and text2, return the length of their longest common subsequence.

        A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.



        If there is no common subsequence, return 0.



        Example 1:

        Input: text1 = "abcde", text2 = "ace"
        Output: 3
        Explanation: The longest common subsequence is "ace" and its length is 3.
        Example 2:

        Input: text1 = "abc", text2 = "abc"
        Output: 3
        Explanation: The longest common subsequence is "abc" and its length is 3.
        Example 3:

        Input: text1 = "abc", text2 = "def"
        Output: 0
        Explanation: There is no such common subsequence, so the result is 0.


        Constraints:

        1 <= text1.length <= 1000
        1 <= text2.length <= 1000
        The input strings consist of lowercase English characters only.
        Args:
            text1: str value
            text2: str value

        Returns:
            int:
        """
        if not text1 or not text2:
            return 0
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[-1][-1]
