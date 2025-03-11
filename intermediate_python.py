
------
password = "not_very_secure_2023"

# Define the password_checker function
def password_checker(submission):
  
  # Check that the password variable and the submission match
  if password==submission:
    print("Successful login!")
  
  # Otherwise, print "Incorrect password"
  else:
    print("Incorrect password")

# Call the function    
password_checker("NOT_VERY_SECURE_2025")
------
# More sophisticated example
password = "not_very_secure_2023"  # Stored password

#Define function with submission as a parameter
def password_checker(submission):
    if password == submission:
        return "Successful login!"
    else:
        return "Incorrect password"

# Get user input
user_input = input("Enter your password: ")  

# Call function with user input and print result
print(password_checker(user_input))  
--------
# Define clean_text
def clean_text(text, lower=True):
  if lower == False:
    clean_text = text.replace(" ", "_")
    return clean_text
  else:
    clean_text = text.replace(" ", "_")
    clean_text = clean_text.lower()
    return clean_text
-------
# Define clean_text
def clean_text(text, remove=None):
  if remove != None:
    clean_text = text.replace(remove, "")
    clean_text = clean_text.lower()
    return clean_text
  else:
    clean_text = text.lower()
    return clean_text

-----------
# Create the convert_data_structure function
def convert_data_structure(data,data_type="list"):
  
  # If data_type is "tuple"
  if data_type=="tuple":
    data = tuple(data)
  
  # Else if data_type is set, convert to a set
  elif data_type=="set":
    data = set(data)
  else:
    data = list(data)
  return data

# Call the function to convert to a set
convert_data_structure({"a", 1, "b", 2, "c", 3}, data_type="set")
----------------
#Adding docstrings
def clean_string(text):
  
  # Add a single-line docstring
  """ Swap spaces to underscores and convert text to lowercase. """
    
  no_spaces = text.replace(" ", "_")
  clean_text = no_spaces.lower()
  return clean_text

# Access the docstring
print(clean_string.__doc__)
-----------------------------------------------------------------------
# Create the convert_data_type function
def convert_data_structure(data, data_type="list"):
  # Add a multi-line docstring
  """
  Convert a data structure to a list, tuple, or set.
  
  Args:
  	data (list, tuple, or set): A data structure to be converted.
    data_type (str): String representing the type of structure to convert data to.
    
  
  	
  """
  if data_type == "tuple":
    data = tuple(data)
  elif data_type == "set":
    data = set(data)
  else:
    data = list(data)
  return data
  ------------------------------
  # Create the convert_data_type function
def convert_data_structure(data, data_type="list"):
  # Add a multi-line docstring
  """
  Convert a data structure to a list, tuple, or set.
  
  Args:
  	data (list, tuple, or set): A data structure to be converted.
    data_type (str): String representing the type of structure to convert data to.
    
  Returns:
  	data (list, tuple, or set): Converted data structure
  """
  if data_type == "tuple":
    data = tuple(data)
  elif data_type == "set":
    data = set(data)
  else:
    data = list(data)
  return data

print(help(convert_data_structure))
---------------------------------------------------------------------------
# Define a function called concat
def concat(*args):
  
  # Create an empty string
  result = ""
  
  # Iterate over the Python args tuple
  for arg in args:
    result += " " + arg
  return result

# Call the function
print(concat("Python", "is", "great!"))
----------------------------------------------------------------------------

# Define a function called concat
def concat (**kwargs):
  
  # Create an empty string
  result = ""
  
  # Iterate over the Python kwargs
  for kwarg in kwargs.values():
    result += " " + kwarg
  return result

# Call the function
print(concat(start="Python", middle="is", end="great!"))

----------------------------------------------------------------------------
## Lambda Functions
sale_price = 29.99

# Define a lambda function called add_tax
add_tax = lambda x: x*1.2 

# Call the lambda function
print(add_tax(sale_price))

-----
sale_price = 29.99

# Call a lambda function adding 20% to sale_price
print((lambda x: x * 1.2)(sale_price))

----------------------------------------------------------------------------
sales_prices = [29.99, 9.95, 14.50, 39.75, 60.00]

# Create add_taxes to add 20% to each item in sales_prices
add_taxes = map(lambda x: x*1.2, sales_prices)

# Use add_taxes to return a new list with updated values
print(list(add_taxes))

----------------------------------------------------------------------------
#Error handling
def snake_case(text):
  # Attempt to clean the text
  try:
    # Swap spaces for underscores
    clean_text = text.replace(" ", "_")
    clean_text = clean_text.lower()
  # Run this code if an error occurs
  except:
    print("The snake_case() function expects a string as an argument, please check the data type provided.")
    
snake_case("User Name 187")

-------------------------------------------------------------------------------
def snake_case(text):
  # Check the data type
  if type(text) == str:
    clean_text = text.replace(" ", "_")
    clean_text = clean_text.lower()
  else:
    # Return a TypeError error if the wrong data type was used
    raise TypeError("The snake_case() function expects a string as an argument, please check the data type provided.")

-----
#Interview

from typing import List, Dict

def sort_jobs_by_priority(jobs: List[Dict[str, int]]) -> List[Dict[str, int]]:
    if not jobs:
        raise ValueError("Job list cannot be empty")
    
    # Sort jobs by priority in descending order, maintaining order for equal priority
    return sorted(jobs, key=lambda job: job['priority'], reverse=True)

# Example usage
jobs = [
    {'ID': 1, 'priority': 2},
    {'ID': 2, 'priority': 3},
    {'ID': 3, 'priority': 1},
    {'ID': 4, 'priority': 3},
]

sorted_jobs = sort_jobs_by_priority(jobs)
print(sorted_jobs)
-------------------------------------
    
snake_case("User Name 187")
------------------------------------------------------------------------------

