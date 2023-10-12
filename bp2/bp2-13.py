#!/usr/bin/python3

"""Write a Python program to get all possible two-digit letter combinations from a 1-9 digit string.
string_maps = {
"1": "abc",
"2": "def",
"3": "ghi",
"4": "jkl",
"5": "mno",
"6": "pqrs",
"7": "tuv",
"8": "wxy",
"9": "z"
}

Example - For "29", possible letter combinations based on string map: ['dz', 'ez', 'fz']
          For "47", ['jt', 'ju', 'jv', 'kt', 'ku', 'kv', 'lt', 'lu', 'lv'] """

def permutation(list):
    if len(list) == 0:
        return []
    
    if len(list) == 1:
        return [list]
    
    perm_list = []

    for i in range(len(list)):
        m = list[i]

        remList = list[:i] + list[i+1:]

        for p in permutation(remList):
            perm_list.append([m] + p)

    return perm_list

if __name__ == "__main__":
    string_maps = {
                    "1": "abc",
                    "2": "def",
                    "3": "ghi",
                    "4": "jkl",
                    "5": "mno",
                    "6": "pqrs",
                    "7": "tuv",
                    "8": "wxy",
                    "9": "z"
                   }
    
    print(f" Using the following string maps: \n {string_maps}")

    num = input("\n Enter a number: ")

    str1 = string_maps[num[0]]
    str2 = string_maps[num[1]]

    result = []
    for ele1 in str1:
        for ele2 in str2:
            perm_list = permutation([ele1, ele2])
            for ele_list in perm_list:
                str = ele_list[0] + ele_list[1]
                if str not in result and str[::-1] not in result:
                    result.append(str)
            
    print(f"\n All possible two-digit letter combinations for {num}: \n\n {result}")
