"""
Ramlaal - The AI

This is an AI program / project written in Python3 programming language. This uses the same basic method for every desktop assistant written in Python3 and are available on the internet for beginners to practice. But, this version of AI is very cranky and shithead. It may use abusive tone of words to you and also get into arguments sometime. F words are commonly used by our very own Ramlaal. But, this ridiculous behavious does not effect the working and functionality of our AI, the tasks assigned are still completed by it. But, the works are done with some swearing.

Dependencies :
Linux base (operating system type)
espeak, alsa-utils, ffmpeg and libespeak1 (software utilities required)
pyttsx3 and SpeechRecognition (Python3 modules required)

Author : Rishav Das (https://github.com/rdofficial/)
Created on : June 7, 2021

Last modified by : -
Last modified on : -

Authors contributed to this script (Add your name below if you have contributed) :
1. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
"""

# Importing the required functions and modules
try:
	import pyttsx3
except Exception as e:
	# If there are errors encountered during the importing of modules, then we display the error message on the console screen and exit

	print(f'[ Error : {e} ]')
	exit()

def speak(text):
	""" """

	# Defining the engine for the speech by which the AI will speak the output or any kind of message to the user
	engine = pyttsx3.init()
	engine.say(text)
	engine.runAndWait()

def main():
	while True:
		speak('Welcome sir, I am Ramlaal. Ofcourse, Ramlaal is my name. Sounds odd! After all, who the fuck names their child such a dumbass name. Ramaal! Really! What the fuck!. Anyways, whats your name maalik?')
		input()

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