#Keyword Arguments
#def my_function(a,b,c)
#Do this with a
#Then do this with b
#Finally do this with c

#my_function(c=3, a=1, b=2)


#POSITIONAL ARGUMENTS
#def my_function(a, b, c):
#Do this with a
#Then do this with b
#Finally do this with c

#my_function(3, 1, 2) a=3 ,b=1 , c=2

#Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

#greet_with("RAVI", "Iceland")    
#vs
#greet_with("Iceland", "Ravi")


#Function with keyword arguments
greet_with(location="Iceland", name="Ravi")