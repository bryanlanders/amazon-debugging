# Amazon OA : Check Pair Sum Exists

# The following function returns a boolean value representing if there is a pair with given sum exists in the array.
# The following code compiles successfully but fails to return the desired result. Your task is to fix the code so that it passes all test cases.

# Solve the problem:

def checkPairSumExists(rows: int, cols: int, arr: List[List[int]], sum: int) -> bool:
    localSet = set()
    for i in range(0, rows):
        for j in range(0, cols):
            if sum - arr[i][j] in localSet:
                return True
            else:
                localSet.add(sum)
    return False
