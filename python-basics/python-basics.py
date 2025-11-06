# Instructions are at https://python.datalumina.com
#

# This is a comment
"""
this is a multi line comment
which is in between triple quotes
"""

name = "My name is Asanga"

name_long = """
my name is Asanga.
And I can use more lines to fill
this string because I'm using
tripple quotes like the long comments
"""
print (name_long) # this prints the lines exactly as above because of the new line feed

long_dash = "-" * 20 
print (long_dash)

new_long_dash = "-" * len(name)
print(name)
print(new_long_dash)

#boolean
age = 18
can_vote = age >= 18 #returns True

# two equal signs is for comparison
is_18 = age == 18  # returns True
not_30 = age != 30 # returns True

#logical operators
has_licence = True
can_drive = age >= 16 and has_licence #returns True

print (True and True) # prints True
print (not True) #prints False

#string manipulation
name = "Asanga"
string = f"Hi there, my name is {name}"

#string methods
text = "Python Programming"
print(text.lower())
print(text.upper())
print(text.title())

#finding and replacing
message = "I love Python programming with Python"

print("Python" in message) # True
print(message.startswith("I")) # True
print(message.endswith("Python")) #True

print(message.find("Python")) # 7 (fist occurence)
print(message.count("Python")) # 2

new_message = message.replace("Python", "JavaScript")
#replaces both occrences of the word Python with JavaScript

word_count = message.count("Python")

#flow controls
# if else .. use ":" at the end of both if and else
"""
if (condition) and (condition):
    do this
elif (condition):
    do the other
else:
    do something else
"""

#nested if statements
has_ticket = False
age = 18

if has_ticket:
    if age >= 18:
        print("Enjoy the movie")
    else:
        print("Needs supervision")
else:
    print("Buy a ticket")

# For loop
for i in renge(5): # i can be any variable name
    print(i) #prints zero to 4

for i in range(1, 6):
    print(i) #prints 1 to 5

for i in range (0, 10, 2):
    print(i) #prints 0, 2, 4, 6, 8

#data structures - think as containers
#Lists - like a shoping list (ordered items)
#Dictionaries - like a phone book (name > number)
#Tuples - like coordinates (fixed values)
#Sets - like a bag of unique items

#Lists
age = 25
my_list = ["Alice", 25, age, True]
my_list[0] #Alice
my_list[-1] #True - the last item.. so a -2 is the sencod last
my_list[0] = "James" #Alice gets replaced with James
my_list.append("Alice") #at the end
my_list.remove("Alice")
my_list.insert(1, "Alice") #inserts after James
my_list.reverse()
new_list = my_list.copy()

#Dictionary
person = { #note curlie brackets
    "name": "Alice",
    "age": 25,
    "city": "NY"
}
person["age"] #returns 25. Note the squre brackets
person["name"] = "James" #Alice gets replaced by James
person["Licence"] = True #Licence gets added to the dictionary at the end
del person["Licence"] #removes it

#keys, values and items
print(person.keys()) # dict_keys(['name', 'age', 'city'])
print(person.values()) # dict_values(['Alice', 25, 'NY'])
print(person.items()) # dict_items([('name', 'Alice'), ('age', 25), ('city', 'NY')])

if "name" in person:
    print("Name found!")

#update multiple values
person.update({"age": 31, "job": "Engineer"})

#Tuples use brackets
# values can't be changed 
empty = ()

point = (3, 5)
colours = ("red", "green", "blue")
print(point[0]) #3
print(colours[-1]) # "blue"
print(colours[0:2]) # ("red", "green")

#Sets
empty_set = set() # not {} - that's a dict!

#create with values - both ways work
numbers = {1, 2, 3, 4, 5} #no pairs
fruits = set(["apple", "banana", "orange"])
new_num = set([1, 2, 3, 4, 5])

#from a list - it removes duplicates - good for dedupe
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores) # {85, 90, 92}

