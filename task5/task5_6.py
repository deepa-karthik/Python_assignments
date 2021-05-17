# Read doc.txt file using Python File handling concept and return only the even length string from
# the file. Consider the content of doc.txt as given below:
# Hello I am a file
# Where you need to return the data string
# Which is of even length
# Make sure you return the content in The same link as it is present.

#to create a new file and write in the file
# file=open("doc.txt","w")
# file.write("Hello I am a file")
# file.close()

#to open file in append mode

# file=open("doc.txt","a")
# file.write("\nWhere you need to return the data string\n Which is of even length\n Make sure you return the content in The same link as it is present.")
# file.close()

#to print file content to console

file=open("doc.txt","r")
#print(file.readlines())
lines_list=file.readlines()     #returns all lines in file as a list
#print(lines_list)
max_str=lines_list[0]       #holds the first line of file
#print(max_str)
for line in lines_list:
    str_len=len(line)
    if str_len>len(max_str):
        max_str=line
    else:
        continue

print(f"the string with maximum string length in doc.txt is :'{max_str}'")

#output
# the string with maximum string length in doc.txt is :' Make sure you return the content in The same link as it is present.'
#
# Process finished with exit code 0


