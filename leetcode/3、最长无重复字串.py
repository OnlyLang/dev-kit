"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def longest_substring(string):
    """
    利用一个字典来记录之前已经出现的值的位置
    :param string:
    :return:
    """
    map_ = dict()
    start = 0
    max_ = 0
    for i in range(len(string)):
        curr = string[i]
        if curr in map_ and map_[curr] >= start:
            curr_length = i - start
            if curr_length > max_:
                max_ = curr_length
            start = map_[curr] + 1
        if i == len(string) - 1:
            curr_length = i - start
            if curr_length > max_:
                max_ = curr_length
        map_[curr] = i
    return max_


if __name__ == '__main__':
    substring = longest_substring("abcabcbb")
    print(substring)
