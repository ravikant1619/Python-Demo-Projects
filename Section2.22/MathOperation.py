#3 + 5
#7 - 4
#3 * 2
#6 / 3
#2 ** 3 #means 2*2*2 if there is 4 then 3 it will 2*2*2*2

#PEMDAS LR MEANS LEFT AND RIGHT

#1 Parenthese  ()
#2 Exponents   **
#3 Multiplication  *
#4 Division     /
#5 Addition  +
#6 Subtraction -


#Example 
#print(3 * 3 + 3 / 3 -3)
#how it will happen
# 9+3/3-3
# 9+1-3
#10-3
#7 answer

#if i want to get 3 how it wil get 

# (3 * (3 + 3) / 3 -3)
#step
# 3* 6/3-3
# 18 / 3 -3
# 6 -3
# 3 answer

#Coding Exercise (BMI CALCULATOR)

height = input()
weight = input()
#Code
weight_as_int = int(weight)
height_as_float = float(height)
#Using the exponent operator (**)
bmi = weight_as_int / height_as_float ** 2
#or using multiplication and PEMDAS
#bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)
print(bmi_as_int)
