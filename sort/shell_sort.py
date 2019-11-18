"""
希尔排序
"""


def shell_sort(l):
    gap = int(len(l) / 2)  # 分区内的元素个数
    while 1 <= gap:
        l_gap = int(len(l) / gap)  # 计算分区个数，按照分区进行遍历
        for i in range(l_gap):  # 区间遍历
            start = i * gap
            end = (i + 1) * gap
            if i == l_gap - 1 or i == len(l):  # 区间划分过程
                end = len(l) - 1
            if i == len(l) - 1:
                start = 0
            for j in range(start + 1, end):  # 区间内直接插入排序
                for z in range(j - 1, start - 1, -1):
                    if l[z + 1] > l[z]:
                        break
                    else:
                        temp = l[z + 1]
                        l[z + 1] = l[z]
                        l[z] = temp
            if i == len(l):  # 区间跳出
                break
        gap = int(gap / 2)
    return l


if __name__ == '__main__':
    arr = [7, 3, 4, 8, 1, 10]
    print(shell_sort(arr))
