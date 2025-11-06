
# this class name is only used to create an instance
class ValidateData:
    def __init__(self):
        self.errors = []

    def validate_email(self, email):
        if "@" not in email:
            self.errors.append(f"{email} is invalid")
            return False
        return True
    
    def validate_age(self, age):
        if age < 0 or age > 150:
            self.errors.append(f"{age} is invalid")
            return False
        return True
    
    #this is the 'method' that runs self top to bottom
    def check_errors(self):
        return self.errors
    
#let's test by first creating an instance of the class
#this is where we us the class name
validator = ValidateData()

#check email and age by passing invalid info
validator.validate_email(email="email.com")
validator.validate_age(age=200)

#finally, we are callling the main method
print(validator.check_errors())
# remember, the more you run, the more gets added to the instantiated list