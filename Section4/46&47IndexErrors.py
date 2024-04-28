fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches",]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

all_dozen = [fruits, vegetables]

print(all_dozen)

#47coding exercise
line1 = [" "," "," "]
line2 = [" "," "," "]
line3 = [" "," "," "]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()
#Code below
letter = position[0].lower()
abc = ["a","b","c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")