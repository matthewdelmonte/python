import time

# Converting the current time into epoch time in milliseconds
current_time_milliseconds = int(time.time() * 1000)

# Converting the time structure into epoch time in seconds
current_time_seconds = current_time_milliseconds / 1000

epoch_time = input("Enter epoch time in milliseconds: ")
len_of_number = len(str(epoch_time))

if len_of_number == 13:
    epoch_time_seconds = float(epoch_time) / 1000
else:
    epoch_time_seconds = float(epoch_time)

# localtime is GMT - 7 for PDT or you can just use gmtime for GMT output
readable_time = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(epoch_time_seconds))

# Parsing the epoch time into a time structure
human_readable_time = time.strftime(
    "%Y-%m-%d %H:%M:%S", time.localtime(epoch_time_seconds)
)

converted_epoch_entry = time.strftime(
    "%Y-%m-%d %H:%M:%S", time.localtime(float(epoch_time))
)

print("The current epoch time in mms is: {}".format(current_time_milliseconds))
print("The current epoch time entered in human readable format is: {}".format(human_readable_time))
