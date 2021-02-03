#importing the library
import win32com.client as wc
speaker = wc.Dispatch('SAPI.spVoice') #defining the speaker
speaker.Speak("Hello World! It's Working")
#run