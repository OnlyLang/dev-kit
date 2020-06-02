"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def judge_palindrome(string, start=0, end=None):
    """
    判断是否为回文串
    :param string:
    :param start:
    :param end:
    :return:
    """
    if end is None:
        end = len(string) - 1
    if start >= end:
        return True
    c1 = string[start]
    c2 = string[end]
    if c1 == c2:
        return judge_palindrome(string, start + 1, end - 1)
    else:
        return False


def longest_palindrome(string):
    """
    暴力查找最长回文子串
    :param string:
    :return:
    """
    if len(string) < 2:
        return -1
    max_len = 0
    max_str = ""
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            temp_str = string[i:j + 1]
            if judge_palindrome(temp_str):
                if len(temp_str) > max_len:
                    max_str = temp_str
                    max_len = len(temp_str)
    return max_str


def longest_palindrome2(string):
    """
    利用动态规划来进行回文字符串的判断
    :param string:
    :return:
    """


if __name__ == '__main__':
    print(longest_palindrome("1中国12321国中12"))
