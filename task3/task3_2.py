#2)Create a list of size 5 and execute the slicing structure

new_list=[10,20,30,40,50]

print(len(new_list))            # 5

#print list as is

print(new_list[:])              #[10, 20, 30, 40, 50]

#slice from start.. get items from start until item number 4...index not considered

print(new_list[:4])             #[10, 20, 30, 40]

#slice to end... get items from after item 1 till end

print(new_list[1:])             #[20, 30, 40, 50]

#slice in between string... slice from item in index 1 to item number 3..item4 in index 3 not included

print(new_list[1:3])        #[20, 30]

#Negative index         #last elemnt has index -1 ..first element -

print(new_list[-3:-1])   #[30, 40]

#reverse list using negative index

print(new_list[::-1])   #[50, 40, 30, 20, 10]