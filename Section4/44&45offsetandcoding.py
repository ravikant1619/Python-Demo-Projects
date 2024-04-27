#OFFSET MEANS THE FIRST WORD 
#FOR EXAMPLE IN STATES OF AMERICA = DELAWARE IS THE OFFSET
#APPENDING IS USED TO ADD THE WORD OR ANY THINGS

states_of_america = ["Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, Florida, Georgia, Hawaii, Idaho, Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, Missouri, Montana, Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, Pennsylvania, Rhode Island, South Carolina, South Dakota, Tennessee, Texas, Utah, Vermont, Virginia, Washington, West Virginia, Wisconsin, and Wyoming."]

states_of_america[1] = "Alaska"

states_of_america.append("Raviland")

print(states_of_america)


#45 coding 

names = names_string.split(", ")

import random


num_items = len(names)  #len means length 

random_choice = random.randin(0, num_items -1)  #is a built-in function that returns a random integer from a given range

person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")