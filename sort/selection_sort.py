"""
简单选择排序
"""


def selection_sort(l):
    for i in range(len(l)):
        min_num = l[i]
        index = i
        for j in range(i + 1, len(l)):
            if l[j] < min_num:
                min_num = l[j]
                index = j
        l[index] = l[i]
        l[i] = min_num
    return l


if __name__ == '__main__':
    arr = [7, 3, 4, 8, 1, 10, 9]
    print(selection_sort(arr))
