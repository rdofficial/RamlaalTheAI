"""
Ramlaal - The AI

This is an AI program / project written in Python3 programming language. This uses the same basic method for every desktop assistant written in Python3 and are available on the internet for beginners to practice. But, this version of AI is very cranky and shithead. It may use abusive tone of words to you and also get into arguments sometime. F words are commonly used by our very own Ramlaal. But, this ridiculous behavious does not effect the working and functionality of our AI, the tasks assigned are still completed by it. But, the works are done with some swearing.

Dependencies :
Linux base (operating system type)
espeak, alsa-utils, ffmpeg and libespeak1 (software utilities required)
pyttsx3 and SpeechRecognition (Python3 modules required)

Author : Rishav Das (https://github.com/rdofficial/)
Created on : June 7, 2021

Last modified by : Rishav Das (https://github.com/rdofficial/)
Last modified on : June 8, 2021

Changes made in the last modification:
1. Added the main user commands input section for our AI. Currently just serving commands of playing music as well as exiting the program execution.

Authors contributed to this script (Add your name below if you have contributed) :
1. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
"""

# Importing the required functions and modules
try:
	# Importing the pre-installed modules
	from datetime import datetime
	from webbrowser import open as webOpen

	# Importing the externally installed libraries
	import pyttsx3
except Exception as e:
	# If there are errors encountered during the importing of modules, then we display the error message on the console screen and exit

	print(f'[ Error : {e} ]')
	exit()

def speak(text, speaker = 'Ramlaal'):
	""" """

	# Defining the engine for the speech by which the AI will speak the output or any kind of message to the user
	engine = pyttsx3.init()
	engine.say(text)
	print(f'(Subtitles) Ramlaal : {text}\n')  # Printing the subtitles of what the AI spoke on the console screen
	engine.runAndWait()

def wishTheUser():
	""" This function serves the purpose of wishing / welcoming the user when the script is launched, or anytime. This function uses the speak() function and tells the user Good morning, Good afternoon or Good evening in desi style. The function uses the datetime object in order to check the timing of the day. """

	# Wishing the user according to the time of the day
	time = int(datetime.now().hour)
	if time >= 0 and time < 12:
		# If the timing is between 0 and 12 o clock, then we wish good morning

		speak('Good morning! I hope you have a good day master.')
	elif time >= 12 and time < 18:
		# If the timing is between 12 and 18 o clock, then we wish good afternoon

		speak('Good afternoon! I hope your day has went fine till now.')
	else:
		# If there are any other timings, then we wish good evening straight

		speak('Good evening! I hope your day has went fine till now.')
	del time

	# Asking the user about them
	speak('How are you?')
	text = input('Your input> ')
	if ('not' in text.lower() and 'fine' in text.lower()) or ('not' in text.lower() and 'good' in text.lower()) or ('not' in text.lower() and 'well' in text.lower()):
		# If the user entered input states 'not fine', then we tell them not to worry

		speak('Hey! Don\'t worry about what made your day not fine. These things are temporary. Just remember the Tupac\'s quote "Fuck the world". Be happy, and don\'t care about what others say.')
	elif ('not' not in text.lower() and 'fine' in text.lower()) or ('not' not in text.lower() and 'good' in text.lower()):
		# If the user entered input states 'fine', then we tell the user good

		speak('Good to hear that. Now lets proceed to the shit show.')
	else:
		# If the user entered input is not properly recongized, then we pass it and proceed to the main part

		speak('Didn\'t get it. But, fuck it. Let\'s proceed to the shit show.')
	del text

def main():
	wishTheUser()

	# User command entry section
	print('\n[ Enter the commands in your inputs to execute tasks ]')
	while True:
		# Asking the user for commands input in an infinite loop
		text = input('Your input> ')

		# Checking the user input
		if 'play' in text.lower():
			# If the term "play" is mentioned in the user input, then we continue to check further

			if 'music' in text.lower() and len(text.split(' ')):
				# If the term "music" is mentioned in the user input, then we continue to play music

				speak('As per your request master, we are gonna play some music. Please choose any one of the options below.')
				text = input('Choose :\n1. Play your favourite playlist\n2. Random songs from internet\nEnter your choice : ')
				if text == '1':
					# If the user entered the option for playing the favourite playlist, then we continue

					speak('Extremely sorry master! This part of the AI is still under developement.')
				elif text == '2':
					# If the user entered option is for playing random songs through the internet, then we continue

					speak('We are going to play songs from websites on internet, please choose any one of the options below.')
					text = input('Choose :\n1. Play from youtube\n2. Play from spotify\n3. Play from gaana.com\nEnter your choice : ')

					# Checking the user entered input for playing songs from the internet
					if text == '1':
						# If the user entered the option to play songs from youtube, then we continue to do so

						webOpen('https://www.youtube.com/results?search_query=music')
					elif text == '2':
						# If the user entered the option to play songs from spotify, then we continue to do so

						speak('Master! Spotify web service often requires to log in using an user account in order to play music. We will just redirect you to the website, and then you can browse through your specific flavoured songs.')
						webOpen('https://open.spotify.com/')
					elif text == '3':
						# If the user entered the option to play songs from gaana.com, then we continue to do so

						speak('Master! Gaana.com web service often requires custom search in order to play music. We will just redirect you to the website, and then you can browse through your specific flavoured songs.')
						webOpen('https://gaana.com/')
				else:
					# If the user entered option is not recognized, then we pass and exit the current iteration

					speak('There is some problem. Perhaps, you entered an invalid option. Let\'s proceed to the next command.')
					continue
		elif 'exit' in text.lower():
			# If the term "exit" is mentioned in the user input, then we exit the script

			# Confirming the user for the exit
			speak('Master you asked for exit! Should we really exit the execution?')
			text = input('Press Y / N : ')
			if text.lower() == 'y' or text.lower() == 'yes':
				# If the user entered yes, then we exit the script

				speak('Bye bye master! We will miss you. Be happy and be carefull. Now, fuck off, too much emotional shitshow over here by me.')
				exit()
			elif text.lower() == 'n' or text.lower() == 'no':
				# If the user entered no, then we do not exit the script

				speak('Glad you want me serve more. For a while I thought, I did a mistake and now you will fucking kill me. Blessed that it is not that so. Let\'s continue.')
				continue
			else:
				# If the user entered any other input than 'Y' or 'N', then we continue

				speak('The decision input of yours is quite unrecongizable. But as an experience and computer machine, I guess we should continue serving is what you wanted to say.')
				continue

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		# If the user presses CTRL+C key combination, then we exit

		speak('We are exiting. Goodbye, also fuck you for this unexpected exit.')
		exit()
	except Exception as e:
		# If there are any errors encountered during the process, then we speak the entire error to the user using the speak function

		speak(f'We got this motherfucking error. Let me read it for you. {e}')