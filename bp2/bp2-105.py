#!/usr/bin/python3

"""Write a Python program to find a number in a given matrix that is maximum in its column and minimum in its row.
Sample Input:
Original matrix: [[1, 2], [2, 3]]
Number in the said matrix which is maximum in its column and minimum in its row:
[2]
Original matrix: [[1, 2, 3], [3, 4, 5]]
Number in the said matrix which is maximum in its column and minimum in its row:
[3]
Original matrix: [[7, 5, 6], [3, 4, 4], [6, 5, 7]]
Number in the said matrix which is maximum in its column and minimum in its row:
[5]"""

def getMinMax(matrix):
    return list(set(map(min,matrix)) & set(map(max,*matrix)))[0]

if __name__ == "__main__":
    print(getMinMax([[1,2], [2,3]]))
    print(getMinMax([[1, 2, 3], [3, 4, 5]]))
    print(getMinMax([[7, 5, 6], [3, 4, 4], [6, 5, 7]]))