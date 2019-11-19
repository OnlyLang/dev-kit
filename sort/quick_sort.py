"""
快速排序实现
"""


def quick_sort(l):
    if len(l) >= 2:
        mid = l[0]
        left, right = [], []
        l.remove(mid)
        for num in l:
            if num > mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return l


if __name__ == '__main__':
    arr = [7, 3, 4, 8, 1, 10, 9]
    print(quick_sort(arr))
