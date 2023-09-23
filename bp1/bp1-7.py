"""Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java"""

# #Using the find function
# if __name__ == "__main__":
#     while True:
#         file = input("\n Enter the filename: ")

#         index = file.find(".")
    
#         if file[index+1:].find(".") == -1:
#             print("\n Extension: ",file[index+1:])
#             break
#         else:
#             print("\n Valid filename not given")

#Using the split function
if __name__ == "__main__":
    while True:
        file = input("\n Enter the filename: ").split(".")

        if len(file) == 2:
            print("\n Extension: ",file[-1])
            break
        else:
            print("\n Valid filename not given")