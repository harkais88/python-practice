"""Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}"""

if __name__ == "__main__":
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])

    # for ele in color_list_1:
    #     if ele not in color_list_2:
    #         print(ele,end=" ")

    print(color_list_1.difference(color_list_2))