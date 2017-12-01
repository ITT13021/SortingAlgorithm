# coding:utf-8


# 算法思路： 通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序
# 1. key = list[left]
# 2. 先找right比key小的，交换数据
# 3. 再找left比key大的，交换数据
# 4. 直到left==right时，此时分为两个数组，再次进行快速排序
def quick_sort(lists, left, right):
    if left > right:
        return lists

    low = left
    high = right
    key = lists[left]

    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left], lists[right] = lists[right], lists[left]
        while left < right and lists[left] <= key:
            left += 1
        lists[left], lists[right] = lists[right], lists[left]
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists


l = [5, 4, 3, 2, 1]
res = quick_sort(l, 0, 4)

print res
