#######################
## Author: Abhishek
## File: Sample Test practice
#######################

# Single line comment

'''
multi line comment

'''

#import os library to use function performed at os level like clearing screen on cmd/bash
import os
os.system('clear')


# try using underscore in variable name
full_name = "Abhishek"
age = 10

# LIST is like an array but can have any data type or multiple too.
# we can also perform actions like add remove elemnets, etc..
list_of_stuff = ["random", "shit", 1 , 1.234, True]


# TUPLE is like a CONSTANT LIST means we cannot manipulate it.
# once declared that's it.
# TUPLE is faster than LIST in some scenario to search in elements.
tuple_of_stuff = ("random", "shit", 1 , 1.234, True)


#print is used to print on cmd/bash/shell
print (full_name)


# New Line
print ()

for i in list_of_stuff:
	print(i)

print ()

print ("Tuple is almost similar to list \n")

for i in tuple_of_stuff:
	print(i)



# Dictionary === Object [in Javacript] === { key: value , key :value }

fav_pizza = {
	'Abhishek': 'Veggie Pizza',
	'Parn'    : 'Chkn Pizza'  ,
	'Divyesh' : 'Any Pizza'
}

print("\n" + fav_pizza["Parn"])

for key in fav_pizza:
	print("\n" + key + " loves " + fav_pizza[key])