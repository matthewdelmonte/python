import time

# Converting the current time into epoch time in milliseconds
current_time_milliseconds = int(time.time() * 1000)

# Converting the time structure into epoch time in seconds
current_time_seconds = current_time_milliseconds / 1000

epoch_time = input("Enter epoch time: ")

# localtime is GMT - 7 for PDT or you can just use gmtime for GMT output
readable_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(epoch_time)))

# Parsing the epoch time into a time structure
human_readable_time = time.strftime(
    "%Y-%m-%d %H:%M:%S", time.localtime(current_time_seconds)
)

print("The current epoch time in mms is: {}".format(current_time_milliseconds))
print(
    "The current epoch time in human readable format is: {}".format(human_readable_time)
)
print("The epoch time you entered is: {}".format(readable_time))

date_str = input("Enter the date YYYY-MM-DD format: ")
time_str = input("Enter the time HH:MM:SS format: ")

datetime_str = f"{date_str} {time_str}"
datetime_fmt = time.strptime("%Y-%m-%d %H:%M:%S")
