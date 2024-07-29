import random
import string
a=int(input("Enter the size of the password:"))
char=string.ascii_letters
char+=string.digits
char+=string.punctuation
passkey=""
for i in range(a):
    passkey+=random.choice(char)
print("Generated password is",passkey)