import string
from random import *
import random
b=[]
min_char = 8
max_char = 12
##string.ascii letters returns all characters a-z in capital and small cases
##string.punctuation returns punctuation marks like !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
##string.digits returns digits 0-9
allchar = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
print ("This is your password : ",password) 

##simply-break down of above code
##another idea to create password
##randint creates random range between 8 to12 digits
##random.choice returns only one value so we have to append it
##or join with previous value to make password length between 8 to 12
for a in range(randint(8,12)):
 b.append(random.choice(allchar
  ))
 
print(len(b))
print("the radom password is ") 
print("".join(b))