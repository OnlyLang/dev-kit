"""
直接插入排序
"""


def insert_sort(l):
    for i in range(1, len(l)):
        for j in range(i - 1, -1, -1):
            if l[j + 1] > l[j]:
                break
            else:
                temp = l[j]
                l[j] = l[j + 1]
                l[j + 1] = temp
    return l


if __name__ == '__main__':
    arr = [7, 3, 4, 8, 1, 10]
    print(insert_sort(arr))
