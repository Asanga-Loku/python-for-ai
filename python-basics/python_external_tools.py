# Instructions are at https://python.datalumina.com
#

#import something that is alrady internal to python
import math
#now you can use items as math.sqrt

#or 
from math import sqrt, pi
#now just use sqrt

#another example
import random

number = random.randint(1, 10)
choice = random.choice("apple", "banana", "orange")

# another - this one for the operating system
import os
current_dir = os.getcwd() #current working directory
print(current_dir)

#import with alias
import pandas as pd
df = pd.DataFrame(data)

# this is resource consuming
#from math import *

""" external libraries like pandas must first be installed in the terminal
pip install pandas 

Have a look at the details of the lib 
you can install older versions, it will uninstall previous ones
pip install requests==2.28.0

you can also install multiple packages
pip install pandas numpy matplotlib

if you do
pip freeze > requirements.txt
it will copy all the packages and their versions for later

when someon gets your project, they run
pip install -r requirements.txt
this intalls all the packages at once

Use chatgpt to find the right package for whatever you want to do

if you import a variable 
And then define the same variable, the old imported one will be overwritten
"""


