"""
k 值计算
"""


def get_k(arr1, start1, arr2, start2, k):
    len1 = len(arr1) - start1
    len2 = len(arr2) - start2

    if len1 > len2:  # 保证如果有一个数组排除完时，肯定是第一个数组
        return get_k(arr2, start2, arr1, start1, k)
    if len1 == 0:
        return arr2[start2 + k - 1]  # 数组一已经排除完，那么就直接从数组二中取值
    if k == 1:
        return min(arr1[start1], arr2[start2])

    # 以下为 ：正常排除
    # 计算k的值,和当前k为止的值的比较，长度和 k/2 之间的选择
    i = start1 + min(len1, int(k / 2)) - 1
    j = start2 + min(len2, int(k / 2)) - 1

    if arr1[i] > arr2[j]:
        # 此时的k值为 减去排除后的值的位置开始算起
        return get_k(arr1, start1, arr2, j + 1, k - (j - start2 + 1))
    else:
        return get_k(arr1, i + 1, arr2, start2, k - (i - start1 + 1))


def get_k2(arr1, arr2, k):
    if len(arr1) > len(arr2):
        return get_k2(arr2, arr1, k)
    if len(arr1) == 0:
        return arr2[k - 1]
    if k == 1:
        return min(arr1[k - 1], arr2[k - 1])

    i = min(len(arr1), int(k / 2)) - 1
    j = min(len(arr2), int(k / 2)) - 1

    if arr1[i] > arr2[j]:
        return get_k2(arr1, arr2[j + 1:], k - j - 1)
    else:
        return get_k2(arr1[i + 1:], arr2, k - i - 1)


if __name__ == '__main__':
    arr1 = [1, 3, 5, 7, 9, 11, 13]
    arr2 = [2, 3, 4]
    print("1:" + str(get_k(arr1, 0, arr2, 0, 6)))
    # print(arr1[3:])
    print("2:" + str(get_k2(arr1, arr2, 6)))
