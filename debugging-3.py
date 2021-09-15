# Amazon OA : Remove Consecutive Vowels

# The following function returns a string value representing the string left after removing consecutive vowels from the string.
# The following code compiles successfully but fails to return the desired result. Your task is to fix the code so that it passes all test cases.

# Solve the problem:

def is_vowel(ch):
    return (ch == 'a') or (ch == 'e') \
           or (ch == 'i') or (ch == 'o') \
           or (ch == 'u')

def removeConsecutiveVowels(inputString: string) -> string:
    str1 = "" + inputString[0]
    for i in range(1, len(inputString)):
        if (not is_vowel(inputString[i - 1])) and \
                (not is_vowel(inputString[i])):
            ch = inputString[i]
            str1 = str1 + ch
    return str1
