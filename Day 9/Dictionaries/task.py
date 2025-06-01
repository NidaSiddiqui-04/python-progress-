programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
print(programming_dictionary["Bug"])
empty_dict={}
print(type(empty_dict))
programming_dictionary["loop"]="loops are control flow structures that allow you to execute a block of code repeatedly."
# edit an element in a dictionary
programming_dictionary["Bug"]="Any small insect"
#loop through a dictionary
for key in programming_dictionary:
    print(key)
    programming_dictionary[key]="loop"
print(programming_dictionary)

#wipe an existing dictionary
#programming_dictionary={}
#print(programming_dictionary)
# dict.update(dict2)
empty_dict.update(programming_dictionary)
print(empty_dict)