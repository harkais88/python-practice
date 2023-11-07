#!/usr/bin/python3

"""Write a Python program to find the name of the oldest student in a given dictionary 
containing the names and ages of a group of students.
Sample Input:
{"Bernita Ahner": 12, "Kristie Marsico": 11, "Sara Pardee": 14, "Fallon Fabiano": 11, "Nidia Dominique": 15}
{"Nilda Woodside": 12, "Jackelyn Pineda": 12.2, "Sofia Park": 12.4, "Joannie Archibald": 12.6, "Becki Saunder": 12.7}
Sample Output:
Nidia Dominique
Becki Saunder"""

def getOldest(dict):
    return max(dict, key = dict.get)

if __name__ == "__main__":
    print(getOldest(
        {"Bernita Ahner": 12, "Kristie Marsico": 11, "Sara Pardee": 14, "Fallon Fabiano": 11, "Nidia Dominique": 15}))
    print(getOldest(
        {"Nilda Woodside": 12, "Jackelyn Pineda": 12.2, "Sofia Park": 12.4, "Joannie Archibald": 12.6, "Becki Saunder": 12.7}
    ))