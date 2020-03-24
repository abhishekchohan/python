#######################
## Author: Abhishek
## File: Sample Test practice
#######################

# Single line comment

'''
multi line comment

'''

#import os library to use function performed at os level like clearing screen on cmd/bash

import random



# try using underscore in variable name
full_name = "Abhishek"

age = 10

########## Type Casting ############
#  float(age)   -> int to float conversion
#  int(float(age))  --> int to float to int  //just for fun :)
# complex(age) ==> (10+0j) 0j is imaginary value; cant convert complex into any other type


print(f'\nThis is Conversion from int->float->int->float->complex\n{complex(float(int(float(age))))}\n\n10 -> 10.0 -> 10 -> 10.0 -> (10+0j)\n')

print(f'Random number betwen 1-10 --> {random.randrange(1,11)}\n\n')  # generate random number between 1 & 10 (11 exclusive)


########### #Strings ########################
#string literals can have any value (concat of int or any data type to string)
msg = f'{full_name} {age} bla bla'
print (msg)

#### Multi line string #######

a = ''' 
hello bla bla bla

another line

multi line string : )


'''

print(a)



######### String Methods ######

print ("\nUpper --> " + msg.upper())
print ("\nLower --> " + msg.lower())
print ("\nCapitalize = first char of first word capital  --> " + msg.capitalize())
print ("\nTitle = first char capital of each word  --> " + msg.title())
print ("\nSwapcase will swap each char with opposite case --> " + msg.swapcase())
print (f'Length of sting --> {len(msg)}')

###### Range/Indexing/split/etc.. in String ######

print (msg[5:10]) # print char at index 5 till 10 (range) inclusive
print (msg.split(" ")) # print a new list of splitted string using space as a splitter
print (msg.split(" ")[1])  # print list element at index 1 i.e 10
print (msg.split(" ")[1:3]) # print list element in range 1-3 but 3 is exclusive

print ("Strip on string -> " + msg.strip())  # remove all white spaces from begining or end of the string

print ("replace bla to Buraah --> " + msg.replace("bla", "Buraah"))


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


#for each loop --> iterating through each element in list/tuple
for i in list_of_stuff:
	print(i)

print ()

print ("Tuple is almost similar to list \n")

for i in tuple_of_stuff:
	print(i)



# Dictionary === just like Object [in Javacript] === { key: value , key :value }

fav_pizza = {
	'Abhishek': 'Veggie Pizza',
	'Parn'    : 'Chkn Pizza'  ,
	'Divyesh' : 'Any Pizza'
}

print("\n" + fav_pizza["Parn"])

for key in fav_pizza:
	print("\n" + key + " loves " + fav_pizza[key])