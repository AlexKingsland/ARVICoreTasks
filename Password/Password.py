import random

password = [];
master = []

specialChar = ['|', '@', '.', ',', '?', '~', '#', '%', '^', '&', '*', '(', ')', '{', '}', '[', ']', '\\', '=', '{'];

length = random.randint(11,23);

lowerCase = [];
upperCase = [];
numbers = range(10);

for i in range(26):
	lowerCase.append(chr(i+97))
	master.append(chr(i+97))

for i in range(26):
	upperCase.append(chr(i+65))
	master.append(chr(i+97))

for i in specialChar:
	master.append(i);

for i in range(len(numbers)):
	master.append(i)


spec = specialChar[random.randint(0,len(specialChar)-1)];
low = lowerCase[random.randint(0,len(lowerCase)-1)];
upper = upperCase[random.randint(0,len(upperCase)-1)];
num = numbers[random.randint(0, len(numbers)-1)];

password.append(specialChar[random.randint(0,len(specialChar)-1)])
password.append(lowerCase[random.randint(0,len(lowerCase)-1)])
password.append(upperCase[random.randint(0,len(upperCase)-1)])
password.append(numbers[random.randint(0,len(numbers)-1)])

for i in range(length-4):
	password.append(master[random.randint(0,len(master)-1)])
	r1 = random.randint(0,len(password)-1)
	r2 = random.randint(0,len(password)-1)
	temp = password[r1]
	password[r1] = password[r2]
	password[r2] = temp

code = ""
for i in password:
	code = str(code) + str(i)

print(code)

