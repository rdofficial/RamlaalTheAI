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
1. Added the wishTheUser() function to the script, where our AI wishes the user as well as asks for their well being.

Authors contributed to this script (Add your name below if you have contributed) :
1. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
"""

# Importing the required functions and modules
try:
	# Importing the pre-installed modules
	from datetime import datetime

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

		speak('Soo prabhat Saheb! I hope you have a good day Saheb.')
	elif time >= 12 and hour < 18:
		# If the timing is between 12 and 18 o clock, then we wish good afternoon

		speak('Subh din Saheb! I hope your day has went fine till now.')
	else:
		# If there are any other timings, then we wish good evening straight

		speak('Andheri shyaam mei, diya tere haath mein! Saheb? I hope your day has went fine till now.')
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