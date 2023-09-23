"""Write a Python program that concatenates all elements in a list into a string and returns it."""

def concat(list):
    result = ""
    for ele in list:
        result += ele
    return result

if __name__ == "__main__":
    list = input("\n Enter different elements seperated by a comma: ").split(",")

    print("\n Result: ",concat(list))
    