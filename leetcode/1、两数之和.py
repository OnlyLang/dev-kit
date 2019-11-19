"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的
那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
"""


def sum1(arr, target):
    """
    不能重复利用，
    这里的思维是：遍历数组，将数组需要用到的值记录下来
    如果发现新遍历的值在需求记录中存在，那么
    :param arr:
    :param target:
    :return:
    """
    map = {}
    for i in range(len(arr)):
        need = target - arr[i]
        if i != 0:
            if arr[i] in map:
                return [map[arr[i]], i]
        map[need] = i
    return [-1, -1]


if __name__ == '__main__':
    arr = [2, 7, 9, 11, 8]
    result = sum1(arr, 10)
    print(result)
