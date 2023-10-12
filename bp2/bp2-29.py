#!/usr/bin/python3

"""Write a Python program to print the length of the series and the series from the given 3rd term, 
3rd last term and the sum of a series.
Sample Data:
Input third term of the series: 3
Input 3rd last term: 3
Input Sum of the series: 15
Length of the series: 5
Series:
1 2 3 4 5"""
 
if __name__ == "__main__":
    third = int(input("\n Enter the third term of the series: "))
    third_last = int(input("\n Enter the third last term of the series: "))
    sum = int(input("\n Enter the sum of the series: "))

    # Considering series to be AP
    number_of_terms = (2*sum) // (third + third_last)

    print("\n According to given input, there can be",number_of_terms," terms in the series")

    d = ((2*sum) - (third_last * number_of_terms)) // (2 * number_of_terms)

    print("\n Common Difference: ",d)
    a = third - (2*d)
    print("\n First Term: ",a)

    print("\n The Series: ",a,end = " ")

    for i in range(1,number_of_terms):
        print(a + (i*d), end = " ")