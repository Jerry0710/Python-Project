class Solution:
    # 实现 strStr() 函数。
    #
    # 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
    #
    # 示例 1:
    #
    # 输入: haystack = "hello", needle = "ll"
    # 输出: 2
    # 示例 2:
    #
    # 输入: haystack = "aaaaa", needle = "bba"
    # 输出: -1
    #
    def strStr(self, haystack: str, needle: str) -> int:
        N, M = len(haystack), len(needle)
        if M == 0:
            return 0
        next_KMV = [-1]
        i, j = 0, -1  # 初始时，j=-1要比i小1；若j=0,则i=1,当M=1时needle[i]报错
        while i < M:
            if (j == -1) | (needle[i] == needle[j]):  # j=-1时表示进入下一位比较
                i += 1
                j += 1
                next_KMV.append(j)
            else:
                j = next_KMV[j]       # 核心（如果不匹配，找之前能匹配到的最大值）
        j = 0
        for i in range(N):
            while (haystack[i] != needle[j]) & (j != 0):
                j = next_KMV[j]
            if haystack[i] == needle[j]:
                j += 1
            if j == M:
                return i-j+1
        return -1

s = Solution()
index = s.strStr('aabaaabaaac', 'aabaaac')
print(index)