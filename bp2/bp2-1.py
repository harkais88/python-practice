#!/usr/bin/python3

"""Write a Python function that takes a sequence of numbers and determines whether 
all the numbers are different from each other."""

# One way to do it
# def chckSeq(nums):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i] == nums[j]:
#                 return False
#     return True

# Another way by using the Python way
def chckSeq(nums):
    return len(nums) == len(set(nums))

if __name__ == "__main__":
    nums1 = [9, 7, 5, 3, 3, 1, 4, 3, 1, 1]
    nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    print("\n Are all numbers different in {} : {}".format(nums1, "Yes" if chckSeq(nums1) else "No"))
    print("\n Are all numbers different in {} : {}".format(nums2, "Yes" if chckSeq(nums2) else "No"))


