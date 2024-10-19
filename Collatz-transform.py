# This is a transformation of the original Collatz-conjecture question
# This solves math questions like: 
# If Bob writes the first n terms using the Collatz-Conjecture sequence and notices that the sum of these terms is a four-digit number. 
# How many different possible values of n are there?

# This can be modified to use for bigger or smaller numbers 

init_value = int(input("What is the starting value? ")

value = init_value
counter = init_value
count_term = 1

while counter < 1000:    # change this to make it 5 digits, 6 digits... {100, 1000, 10000}
    if value % 2 == 0:
        value = value // 2
    else:
        value = 3 * value + 1

    counter += value
    count_term += 1

print("the first 4 digit number is " + str(counter))


sec_value = init_value
sec_counter = init_value
sec_count_term = 1

while sec_counter < 10000:    # change this to be one digit higher than the variable "counter"
    if sec_value % 2 == 0:
        sec_value = sec_value // 2
    else:
        sec_value = 3 * sec_value + 1

    sec_counter += sec_value
    sec_count_term += 1

sec_counter -= sec_value
print("the last 4 digit number is " + str(sec_counter))

print(sec_count_term - count_term)
