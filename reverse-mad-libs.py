# Sources:
# Python Overview: https://www.youtube.com/watch?v=N4mEzFDjqtA
# Mad Lib Ideas: https://codeboom.wordpress.com/2012/11/22/python-madlibs/

# Here are the three strings required for the easy, medium, and hard levels."
easy_prompt = "Computer __1__ is about how to solve __2__, by breaking them into smaller __3__s, and then precisely and mechanically describing a sequence of __4__ that you can use to solve each __3__." 
medium_prompt = "__1__, named after Monty __1__, is a computer programming __2__ that gives us a high-level __2__ to write __3__. An __4__ allows you to write __1__ code. "
hard_prompt = "Without a __1__, a __2__ is useless. The power of a __2__ is that it can do anything--it is a universal __3__ that can be __1__med to any __4__ that we can imagine."

# Here are the answers for those strings.
easy_answers = ["science", "problems", "piece", "steps"]
medium_answers = ["Python", "language", "programs", "editor" ]
hard_answers = ["program", "computer", "machine", "computation"]

def level_selector():
	"""This allows the user to select the difficulty, and outputs that difficulty to 'game_magic'"""
	easy = ["easy", "Easy", "EASY"]
	medium = ["medium", "Medium", "MEDIUM"]
	hard = ["hard", "Hard", "HARD"]
	user_input = raw_input("Select your level of difficulty: easy / medium / hard" + "\n")
	if user_input in easy:
		print "\n" + easy_prompt
		return game_magic (easy_prompt, easy_answers)
	elif user_input in medium:
		print "\n" + medium_prompt
		return game_magic (medium_prompt, medium_answers)
	elif user_input in hard:
		print "\n" + hard_prompt
		return game_magic(hard_prompt, hard_answers)
	else:
		print "Please try again." + "\n"
		level_selector ()

def game_magic(prompt, answers):
	"""This is the loop structure that fills in the blanks of the prompt with the answers provided."""
	i = 0
	while i < len(answers):
		user_input = raw_input("What is the answer to __" + str(i + 1) + "__ ?" + "\n")
		if user_input == answers[i]:
			print "Nice job!" + "\n"
			i += 1
			prompt = prompt.replace("__" + str(i) + "__", user_input)
			print prompt
		else:
			print "Incorrect answer." + "\n" + prompt
	print "Good game!"

def play_game():
	"""This is the function that calls upon the other functions to provide game play."""
	level_selector()
	yes = ['yes', 'Y', 'YES']
	no = ['no', 'N', 'NO']
	user_input = raw_input("Would you like to play another round?: yes / no ")
	if user_input in yes:
		play_game()
	else:
		print "Thanks for playing!" 

play_game()





