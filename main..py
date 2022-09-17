import random
import string
import pyfiglet

#title  
result = pyfiglet.figlet_format("Password Generator")
print(result)



#take length input from user
length = input("Please enter the length of the password you would like: ")
#generate all lowercase letters from alphabet
lower = string.ascii_lowercase
#generate all uppercase letters from alphabet
upper = string.ascii_uppercase
#generate all integers from 0 to 9
num = string.digits
#generate a set of symbols
symbols = string.punctuation
#add all generated sets together onto one string
all = lower + upper + num + symbols
#from that string, at random,
#with the length provided from the user, create another string
temp = random.sample(all, int(length))
password = "".join(temp)
print(password)

