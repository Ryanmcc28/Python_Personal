import random
import string


# 6 digit password cracker

'''
password = 83950
count = 0
while count != password:
   #count = random.randint(0,100000)

       #or
    #count += 1
  print(count)
'''

#3 letter password cracker

password = "pugs"
guess = ""
count = 0
char_range = string.ascii_letters.lower()

while guess != password.lower():
    count += 1
    char1 = random.randint(0, len(char_range)-1)
    char2 = random.randint(0, len(char_range)-1)
    char3 = random.randint(0, len(char_range)-1)
    char4 = random.randint(0, len(char_range)-1)

    guess = char_range[char1] + char_range[char2] + char_range[char3] + char_range[char4]

    print(guess)
    
print(str(count) + " attempts")

