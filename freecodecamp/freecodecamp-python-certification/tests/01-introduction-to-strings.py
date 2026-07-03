# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print("Quotes:\n")

single_quotes = 'Hello'
print(single_quotes)

double_quotes = "Hello"
print(double_quotes)

multi_line = """This is
a multi-line
string"""
print(multi_line)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print("\n\nEscaping:\n")

escaping_single = 'It\'s a pleasure to meet you!'
print(escaping_single)

escaping_double = "And he said \"Oh, that's nice!\""
print(escaping_double)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print("\n\nin operator:\n")

person_one = "Leo"
person_two = "Gzu"
is_it_leo = ('Leo' in person_one) # Case-sensitive
is_it_gzu = ('gzu' in person_two) # Returns false because it is case-sensitive (gzu != Gzu)
print("Is person one Leo?", is_it_leo, "\nIs person two Gzu?", is_it_gzu)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print("\n\nString Indexing:\n")

my_msg = "I'm a big fan of ice cream"
msg_length = len(my_msg)
first_character = my_msg[0]
fourth_character = my_msg[3]
last_character = my_msg[-1]
print("The message is:", my_msg, "\nThe message has:", msg_length, "characters", "\nThe first character is:", first_character, "\nThe fourth character is:", fourth_character, "\nThe last character is:", last_character)

# all data in python is treated as object. strings are immutable objects, which means they can't be modified once declared, but you can reassign the variable name to another object.
my_string = "\nThis is the old string" # declaring the variable
print(my_string)
my_string = "This is the new string" # reassigning the variable name to a new string (object)
print(my_string)
# strings are immutable, you can't modify them:
# my_string[0] = "H" ---> TypeError: 'str' object does not support item assignment

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print("\n\nString Concatenation:\n")

str_concat_one = "Hi, my name " 
str_concat_two = "is Leo. "
# plus operator
str_concatenated = str_concat_one + str_concat_two
print(str_concatenated)
str_concat_three = "Nice to meet you! "
# augmented assignment operator
str_concatenated += str_concat_three
print(str_concatenated)

# you can only concatenate string with string, otherwise you will get a type error
my_age = 23
# str_concatenated += my_age --> TypeError: can only concatenate str (not "int") to str
# to concatenate a string with another object of a different data type, you need to first parse the other object into a string with the str() function
str_concat_four = "I am "
str_concatenated += str_concat_four
print(str_concatenated)
str_concatenated += str(my_age)
print(str_concatenated)
str_concat_five = " years old."
str_concatenated += str_concat_five
print(str_concatenated)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print("\n\nString interpolation\n")
# string interpolation is the process of inserting variables and expressions into a string
# you can use formatted string literals (f-strings) to do string interpolation
name = "Leo"
age = 23 # you don't need to parse the integer object into a string object when using f-strings, python does it on its own.
f_string_lowercase = f"Hi. My name is {name}. Nice to meet you! I am {age} years old." # the "f" is case-insensitive
f_string_uppercase = F"Hi. My name is {name}. Nice to meet you! I am {age} years old." # the "f" is case-insensitive
print(f"f lowercase: {f_string_lowercase}\nF uppercase: {f_string_uppercase}")

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print("\n\nString slicing:\n")
# string slicing lets you extract a portion of a string or work with only a specific part of it
# string[start:stop:step]

str_slc_full = "Leonardo"
print("Full string:", str_slc_full)

str_slc_first = str_slc_full[:1]
print("First character:", str_slc_first)

str_slc_nickname = str_slc_full[:3]
print("Nickname:", str_slc_nickname)

str_slc_nar = str_slc_full[3:6]
print("Nar:", str_slc_nar)

str_slc_two_increment = str_slc_full[::2]
print("Two increment:", str_slc_two_increment)

str_slc_reversed = str_slc_full[::-1]
print("String reversed:", str_slc_reversed)