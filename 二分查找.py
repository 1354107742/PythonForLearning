#二分法必须查有序
lst = [22, 33, 44, 55, 66, 77, 88, 99, 101, 238, 345, 456, 567, 678, 789]
#常规思路
def func(n):
    right = len(lst) - 1
    left = 0
    middle = (left+right) // 2
    while left < right:
        if n > lst[middle]:
            left = lst[middle] + 1
        elif n < lst[middle]:
            right = lst[middle] - 1
        else:
            break
    return middle
print(func(101))
#递归思想
def func1(n, left, right):
    if left <= right:        
        middle = ( left + right ) // 2 
        if n > lst[middle]:
            left = middle + 1
        elif n < lst[middle]:
            right = middle - 1
        else:
            return middle
        return func1(n, left, right)
        
print(func1(101, 0, len(lst)-1))
