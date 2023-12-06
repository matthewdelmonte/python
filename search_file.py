# Search for a phrase in a file using find()
import re

# User entries
search_phrase = input('Enter a search term: ')
search_file = input('Enter the relative path of the file: ')

# State variables
match_found = False
match_count = 0

# Open file
my_file = open(search_file)

# Search
for line in my_file:
    line = line.rstrip()
    if line.find(search_phrase) >= 0:
        match_found = True
        match_count = match_count +1

# Close the file
my_file.close()

# Print the results
if match_found and match_count <= 1:
    print(f"Found {match_count} result for {search_phrase}.")
elif match_found and match_count > 1:
    print(f"Found {match_count} results for {search_phrase}.")
elif not match_found:
    print('Could not find search value.')