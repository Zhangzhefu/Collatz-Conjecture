# Solution 2
# This Solution utilizes the % symbol, which returns the remainder
# Any even number divided by 2 has a remainder of 0, and any odd number divided by 2 has a remainder of 1

value = int(input("pass in a positive integer: "))
if value <= 0:
    raise Exception("Must be positive!")  # check for positive value only
while value != 1:  
    if value % 2 == 0: # utilize the % symbol
        value = value // 2  
    else:
        value = value * 3 + 1  
      print(value)
print(str(value) + " is the final answer")
