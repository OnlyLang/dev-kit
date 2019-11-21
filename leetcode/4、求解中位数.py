"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

25344.36
5747.13
则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from algorithm import k值计算 as k


def median(arr1, arr2):
    """
    通过k值计算方法进行计算
    :param arr1:
    :param arr2:
    :return:
    """
    # 计算k值
    k1 = int((len(arr1) + len(arr2) + 1) / 2)
    k2 = int((len(arr1) + len(arr2) + 2) / 2)
    return (k.get_k2(arr1, arr2, k1) + k.get_k2(arr1, arr2, k2)) * 0.5


if __name__ == '__main__':
    arr1 = [1, 3, 4]
    arr2 = [2]
    print(median(arr1, arr2))
