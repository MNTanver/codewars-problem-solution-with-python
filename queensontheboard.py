# Your task is to find the maximum number of queens that can be put on the board so that there would be one single unbeaten square (ie. threatened by no queen on the board).

# The Queen can move any distance vertically, horizontally and diagonally.
# Input

# The queens(n) function takes the size of the chessboard.

# n∈Z, so it can be negative, and values can go up to 1411000141^{1000}1411000.
# Output

#     The maximum number of queens to leave one single unbeaten square
#     Return 0 if n is negative.

# Examples

#     n=4→6  n=4→6 queens
#     n=5→12   n=5→12 queens

# Good luck )

def queens(n):
    if n < 3:
        return 0
    else:
        return (n - 1) * (n - 2)

# This code defines a Python function called queens that takes an integer input n. The purpose of this function is to calculate the maximum number of queens that can be placed on a chessboard of size n x n such that there is exactly one square on the board that is not threatened by any queen.

# Here's a step-by-step explanation of the code:

#     The function begins with an if statement to handle the case where n is less than 3. If n is less than 3, it means that it's not possible to place any queens on the board while satisfying the condition of having one unbeaten square. In this case, the function returns 0.

#     If n is greater than or equal to 3, the else block is executed.

#     In the else block, the code calculates the maximum number of queens that can be placed on the n x n chessboard while leaving exactly one square unbeaten. The formula used for this calculation is:

#     (n - 1) * (n - 2)

#     This formula is derived from the observation that if you place queens in a way that they occupy all rows and columns except one row and one column (leaving those two for the unbeaten square), you can maximize the number of queens. So, the (n - 1) part represents the number of queens placed in rows, and (n - 2) represents the number of queens placed in columns. The product of these two values gives the maximum number of queens that satisfy the condition.

#     The calculated value is returned as the result of the function.

# In summary, the queens function calculates and returns the maximum number of queens that can be placed on a chessboard of size n x n while ensuring that there is exactly one square that is not threatened by any queen. If n is less than 3, it returns 0 because it's not possible to satisfy the condition in that case.