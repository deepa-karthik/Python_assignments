# Write a program to construct a dictionary from the two lists containing the names of students and
# their corresponding subjects. The dictionary should map the students with their respective subjects.
# Let’s see how to do this using for loops and dictionary comprehension.


name_list=["Deepa","Karthik","Lucy","Maya"]
sub_list=["math","CSC","English","economics"]

#creates a zip object which contains tuples of elements from each list
zip_obj=zip(name_list,sub_list)
#print(dict(zip_obj))     #{'Deepa': 'math', 'Karthik': 'CSC', 'Lucy': 'English', 'Maya': 'economics'}
#print(list(zip_list))      #comment print for the zip object to be available for creating the dictionary
#[('Deepa', 'math'), ('Karthik', 'CSC'), ('Lucy', 'English'), ('Maya', 'economics')]


#to generate a dictionary from zip object using loops

my_dict={}
my_dict.update({key:value for key,value in list(zip_obj)})
print(f"the expected output dictionary is:{my_dict}")

#output
# the expected output dictionary is:{'Deepa': 'math', 'Karthik': 'CSC', 'Lucy': 'English', 'Maya': 'economics'}
#
# Process finished with exit code 0


