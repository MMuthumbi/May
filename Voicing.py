print("For the Voices")
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
while 1:
    print('Richard Of York Gained Battle in Vain.')
    s = input( )
    speaker.Speak(s)
    