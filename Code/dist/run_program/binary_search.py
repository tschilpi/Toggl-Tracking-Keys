import random
import math

numbers = random.sample(range(1, 100000), 10000)
numbers.sort()

low = 0
high = len(numbers)-1

# def binary_search(arr, x, low, high):
#
#     if arr[low] == x or arr[high] == x:
#         return arr.index(x)
#
#     if round((low+high)/2) == low or round((low+high)/2) == high:
#         return("Not in Array.")
#
#     elif arr[round((low+high)/2)] == x:
#         return arr.index(x)
#
#     elif x < arr[round((low+high)/2)]:
#         return binary_search(arr, x, low, high=round((low+high)/2))
#
#     elif x > arr[round((low+high)/2)]:
#         return binary_search(arr, x, low=round((low+high)/2), high=high)


def binary_search(arr, x, low, high):

    if low>high:
        return("Not in Array.")

    elif arr[math.floor((low+high)/2)] == x:
        return arr.index(x)

    elif x < arr[math.floor((low+high)/2)]:
        return binary_search(arr, x, low, high=math.floor(((low+high)/2)-1))

    elif x > arr[math.floor((low+high)/2)]:
        return binary_search(arr, x, low=math.floor((low+high)/2)+1, high=high)


k = 0
for x in numbers:
    print(binary_search(numbers, x, low, high))
    k +=1

print(k)

print(binary_search(numbers, 4911, low, high))