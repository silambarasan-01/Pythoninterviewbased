# Sum of digit until it reduces to single digit
# Reading number
number = int(input("Enter number: "))
# Finding sum
total_sum = 0
step = 1
condition = True
while condition:
    while number:
        total_sum = total_sum+number % 10
        #print(total_sum)
        number //= 10
        #print(number)
    print("Step-%d Sum: %d" % (step, total_sum))
    number = total_sum
    total_sum = 0
    step = step+1
    condition = number > 9