# Search for a phrase in a file using REGEX
import re

# User entries
search_input = input("Enter a search term and include regex: ")
search_phrase = str(search_input)
search_file = input("Enter the relative path of the file: ")

# State variables
match_found = False
match_count = 0

# Open file
my_find = open(search_file)

# Search
for line in my_find:
    line = line.rstrip()
    if re.search(search_phrase, line):
        match_found = True
        match_count = match_count + 1

# Close the file
my_find.close()

# Print the results
if match_found and match_count <= 1:
    print(f"Found {match_count} result for {search_phrase}.")
elif match_found and match_count > 1:
    print(f"Found {match_count} results for {search_phrase}.")
elif not match_found:
    print("Could not find search value.")
