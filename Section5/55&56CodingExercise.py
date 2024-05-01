#55ADDING EVEN NUMBER 

target = int(input())
even_sum = 0
for number in range(2, target + 1, 2):
    even_sum += number
print(even_sum)    


#-------------------------------

#56THE FIZZBUZZ JOB QUESTION

target = 100
for number in range(1, target +1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)            