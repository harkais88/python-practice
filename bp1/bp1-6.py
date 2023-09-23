"""Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')"""

if __name__ == "__main__":
    list = input("\n Enter a few numbers seperated by commas: ").split(",")
    print("\n List: ",list)
    print("\n Tuple: ",tuple(list))
