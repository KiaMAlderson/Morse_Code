morse = [".-  ", "-...  ", "-.-.  ", "-..  ", ".  ",
         "..-.  ", "--.  ", "....  ", "..  ", ".---  ",
         "-.-  ", ".-..  ", "--  ", "-.  ", "---  ",
         ".--.  ", "--.-  ", ".-.  ", "...  ", "-  ",
         "..-  ", "...-  ", ".--  ", "-..-  ", "-.--  ", "--..  "]


def main():
    englishString = input('Enter an English string : ')
    result = ""

    for char in englishString:
        if (char.isnumeric()):
            result += numToMorse(char) 
        elif (char == " "):
            result += " /  "
        elif (char.isalpha()):
            letter = charToIndex(char.lower())
            result += morse[letter-1]
        else :
            result += char
            result += "  "

    print(englishString, "  :  " ,result)
    

def charToIndex(caseChar):
    switch = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4,
              'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8,
              'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12,
              'm' : 13, 'n' : 14, 'o' : 15, 'p' : 16,
              'q' : 17, 'r' : 18, 's' : 19, 't' : 20,
              'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24,
              'y' : 25, 'z' : 26}

    return switch.get(caseChar)

def numToMorse(number):
    switch = {'1' : ".----  ", '2' : "..---  ", '3' : "...--  ",
              '4' : "....-  ", '5' : ".....  ", '6' : "-....  ",
              '7' : "--...  ", '8' : "---..  ", '9' : "----.  ",
              '0' : "-----  "}

    return switch.get(number)


main()
