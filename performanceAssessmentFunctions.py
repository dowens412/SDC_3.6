# This function prints the full Student ID.
def functionOne():
    print(f'My Student ID is DAVOWE9952')


# This function asks the user for two numbers, adds them,
# prints the sum, and returns the sum back to main().
def functionTwo():
    firstNum = int(input('Please enter a number: '))
    secondNum = int(input('Please enter a number: '))
    totalSum = firstNum + secondNum
    print(f'The sum of {firstNum} and {secondNum} is {totalSum}.')
    return totalSum


# This function accepts the sum from functionTwo().
# It checks whether the sum is greater than 5 or 5 or less,
# prints the correct message, and returns the numeric part of the Student ID.
def functionThree(sumValue):
    if sumValue > 5:
        print(f'The sum is greater than 5.')
    else:
        print(f'The sum is 5 or less.')

    return 9952


# This function prints the value returned from functionThree().
def functionFour(returnValue):
    print(f'functionThree returned the value of {returnValue}.')


# This is the main function that controls the program.
def main():
    # Call functionOne to display the Student ID.
    functionOne()

    # Call functionTwo and save the returned sum in a variable.
    sumValue = functionTwo()

    # Call functionThree, pass the sum, and save the returned numeric ID value.
    returnedValue = functionThree(sumValue)

    # Call functionFour to display the value returned from functionThree().
    functionFour(returnedValue)


# Call main() to start the program.
main()