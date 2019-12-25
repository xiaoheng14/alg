# 动态规划求最长回文字符串
class MaxPalindromeString:
    def __init__(self):
        self.start_index = None
        self.array_len = None

    def get_longest_palindrome(self, s):
        if not s:
            return

        size = len(s)
        if size < 1:
            return
        self.start_index = 0
        self.array_len = 1
        # 保存历史记录
        history_record = [([0] * size) for _ in range(size)]

        # 初始化长度为1的回文字符串信息
        for i in range(size):
            history_record[i][i] = 1

        # 初始化长度为2的回文字符串信息
        for i in range(size - 1):
            if s[i] == s[i + 1]:
                history_record[i][i+1] = 1
                self.start_index = i
                self.array_len = 2

        # 查找从长度为3开始的回文字符串
        p_len = 3
        while p_len <= size:
            i = 0
            while i < size - p_len + 1:
                j = i + p_len - 1
                if s[i] == s[j] and history_record[i + 1][j - 1] == 1:
                    history_record[i][j] = 1
                    self.start_index = i
                    self.array_len = p_len
                i += 1
            p_len += 1
        return self.start_index, self.array_len


s = 'abcba'
p = MaxPalindromeString()
st, le = p.get_longest_palindrome(s)
print(st, le)
if st is not None:
    print(s[st: st + le])
