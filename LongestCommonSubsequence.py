class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)+1
        m = len(text2)+1
        memo = [[0 for i in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if text1[j-1] == text2[i-1]:
                    memo[i][j] = 1 + memo[i-1][j-1]
                else:
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1])
        return memo[m-1][n-1]


    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def my_LCS(len1: int, len2: int) -> int:
            if len1==0 or len2==0:
                return 0
            cur_state = (len1, len2)
            if cur_state in memo:
                return memo[cur_state]
            if text1[len1-1] == text2[len2-1]:
                memo[cur_state] = 1 +  my_LCS(len1-1, len2-1)
            else: 
                memo[cur_state] = max(my_LCS(len1-1, len2), my_LCS(len1, len2-1))
            return memo[cur_state]
        memo = {}
        return my_LCS(len(text1), len(text2))