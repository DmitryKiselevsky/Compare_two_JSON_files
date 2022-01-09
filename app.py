#-------------------------------------------------------------------------------
# Name:        app
# Purpose:
#
# Author:      Kiselevsky Dmitry
#
# Created:     07.01.2022
# Copyright:   (c) Kiselevsky Dmitry 2022
# Licence:     WTFPL
#-------------------------------------------------------------------------------
import sys

def main():
    pass

if __name__ == '__main__':
    main()

if len(sys.argv) != 3:
    exit("Not enough files!")

index = 1

def parse_json(string):
    global index
    field = ""
    value = ""
    field_parse_mode = True
    value_parse_mode = False
    res = {}
    while index < len(string):
        if string[index] == "\n":
            index += 1
            continue
        if string[index] == "{":
            index += 1
            res[field] = parse_json(string)
            field_parse_mode = True
            value_parse_mode = False
            field = ""
            value = ""
            continue
        if string[index] == "}":
            if field != "" and value != "":
                res[field] = value.strip().strip("\"")
            index += 1
            return res
        if string[index] == ":":
            field = field.strip().strip("\"")
            field_parse_mode = False
            value_parse_mode = True
            index += 1
            continue
        if string[index] == ",":
            res[field] = value.strip().strip("\"")
            field_parse_mode = True
            value_parse_mode = False
            field = ""
            value = ""
            index += 1
            continue
        if field_parse_mode:
            field += string[index]
            index += 1
        if value_parse_mode:
            value += string[index]
            index += 1
    return res

def recursive_read(d: dict):
    res = []
    for key, val in d.items():
        if type(val) == dict:
            res += recursive_read(val)
        res.append(str(key))
    return res


def compare_for_two(d1, d2):
    first_file = recursive_read(d1)
    secnd_file = recursive_read(d2)
    if len(first_file) != len(secnd_file):
        print("Not equal number of fields!")
    for f in first_file:
        if f not in secnd_file:
            print("First file content not equal field " + f)
    for f in secnd_file:
        if f not in first_file:
            print("Second file content not equal field " + f)


print(sys.argv[1] + " and " + sys.argv[2])
f1 = open('File-A.json','r', encoding='utf-8-sig')
f2 = open('File-B.json','r', encoding='utf-8-sig')

s1 = f1.read()
s2 = f2.read()

dict1 = parse_json(s1)
index = 1
dict2 = parse_json(s2)

compare_for_two(dict1, dict2)

f1.close()
f2.close()

