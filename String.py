# Normal way of Printing string
print("Hello, World")

# If single inverted comma in string. use double inverted comma outside
print("It's Car")

# To print paragraph
print("""My Name is Abhay Pratap Singh from Shahjahanpur, UP
I am currently pursuing my BTech from AKGEC, Ghaziabad, UP""")

# Output no. of char of string
message = "Hello World"
print(len(message))

# Print particular part of string
print(message[0:7])

# Transform to lower case 
print(message.lower())

# Transform to upper case
print(message.upper())

# no. of times a char or substring occur
print(message.count('o'))

# to find index of particular char or substring
print(message.find('World'))

# replace particular part of string Note: it return replaced string to store in new variable
new_message = message.replace('World', 'Universe')
print(new_message)

# adding two string
greeting = 'Namaste'
name = 'Duniya'
message = greeting + ' ' + name
print(message)

# better way to add strings
message = f'{greeting} {name}'
print(message)

# To know which methods can be used for certain variable
print(dir(message))

# To know more details about a variable 
print(help(str))
