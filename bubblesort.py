# coding:utf-8


# 算法思路：每一次循环，把最大的放到最后面
def bubble_sort1(l):
    if len(l) == 1:
        return l
    for i in xrange(len(l)):
        for j in xrange(0, len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


# 算法思路：每一次循环，把最小的放到最前面
def bubble_sort2(lists):
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


l = [5, 4, 3, 2, 1]
res = bubble_sort1(l)

print res
