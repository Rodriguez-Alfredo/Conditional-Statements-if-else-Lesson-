#!/bin/python3

#CONDITIONAL STATEMENTS - IF/ELSE

def drink(money):
	if money >=2:
		return "You've got yourself a drink!"
	else:
		return "No drink for you!"

print(drink(3))#you have 3 dollars at the time
print(drink(1))# you have 1 dollar at the time



def alcohol(age,money):

#You have the age and money
	if (age >= 21) and (money >= 5):
		return "We're getting a drink!"
		
#you have the age but not enough money
	elif (age >= 21) and (money < 5):
		return "Come back with more money!"
		
#You dont have the age but have money
	elif (age < 21) and (money >= 5):
		return "Nice try, kid!"
		
#Dont have the age and money 
	else:
		return "You're too young and too poor."

#add the values
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,5))
print(alcohol(20,4))


#Thank You TCM Security 