print("Thank you for choosing Pizza Deliveries!")
size = input()
add_pepperoni = input()
extra_cheese = input()

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25   

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    if size == "S":
        bill += 5
    else:
        bill += 6            

print(f"Your final bill is: ${bill}.")
