class Solution:
    def misDistance(self, word1, word2):
        m = len(word1) + 1
        n = len(word2) + 1
        dp = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            dp[i][0]=i
        for j in range(n):
            dp[0][j]=j

        for i in range(1, m):
            for j in range(1, n):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 插入、删除、替换
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1

        return dp[m-1][n-1]

def editdis(str1, str2):
	len_str1 = len(str1) + 1
	len_str2 = len(str2) + 1
	matrix = [0 for n in range(len_str1 * len_str2)]
	for i in range(len_str1):
		matrix[i]=i
	for j in range(0, len(matrix), len_str1):
		if j % len_str1 == 0:
			matrix[j] = j

	for i in range(1, len_str1):
		for j in range(1, len_str2):
			if str1[i-1] == str2[j-1]:
				cost = 0
			else:
				cost = 1
			matrix[j*len_str1+i] = min(matrix[(j-1) * len_str1 + i] + 1, matrix[j*len_str1 + (i-1)]+1, matrix[(j-1)*len_str1+(i-1)]+cost)
	return matrix[-1]

if __name__ == "__main__":
    word1 = input("word1:")
    word2 = input("word2:")
    solution = Solution()
    print("The min distance is: \n1. DP method: ", solution.misDistance(word1, word2))
    print("2. another method: ", editdis(word1, word2))