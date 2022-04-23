import haversine as hs
import csv

f1 = open('countries.csv')
csvreader = csv.reader(f1)

header = next(csvreader)

rows = []
for row in csvreader:
	rows.append(row)
f1.close()

possible_answers = []
possible_answers2 = []
next_guess = ''
guesses = 1

while True:
	guesses += 1
	if next_guess:
		guess = next_guess
	else:
		guess = input('Enter your guess: ').title().strip()
	distance_left = int(input('Enter how far you are in km: '))

	position = int([i for i, lst in enumerate(rows) if guess in lst][0])

	for country, lat, lon in rows:
		guessed_coordinates = (float(rows[position][1]), 
			float(rows[position][2]))
		next_country = (float(lat), float(lon))
		distance = hs.haversine(guessed_coordinates, next_country)
		
		if abs(distance_left - distance) < 25:
			possible_answers.append(country)

		elif abs(distance_left - distance) < 50:
			possible_answers.append(country)

	if possible_answers2:
		for i in possible_answers:
			if i not in possible_answers2:
				possible_answers.remove(i)
				continue

	if len(possible_answers) == 1:
		print('\nThe answer is ' + str(possible_answers[0]).title())
		print('\nWoohoo!')
		print('\nIt took ' + str(guesses) + ' guesses.')
		break

	if possible_answers:
		print('\nIt could be one of these countries: ' + 
			str(possible_answers))
		next_guess = input('\nWhat was your next guess: ').title().strip()
		check = input('\nWas your next guess right (y/n)? ').upper().strip()

		if check == 'Y':
			print('\nWoohoo!')
			print('\nIt took ' + str(guesses) + ' guesses.')
			break
		else:
			possible_answers.remove(next_guess)
			possible_answers2 = possible_answers
			print("\nLet's try again.")
			possible_answers2 = possible_answers
			possible_answers = []
	else:
		print('\nThere seems to be an issue.'
			'\nPlease make sure you spelled the country correctly'
			'and entered the correct distance in km.')
		print('\n')	