import random
print("Welcome to hang man!")
word = ["EVAPORATE","COMPUTER","AFTERNOON","MORNING","AWESOME"]
clue =  random.sample(word,1)[0]
string = list(clue)
guessWord = list("_"*len(string))
tries = 6
while(tries!=0 and guessWord != "".join(string)):
	flag = 0
	guess = input("Your guess : ").upper()
	for i in range(0,len(string)):
		if guess == string[i]:
			guessWord[i] = guess
			flag = 1

	if(flag == 0):
		tries = tries -1
		print("Your guessed it wrong , now you have "+str(tries)+" left")
	else:
		print("word after your guess is : "+("".join(guessWord)))
if tries == 0:
	print("Sorry, you lost! You were not able to guess the word.")


