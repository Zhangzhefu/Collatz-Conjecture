# Solution 1
# This solution utilize the fact that even numbers end in 02468

value = input("Pass in a positive integer: ")  # the starting value user enters
if value <= 0:
    raise Exception("Must be positive!")  # check if positive

while value != 1:
    last_digit = str(value)[-1]  # receive the last digit of variable value in string form

    if last_digit in "02468":   # check if even
        value = value // 2 
    else:
        value = value * 3 + 1  #

    print(value)  # Print the result at each step
