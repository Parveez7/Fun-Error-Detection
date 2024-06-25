import os
try:
    print("hi") #this is a sample code
    #code here
except:
    x="sample message" #message here
    command = f'''PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}');"'''
    os.system(command)