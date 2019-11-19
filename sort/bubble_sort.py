"""
冒泡排序
"""


def bubble_sort(l):
    for i in range(len(l) - 1):  # 比较的轮数控制
        for j in range(0, len(l) - (i + 1)):  # 实际比较，将大数放到最后
            if l[j] > l[j + 1]:
                temp = l[j + 1]
                l[j + 1] = l[j]
                l[j] = temp
    return l


if __name__ == '__main__':
    arr = [7, 3, 4, 8, 1, 10, 9]
    print(bubble_sort(arr))
