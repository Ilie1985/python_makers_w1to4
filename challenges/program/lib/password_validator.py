# == INSTRUCTIONS ==
#
# Purpose: Validate a password
# Parameters: one, a string
# Rules:
#   - It must be longer than 7 characters (8 is fine)
#   - It must contain at least one of the following special characters: `!`, `@`,
#     `$`, `%` or `&`
# symbols=["!", "@","$", "%","&"]
# is_valid("1234567")
# is_valid("12345678")  
# is_valid("12345!78")
# Returns: a boolean (True if valid, False otherwise)
# Example:
#   Call:    is_valid("1234567")
#   Returns: False
#   Call:    is_valid("12345678")
#   Returns: False
#   Call:    is_valid("12345!78")
#   Returns: True

# == YOUR CODE ==

def is_valid(password):
#    create a list for symbols
     symbols=["!", "@","$", "%","&"]
     for symbol in symbols:
          if symbol in password and len(password)>7:
               return True
     else :
          return False     

is_valid("1234567")
is_valid("12345678")  
is_valid("12345!78")










