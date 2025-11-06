# Instructions are at https://python.datalumina.com
#

# Functions
# for styling, don't use uppercase names use _

def greet():
    print("Hello!")
    pass #this is optional

# if you define a global var, it will be accessible inside func
# but not the other way around, even if you use the same name

def check_weather(name, temp):
    #local values
    #temp = 25
    if temp >25:
        print(f"Hey {name}, {temp} degrees is damn hot!")
    else:
        print(f"Hey {name}, {temp} degrees is pretty cool")

# greet()
check_weather(name="Asanga", temp=30) #if you don't assign, it will follow the default order in the functoin def

#How to return values
def do_math(a, b):
    return a + b, a * b

sum_num, multi_num = do_math(a=5, b=10)
print(f"Sum: {sum_num} and Multi: {multi_num}")

# another example
def get_min_max(num):
    return min(num), max(num)

minimum, maximum = get_min_max([5, 2, 8, 1, 9])
print(f"Min :{minimum} and Max :{maximum}")

# another example
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)

