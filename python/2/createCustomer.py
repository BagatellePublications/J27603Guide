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
		password = raw_input('Enter Password : ')
		if secure(password):
			return password
		else:
			print("%s must contain at least one number and one capital letter" %(password))

def setupAccount():
	account = []
	username = raw_input ('Username : ')
	account.append(username)
	password = getPassword()
	account.append(password)
	name = raw_input('Name : ')
	account.append(name)
	address = raw_input('Address : ')
	account.append(address)
	dob = raw_input('Date of Birth [dd-mm-yyyy] : ')
	account.append(dob)
	gender = raw_input('Gender M/F : ')
	account.append(gender)

	interests = []
	moreInterests = True
	while moreInterests:
		interest = raw_input('Interests, empty string to quit : ')
		if interest == "":
			moreInterests = False
		else:
			interests.append(interest)

	account.append(interests)
	return account

def getSingleFilm():
	film = []
	name = raw_input('Film name : ')
	film.append(name)

	genres = []
	moreGenres  = True
	while moreGenres:
		genre = raw_input('Genre (terminate entries by hitting Enter on its own) : ')
		if genre == "":
			moreGenres = False
		else:
			genres.append(genre)
	film.append(genres)

	actors = []
	moreActors = True
	while moreActors:
		actor = raw_input('Actor (terminate entries by hitting Enter on its own) : ')
		if actor == "":
			moreActors = False
		else:
			actors.append(actor)
	film.append(actors)

	director = raw_input('Director : ')
	film.append(director)

	like = raw_input('Like (Y/N) : ')
	film.append(like)
	return film

def getNFilms(n):
	films = []
	for _ in range(n):
		film = getSingleFilm()
		films.append(film)
	return films

def createCustomer(n):
	customer = setupAccount()
	films = getNFilms(n)
	customer.append(films)
	return customer

# main code starts here
# let's create one customers who is required to enter 2 films
Customers = []
for _ in range(1):
	customer = createCustomer(2)
	Customers.append(customer)

print (Customers)
