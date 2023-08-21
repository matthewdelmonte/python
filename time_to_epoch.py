import time

# Prompting the user for date and time input
date_str = input("Please enter a date in YYYY-MM-DD format: ")
time_str = input("Please enter a time in HH:MM:SS format: ")

# Combining date and time into a single string
datetime_str = f"{date_str} {time_str}"

# Defining the expected format
datetime_format = "%Y-%m-%d %H:%M:%S"

# Parsing the user input into a time structure
time_struct = time.strptime(datetime_str, datetime_format)

# Converting the time structure into epoch time in seconds
epoch_time_seconds = time.mktime(time_struct)

# Converting the epoch time to milliseconds
epoch_time_milliseconds = int(epoch_time_seconds * 1000)

print(f"The epoch time in milliseconds is: {epoch_time_milliseconds}")
