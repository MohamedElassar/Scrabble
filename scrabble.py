import random
import string

WORDLIST_FILENAME = "words.txt"

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def get_words():

    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.read()
    wordlist = line.split("\n")
    inFile.close()
    print("  ", len(wordlist), "words loaded.")
    for i in range(len(wordlist)):
    	wordlist[i] = wordlist[i].lower()
    return wordlist

def calculate_score(word, size):

	total = 0
	for c in word:
		total = total + SCRABBLE_LETTER_VALUES[c]

	bonus = 7 * len(word) - 3*(size - len(word))

	if(bonus > 1):
		return total + bonus
	else:
		return total + 1


def is_Valid(hand, word, wordlist):

	for c in word:
		if(c not in hand):
			return False

	if(word in wordlist):
		return True

	return False

def generate_hand(HAND_SIZE, MAX_CONSONANTS, MAX_VOWELS):

	consonant_count = 0
	vowel_count = 0
	
	alphabet = string.ascii_lowercase
	vow = "aeiou"
	
	hand = []

	while(len(hand) < HAND_SIZE):
		index = random.randint(0,25)
		char = alphabet[index]
		if(char in vow):
			if(vowel_count < MAX_VOWELS):
				hand.append(char)
				vowel_count += 1
		else:
			if(consonant_count < MAX_CONSONANTS):
				hand.append(char)
				consonant_count += 1
	return hand


def display_hand(hand):

	print("Current hand: " + " ".join(hand))


def remove_from_hand(hand, word):

	for c in word:
		for i in range(len(hand)):
			if(c == hand[i]):
				hand.pop(i)
				break

def replay_round():
	
	replay = input("Would you like to replay the hand? ")
	if(replay == "yes"):
		return True
	else:
		return False

def play(hand, wordlist):

	current_hand_size = len(hand)
	total_points = 0
	while(current_hand_size > 0):
		print("************************")
		display_hand(hand)
		inp = input("Please enter a word of '!!' to indicate you are done: ")
		if(inp == "!!"):
			print("Total score for this hand: " + str(total_points))
			break
		else:
			valid = is_Valid(hand, inp, wordlist)
			if(valid):
				word_points = calculate_score(inp, current_hand_size)
				total_points = total_points + word_points
				print(inp + " earned " + str(word_points) + " point. Total: " + str(total_points) + " points")
				remove_from_hand(hand, inp)
				current_hand_size -= len(inp)
			else:
				print("Invalid word. Please try again.")
	
	if(current_hand_size == 0):
		print("Ran out of letter\nTotal score for this hand: " + str(total_points))


def scrabble():

	wordlist = get_words()

	HAND_SIZE = 7
	MAX_CONSONANTS = 4
	MAX_VOWELS = 3

	num_hands = input("Please enter the desired number of hands: ")

	for i in range(int(num_hands)):
		replay = True
		copy = generate_hand(HAND_SIZE, MAX_CONSONANTS, MAX_VOWELS)
		while(replay):
			hand = []
			for i in copy:
				hand.append(i)
			play(hand, wordlist)
			replay = replay_round()

if __name__ == '__main__':
	scrabble()