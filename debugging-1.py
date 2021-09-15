# Amazon OA : Calculate Sum Of Numbers In String

# The following function returns a positive integer representing the sum of numbers in the inputString.
# The following code compiles successfully but fails to return the desired result. Your task is to fix the code so that it passes all test cases.

# Solve the problem:


def calculateSumOfNumbersInString(inputString: str) -> int:
    temp = ""
    sum = 0
    for i in range(0, len(inputString)):
        ch = inputString[i]
        if ch.isdigit():
            temp += ch
        else:
            sum += int(temp)
        temp = "0"

    return sum + int(temp)
