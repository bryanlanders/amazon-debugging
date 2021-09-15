# Amazon OA : Reverse Alphabet Chars Only

# The following function returns a string representing the reversed string in such a way that the position fo the special chars are not affected.
# The following code compiles successfully but fails to return the desired result. Your task is to fix the code so that it passes all test cases.

# Solve the problem:

def reverseAlphabetCharsOnly(inputString: str) -> str:
    inputChar = list(inputString)
    right = len(inputString) - 1
    left = 0
    while left < right:
        if not inputChar[left].isalpha():
            left = left + 1
        elif not inputChar[right].isalpha():
            right = right - 1
        else:
            temp = inputChar[left]
            inputChar[left] = inputChar[right]
            inputChar[right] = temp
        left = left + 1
        right = right - 1
    return ''.join(inputChar)
