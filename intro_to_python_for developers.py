# Add 19 and 17
print(19+17)

# Subtract 12 from 99
print(99-12)

# Calculate and print 9 multiplied by 2
print(9*2)

# Print the result of dividing 120 by 12
print(120/12)
-----------------------------------------------------------
#Variable Assignment
# Age of a customer
customer_age = 27

#Create account_balance variable
account_balance = 120.50

# Print account_balance
print(account_balance)

account_balance = 20000.00
is_millionaire = False

# Update account balance
account_balance = 1300000.00
# Update is_millionaire variable
is_millionaire = True

print(account_balance)
print(is_millionaire)

customer_age = 49
account_balance = 120078.89

# Print the data type of account_balance
print(type(account_balance))

customer_age = 49
account_balance = 120078.89
is_millionaire = False

# Print the data type of is_millionaire
print(type(is_millionaire))

----------------------------------------------------------------------------
#strings transformations

# Create review_one
review_one = """ I really enjoy the courses,
and they are easy to fit into my busy schedule. 
I wish I had started using your platform sooner.
I'll be recommending you to my friends!!"""

# Create review_two
review_two = """One year ago, I was unsure of how to make progress in my career. 
Now, I work as a Prompt Engineer, and I can't thank you enough! 
Keep up the great work."""

# Print the two reviews individually
print(review_one)
print(review_two)

most_popular_course = "Intro to Embeddings with the OpenAI API"

# Update the first word
most_popular_course = most_popular_course.replace("Intro", "Introduction")

print(most_popular_course)

most_popular_course = "Intro to Embeddings with the OpenAI API"

# Update the first word
most_popular_course = most_popular_course.replace("Intro", "Introduction")

# Swap spaces for underscores
most_popular_course = most_popular_course.replace(" ", "_")

# Change to lowercase
most_popular_course = most_popular_course.lower()

print(most_popular_course)

------------------------------------------------------------------------------
#string manipulation applied on transformations on pandas dataframes

import pandas as pd
from sqlalchemy import create_engine

# Database connection (Modify this for your actual DB)
engine = create_engine("sqlite:///courses.db")  # Example using SQLite; replace with your DB connection

# Read data into Pandas DataFrame
df = pd.read_sql("SELECT id, course_name FROM Courses", engine)  # Assuming `id` is the primary key

# Apply transformations
df['course_name'] = df['course_name'].str.replace("Intro", "Introduction")
df['course_name'] = df['course_name'].str.replace(" ", "_")
df['course_name'] = df['course_name'].str.lower()

# Write updated data back to the database
df.to_sql("Courses", engine, if_exists="replace", index=False)  # Be cautious with `replace`

print("Database updated successfully!")


---------------------------------------------------------------------------------
#Lists
# Create the playlist variable
playlist = [1,"Blinding Lights", 2, "One Dance", 3, "Uptown Funk"]

# Print the list
print(playlist)

# Find the second song
print(playlist[1])

 Get the last song's artist
print(playlist[-1])

# Print all songs in the playlist
print(playlist[1::3])

-----------------------------------------------------------------------------------
#Real world application 
import pandas as pd
import json

# Sample dataset simulating a music streaming service (e.g., Spotify)
data = {
    "user_id": [201, 202, 203],
    "username": ["Alice", "Bob", "Charlie"],
    "playlist": [
        json.dumps([
            {"title": "Blinding Lights", "artist": "The Weeknd"},
            {"title": "Levitating", "artist": "Dua Lipa"},
            {"title": "Peaches", "artist": "Justin Bieber"},
            {"title": "Save Your Tears", "artist": "The Weeknd"},
            {"title": "Kiss Me More", "artist": "Doja Cat"},
            {"title": "Good 4 U", "artist": "Olivia Rodrigo"}
        ]),  # Alice's playlist

        json.dumps([
            {"title": "Shape of You", "artist": "Ed Sheeran"},
            {"title": "Uptown Funk", "artist": "Bruno Mars"},
            {"title": "Closer", "artist": "The Chainsmokers"},
            {"title": "Senorita", "artist": "Shawn Mendes"},
            {"title": "Happier", "artist": "Marshmello"},
            {"title": "Bad Guy", "artist": "Billie Eilish"}
        ]),  # Bob's playlist

        json.dumps([
            {"title": "Hello", "artist": "Adele"},
            {"title": "Someone You Loved", "artist": "Lewis Capaldi"},
            {"title": "Sunflower", "artist": "Post Malone"},
            {"title": "Shallow", "artist": "Lady Gaga"},
            {"title": "Watermelon Sugar", "artist": "Harry Styles"},
            {"title": "Don't Start Now", "artist": "Dua Lipa"}
        ])  # Charlie's playlist
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert JSON string to Python lists (list of dictionaries)
df["playlist"] = df["playlist"].apply(json.loads)

# Extract every 3rd song starting from index 1
df["filtered_playlist"] = df["playlist"].apply(lambda x: x[1::3])

# Display the transformed DataFrame
print(df[["user_id", "username", "filtered_playlist"]])

---------------------------------------------------------------------------------------------
#Dictionaries

# Create the playlist dictionary
playlist = { "The Weeknd": "Blinding Lights", "Drake":"One Dance"}

# Print the playlist
print(playlist)

# Print the song by Coldplay
print(playlist["Coldplay"])

# Add a new song
playlist["Usher"] = "Yeah!"

# Print the songs in the playlist
print(playlist.values())

---------------------------------------------------------------------------------------------
#tuples
# Fixed Data: When the data should not change.
# Returning Multiple Values: Functions returning multiple values.
# Dictionary Keys: When you need immutable keys.
# Iterating Over Paired Data: With unpacking during iteration.
# Performance: More efficient in memory usage than lists.
# Representing Records: Fixed data structure to represent a record or entity.
# Safe for Multi-threading: Immutable and thread-safe.

# Create a tuple
q3_financials=(325780, 1041, 4271599)

# Print the tuple
print(q3_financials)

---------------------------------------------------------------------------------------------
#Sets
hip_hop_list = ["Drake", "JAY-Z", "50 Cent", "Drake"]

# Create a set
indie_set = {"Kings of Leon", "MGMT", "Stereophonics"}

# Convert hip_hop to a set
hip_hop_set = set(hip_hop_list)

# Print the indie and hip_hop sets
print(indie_set)
print(hip_hop_set)

---------------------------------------------------------------------------------------------
# Conditional Statements

# Check if September inflation is less than August inflation
if inflation_september < inflation_august:
  print("Inflation decreased")

# Check if September inflation is more than August inflation
elif inflation_september > inflation_august:
  print("Inflation increased")
  
# Confirm that they are equal
else :
  print("Inflation remained stable")
------
# Check the number of beds
if num_beds< min_num_beds:
  print("Insufficient bedrooms")

# Check square feet
elif sq_foot<=min_sq_foot:
  print("Too small")
  
# Check the rent
elif rent > max_rent:
  print("Too expensive")
  
# If all conditions met
else:
  print("This looks promising!")

---------------------------------------------------------------------------
#For loops
#for value in sequence
#action

user_ids = ["T42YG4KTK", "VTQ39IDQ0", "CRL11YUWX", 
            "K6Y5URXLR", "V4XCBER7V", "IOGQWC61K"]

# Loop through user_ids
for user_id in user_ids:
  # Print the user_id
  print(user_id)

------------------------------------------------------------------------
# Ensure range() works as expected
print(type(range))  # Should print <class 'builtin_function_or_method'>

# Create the tickets_sold variable
tickets_sold = 0

# Create the max_capacity variable
max_capacity = 30

# Loop through a range up to max_capacity
for _ in range(max_capacity):  
    tickets_sold += 1
  
print(f"Sold out: {tickets_sold} tickets sold!")
---------------------------------------------------------------------------

# Loop through the dictionary's keys and values
for key, value in courses.items():
  
  # Check if the value is "AI"
  if value == "AI":
    print(key, "is an AI course")
  
  # Check if the value is "Programming"
  elif value == "Programming":
    print(key, "is a Programming course")
  
  # Otherwise, print that it is a "Data Engineering" course
  else:
    print(key, "is a Data Engineering course")

-----------------------------------------------------------------------------
# while condition
    action

tickets_sold = 0
max_capacity = 10

# Create a while loop
while tickets_sold< max_capacity:
  
  # Add one to tickets_sold in each iteration
  tickets_sold += 1

# Print the number of tickets sold
print("Sold out:", tickets_sold, "tickets sold!")

-------
release_date = 26
current_date = 22

# Create a conditional loop while current_date is less than or equal to the release_date
while current_date <= release_date:
  
  # Promote purchases
  if current_date <= 24:
    print("Purchase before the 25th for early access")
  
  # Check if the date is equal to the 25th
  elif current_date == 25:
    print("Coming soon!")
  else:
    print("Available now!")
  
  # Increment current_date by one
  current_date += 1

----------------------------------------------------------------------------------------------
# Create an empty list
authors_below_twenty_five = []

# Loop through the authors dictionary
for key, value in authors.items():
  
  # Check for values less than 25
  if value < 25:
    
    # Append the author to the list
    authors_below_twenty_five.append(key)
    
print(authors_below_twenty_five)

----------------------------------------------------------------------------------------------

for genre, average_sale in genre_sales.items():
    
    # Filter for the maximum sales value
    if average_sale == 5166000000:
      
      # Print the genre
      print("Most popular genre: ", genre)
      print("Average sales: ", average_sale)
    
    # Filter for the minimum sales value
    elif average_sale ==80000000:
      
      # Print the genre
      print("Least popular genre: ", genre)
      print("Average sales: ", average_sale)

---------------------------------------------------------------------------------------------

# Loop through the dictionary
for genre, sale in genre_sales.items():
  
  # Check if genre is Horror or Mystery
  if genre == "Horror" or genre == "Mystery":
    print(genre, sale)
  
  # Check if genre is Thriller and sale is at least 3 million
  elif genre=="Thriller" and sale>=3000000:
    print(genre, sale)

-------------------------------------------------------------------------------------------

