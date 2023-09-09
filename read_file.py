# fhandle = open("sample.txt")

# count the number of lines in a file
# count = 0
# for line in fhandle:
#     count = count + 1
# print("line count: ", count)

# reading the lines in a file
# inp = fhandle.read()
# print(inp[:30])

# search through a file
# for line in fhandle:
#     if line.startswith("m"):
#         # rstrip() removes new line \n characters and trailing whitespace
#         line = line.rstrip()
#         print(line)

# using try/except to validate data and prevent a traceback
fname = input("Enter the name of the file: ")
try:
    fhandle = open(fname)
except:
    print("The file entered cannot be opened: ", fname)
    quit()

count = 0
for line in fhandle:
    if line.startswith("m"):
        count = count + 1
print("There were: ", count, "m lines in ", fhandle)
