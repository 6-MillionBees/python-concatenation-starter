# Concatenation Practice


# Work with your assigned partner
# Each person in your team should take turns writing the code to create and display longer strings
# Check your partner's code for spelling, capitalization, and coding errors
# Correct any bugs in your code

# Part 1
# Create variables to store your first, middle, and last name
# Have Python print a message that contains your concatenated full name, i.e., your combined first, middle and last names

first_name = 'Arden '
middle_name = 'Elis'
last_name = 'Boettcher'

print(first_name + middle_name + ' ' + last_name)

# Part 2
# Assume you're building a Space Invaders game
# Use concatenation to create and display a custom welcome message that includes the player's first name

player_name = input('What\'s your name? ')

print('Welcome ' + player_name.title() + ' to Space Invaders')

# Part 3
# Use concatenation to build and display a string that includes your first name, last name, and the year you were born

year_of_birth = '2008'

print('my name is ' + first_name + middle_name + ' ' + last_name + ' ' + 'and I was born in ' + year_of_birth) 

# Part 4
# Use concatenation to create and display a sentence that says which country in the world you would visit if money were no object

country = 'finland'

print('I would definitely go to ' + country.title() + ' because ' + country.title() + ' is the best and they have so many saunas')
