#year = input() # Which year do you want to check?

#if year % 4 == 0:
 # if year % 100 == 0:
    #  print("Leap year.")
    #else:
      #print("Not leap year.")
 # else:
    #rint("Leap year.")
#else:
  #print("Not leap year.")

#----------------------------------------------

year = int(input()) # TypeError without int() conversion

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")  