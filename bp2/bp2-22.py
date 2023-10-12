#!/usr/bin/python3

"""Write a Python program to find the number of notes (Samples of notes: 10, 20, 50, 100, 200, 500) 
against an amount.
Range - Number of notes(n) : n (1 <= n <= 1000000)."""

def countNotes(num):
    notes = [[500, 0], [200, 0], [100, 0], [50, 0], [20, 0], [10, 0], [1, 0]]

    while num != 0:
        for i in range(len(notes)):
            if num % notes[i][0] == 0:
                note_index = i
                break

        notes[note_index][1] += 1
        num -= notes[note_index][0]

    return notes

if __name__ == "__main__":
    # Sample Output
    # Number of notes required for Rs. 999999: 1998 500s, 4 200s, 1 100s, 0 50s, 4 20s, 1 10s and 9 1s
    notes = countNotes(999999)
    print("\n Number of notes required for Rs. {}: {} 500s, {} 200s, {} 100s, {} 50s, {} 20s, {} 10s and {} 1s".format(
        999999, notes[0][1], notes[1][1], notes[2][1], notes[3][1], notes[4][1], notes[5][1], notes[6][1]
    ))

    # # For extensive results, writing the full output to a file
    # # This will obviously take some time
    # from os.path import expanduser, join
    # file = open(join(expanduser("~"), "Desktop\\test"),"w")
    # for i in range(1,1000001):
    #     notes = countNotes(i)

    #     file.write("\n Number of notes required for Rs. {}: {} 500s, {} 200s, {} 100s, {} 50s, {} 20s, {} 10s and {} 1s".format(
    #     i, notes[0][1], notes[1][1], notes[2][1], notes[3][1], notes[4][1], notes[5][1], notes[6][1]
    # ))
    # print("File Written Successfully")
    # file.close()