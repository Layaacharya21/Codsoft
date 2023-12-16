import random
import array as arr

len=int(input("Enter length of the password: "))

digits=['0','1','2','3','4','5','6','7','8','9']
lcase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
ucase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
Symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
           '*', '(', ')', '<']

clist=digits+lcase+ucase+Symbols

temp=""
for i in range(len):
    temp=temp+random.choice(clist)
    templist=arr.array('u',temp)
    random.shuffle(templist)

password=""
for i in templist:
    password=password+i

print(password)
