#!/usr/bin/python3

"""Write a Python program that accepts six numbers as input and sorts them in descending order.
Input:
Input consists of six numbers n1, n2, n3, n4, n5, n6 (-100000 <= n1, n2, n3, n4, n5, n6 <= 100000). 
The six numbers are separated by a space.
Input six integers:
15 30 25 14 35 40
After sorting the said integers:
40 35 30 25 15 14"""

# There are way too many ways to do this, from the naive ways to the most intricate ways
# Some of these sorting algorithms will be implemented here
# Note that these algorithms are for descending order fashion, but if concept is understood,
# you can easily tweak them to ascending order

# A good reference site: https://www.geeksforgeeks.org/sorting-algorithms/

# Using Bubble Sort
# Time Complexity: O(N^2)
# def sort(list):
#     for i in range(len(list)-1,-1,-1):
#         for j in range(i-1,-1,-1):
#             if list[j] < list[i]:
#                 # Swapping the elements
#                 list[i] = list[j] + list[i]
#                 list[j] = list[i] - list[j]
#                 list[i] = list[i] - list[j]
#     return list

# Using Insertion Sort
# Time Complexity: O(N^2)
# def sort(list):
#     for i in range(len(list)-2,-1,-1):
#         key = list[i]
#         j = i + 1

#         while j <= len(list)-1 and list[j] > key:
#             list[j-1] = list[j]
#             j += 1

#         list[j-1] = key
#     return list     

# Using Selection Sort
# Time Complexity: O(N^2)
# def sort(list):
#     # ONE WAY TO DO IT IN DESCENDING

#     # for i in range(len(list)-1,0,-1):
#     #     min = i
#     #     for j in range(i-1,-1,-1):
#     #         if list[j] < list[min]:
#     #             min = j
#     #     # Swapping element at positions i and min
#     #     list[min] = list[i] + list[min]
#     #     list[i] = list[min] - list[i]
#     #     list[min] = list[min] - list[i]

#     # ANOTHER WAY TO DO IT IN DESCENDING
#     for i in range(len(list)-1):
#         max = i
#         for j in range(i+1,len(list)):
#             if list[j] > list[max]:
#                 max = j
#         # Swapping element at positions i and max
#         list[max] = list[i] + list[max]
#         list[i] = list[max] - list[i]
#         list[max] = list[max] - list[i]

#     return list 

# Using Merge Sort
# Time Complexity: O(NlogN)
# def sort(list):
#     if len(list) > 1:
#         mid = len(list) // 2

#         L = list[:mid]
#         R = list[mid:]

#         L = sort(L)
#         R = sort(R)

#         # ONE WAY TO DO IT IN DESCENDING
#         # i = len(L) - 1
#         # j = len(R) - 1
#         # k = len(list) - 1

#         # while i >= 0 and j >= 0:
#         #     if L[i] < R[j]:
#         #         list[k] = L[i]
#         #         i -= 1
#         #     if L[i] > R[j]:
#         #         list[k] = R[j]
#         #         j -= 1
#         #     k -= 1

#         # while i >= 0:
#         #     list[k] = L[i]
#         #     i -= 1
#         #     k -= 1
#         # while j >= 0:
#         #     list[k] = R[j]
#         #     j -= 1
#         #     k -= 1

#         # ANOTHER WAY TO DO IT IN DESCENDING
#         i = j = k = 0

#         while i < len(L) and j < len(R):
#             if L[i] > R[j]:
#                 list[k] = L[i]
#                 i += 1
#             elif L[i] < R[j]:
#                 list[k] = R[j]
#                 j += 1
#             k += 1

#         while i < len(L):
#             list[k] = L[i]
#             i += 1
#             k += 1

#         while j < len(R):
#             list[k] = R[j]
#             j += 1
#             k += 1

#     return list

# Using QuickSort
# Time Complexity: O(NlogN) at best and average cases, O(N^2) in worst case
def sort(list):
    if len(list) > 1:
        pivot = len(list) - 1 # Considering last element as pivot
        i = -1
        j = 0

        while j != pivot:
            if list[j] > list[pivot]:
                i += 1
                # Swapping elements at positions i and j
                list[i],list[j] = list[j],list[i]
            j += 1
        # Swapping elements at positions i+1 and pivot
        i += 1
        list[i], list[pivot] = list[pivot], list[i]

        list = sort(list[:i]) + [list[i]] + sort(list[i+1:])
    return list

# Bonus: Check out the other sorting algorithms!

if __name__ == "__main__":
    print("Input consists of six numbers n1, n2, n3, n4, n5, n6 (-100000 <= n1, n2, n3, n4, n5, n6 <= 100000).")
    print("The six numbers are separated by a space.")
    list = [int(i) for i in input("Input six integers:\n").split()]
    print("After sorting the said integers:")
    print(" ".join(str(ele) for ele in sort(list)))