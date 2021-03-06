def secure(password):
	nums = set('0123456789')
	caps = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	foundNumber = False
	foundCaps = False

	for n in password:
		if (n in nums):
			foundNumber = True
		if (n in caps):
			foundCaps = True

	if foundNumber and foundCaps:
		return True
	else:
		return False

def getPassword():
	while True:
		password = input('Enter Password : ')
		if secure(password):
			return password
		else:
			print("%s must contain at least one number and one capital letter" %(password))

def setupAccount():
	account = []
	username = input ('Username : ')
	account.append(username)
	password = getPassword()
	account.append(password)
	name = input('Name : ')
	account.append(name)
	address = input('Address : ')
	account.append(address)
	dob = input('Date of Birth [dd-mm-yyyy] : ')
	account.append(dob)
	gender = input('Gender M/F : ')
	account.append(gender)

	interests = []
	moreInterests = True
	while moreInterests:
		interest = input('Interests, empty string to quit : ')
		if interest == "":
			moreInterests = False
		else:
			interests.append(interest)

	account.append(interests)
	return account

# main code starts here
Account = setupAccount()
print(Account)
