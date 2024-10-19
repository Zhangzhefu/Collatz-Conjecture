#
#
#
counter = 24
count_term = 1

while counter < 1000:
    if value % 2 == 0:
        value = value // 2
    else:
        value = 3 * value + 1

    counter += value
    count_term += 1

print("the first 4 digit number is " + str(counter))
#print("the value left off here is " + str(value))


sec_value = 24
sec_counter = 24
sec_count_term = 1

while sec_counter < 10000:
    if sec_value % 2 == 0:
        sec_value = sec_value // 2
    else:
        sec_value = 3 * sec_value + 1

    sec_counter += sec_value
    sec_count_term += 1

sec_counter -= sec_value
print("the last 4 digit number is " + str(sec_counter))

#print("the value left off here is " + str(sec_value))
#print("the terms it took for this is " + str(count_term))
#print(sec_counter - sec_value - counter)

print(sec_count_term - count_term)
