"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    """
    按照正常的口算方式进行计算和填补位置
    :param l1:
    :param l2:
    :return:
    """
    result = None
    before_node = None
    carry = 0
    while l1 is not None or l2 is not None:
        num1 = l1.val
        num2 = l2.val
        if num1 is None:
            num1 = 0
        if num2 is None:
            num2 = 0
        sum_ = num1 + num2 + carry  # 位数相加，并加上次计算得出的进位数
        carry = sum_ // 10  # 进位数
        curr = sum_ % 10  # 计算结果当前位置值
        curr_node = ListNode(curr)
        if before_node is None:
            result = curr_node
        else:
            before_node.next = curr_node
        before_node = curr_node

        l1 = l1.next
        l2 = l2.next
    return result


if __name__ == '__main__':
    print(1 // 10)
    print(1 % 10)
    node1 = ListNode(2)
    node1.next = ListNode(4)
    node1.next.next = ListNode(3)

    node2 = ListNode(5)
    node2.next = ListNode(6)
    node2.next.next = ListNode(4)

    numbers = add_two_numbers(node1, node2)
    print(numbers)
