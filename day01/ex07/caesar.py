import os
import sys

def caesar(code, word, key):
    if code == 'encode':
        sign = 1
    elif code == 'decode':
        sign = -1
    else:
        print("Wrong 1st argument:\nThe firs argument has to be 'encode' or 'decode'")
        return
    for i in word:
        if i.islower() or i.isupper():
            value = (ord(i) + (sign)*key)
            if (value > ord('z') or value < ord('a')) and i.islower():
                value = value - (sign)*26
            if (value > ord('Z') or value < ord('A')) and i.isupper():
                value = value - (sign)*26
            print(chr(value), end="")
        elif 1040 < ord(i) < 1071:
            print("The script does not support your language yet.")
        else:
            print("Please write only english alphabet letters.")
    print("")

def main():
    if len(sys.argv) != 4:
        print("Incorrect number of arguments, maximum 3: code word key.")
        print("example: python3 caesar.py encode hello 12")
    else:
        word = str(sys.argv[2])
        for i in word:
            if 1040 < ord(i) < 1103:
                print("The script does not support your language yet.")
                return
            elif not i.islower or not i.isupper:
                print("Please write only english alphabet letters.")
                return

        if sys.argv[3].isdigit():
            key = int(sys.argv[3])
        else:
            print("wrong 3rd argument, plese write a number")
            return
        code = sys.argv[1]
        caesar(code, word, key)
if __name__=='__main__':
    main()
