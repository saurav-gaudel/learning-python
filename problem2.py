# install external mmodule and use it eg. pyttsx3 to convert text to speech
import pyttsx3
engine = pyttsx3.init()
engine.say('Hey Saurav, how are you feeling learning python')

engine.runAndWait()