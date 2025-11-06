# Instructions are at https://python.datalumina.com
#

name = input("Hey, what's your name? ")
print(f"Hi there {name}, nice to meet you")
age = input("How old are you? ")
if age.isdigit():
    print(f"Looks like you'll be {int(age)+1} years old next year!")
else:
    print(f"C'mon {name}, {age} isn't in number format!")




