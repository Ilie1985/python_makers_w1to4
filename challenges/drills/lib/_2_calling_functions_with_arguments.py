# == INSTRUCTIONS ==
#
# These challenges are a bit trickier and, in some cases, will require a few
# lines of code. If you start to get a little stuck, take a step back and make
# a plan by breaking the overall task down into small steps.

# == EXERCISES ==

# Purpose: checks if a string starts with the letter a
# Example:
#   Call:    starts_with_the_letter_a("apple")
#   Returns: True
#   Call:    starts_with_the_letter_a("Apple")
#   Returns: True
#   Call:    starts_with_the_letter_a("Rock")
#   Returns: False
def starts_with_the_letter_a(string):
    # your code goes here (delete the pass below)
    return string[0] == "a" or string[0]=="A"
starts_with_the_letter_a("apple")
starts_with_the_letter_a("Apple")
starts_with_the_letter_a("Rock")


# Purpose: checks if a string ends with the letter a
# Example:
#   Call:    ends_with_the_letter_a("Java")
#   Returns: True
#   Call:    ends_with_the_letter_a("JAVA")
#   Returns: True
#   Call:    ends_with_the_letter_a("Python")
#   Returns: False
def ends_with_the_letter_a(string):
    # your code goes here (delete the pass below)
    return string[-1]== "a" or string[-1] == "A"
ends_with_the_letter_a("Java")
ends_with_the_letter_a("JAVA")
ends_with_the_letter_a("Python")


# Purpose: checks if a string contains the word hello
# Example:
#   Call:    contains_hello("hello world")
#   Returns: True
#   Call:    contains_hello("HELLO WORLD")
#   Returns: True
#   Call:    contains_hello("world")
#   Returns: False
def contains_hello(string):
    # your code goes here (delete the pass below)
    word ="hello"
    
    return word in string.lower()
contains_hello("hello world")
contains_hello("HELLO WORLD")
contains_hello("world")


# Purpose: replaces the word hello with the word goodbye
# Note: you don't need to worry about matching 'Hello' or 'HELLO' here
#       lowercase only is fine.
# Example:
#   Call:    substitute_hello_with_goodbye("hello folks")
#   Returns: "goodbye folks"
#   Call:    substitute_hello_with_goodbye("Hello folks")
#   Returns: "Hello folks"
def substitute_hello_with_goodbye(string):
    # your code goes here (delete the pass below)
    return string.replace("hello","goodbye")
substitute_hello_with_goodbye("hello folks")
substitute_hello_with_goodbye("Hello folks")


# Purpose: removes the letter x from a string
# Example:
#   Call:    remove_x("xoxo")
#   Returns: "oo"
#   Call:    remove_x("OXO")
#   Returns: "OO"
def remove_x(string):
    # your code goes here (delete the pass below)
   
    replacements = [('x', ''), ('X', '')]
    for char,replacement in replacements:
      if char in string:
        string = string.replace(char, replacement)
   
    return string 
remove_x("xoxo")
remove_x("OXO")


# Purpose: returns the first half of a string
# Example:
#   Call:    first_half("coding")
#   Returns: "cod"
# Note: you can assume the string will always have an even number of characters
def first_half(string):
    # your code goes here (delete the pass below)
     return string[:len(string)//2]

first_half("coding")
# Purpose: returns the second half of a string
# Example:
#   Call:    second_half("coding")
#   Returns: "ing"
# Note: you can assume the string will always have an even number of characters
def second_half(string):
    # your code goes here (delete the pass below)
    return string[len(string)//2:]


# Congrats, you're done with this file. Move on to the next one.
