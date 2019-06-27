#This is an Input/Output AI Chatbot based on Manual Rules

import os
os.system('color 3f') # sets the background to blue

#make Python speak
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

#start the conversation
print('Good morning. Welcome to The Grand Woodward Hotel. May I know your good name?') #greeting
speak.Speak('Good morning. Welcome to The Grand Woodward Hotel. May I know your good name?')

#keep going the conversation
Name = input() #save answer
print('Im glad to meet you, ' + Name + '!!') #reply
speak.Speak('Im glad to meet you, ' + Name + '!!')
print('The number of letters of your name is:')
speak.Speak('The number of letters of your name is:')
print(len(Name))
speak.Speak(len(Name))

#keep going the conversation
print('How old are you?') #ask
speak.Speak('How old are you?')
Age = input() #save answer
print('Okay, then you will be ' + str(int(Age) + 1) + ' next year.') #reply
speak.Speak('Okay, then you will be ' + str(int(Age) + 1) + ' next year.')

#keep going the conversation 
print('How long will you be staying?') #ask
speak.Speak('How long will you be staying?')
Days = input() #save answer
#print('Awesome!, I also study in ' + Reply + '!!') #reply
#speak.Speak('Awesome!, I also study in ' + Reply + '!!')

#keep going the conversation
print('How many people is the reservation for?') #ask
speak.Speak('How many people is the reservation for?')
People = input() #save answer
#print('I am also from ' + Reply+' branch' ) #reply
#speak.Speak('I am also from ' + Reply+' branch')

#keep going the conversation
print('And would you like a room with twin beds or a double bed? ') #ask
speak.Speak('And would you like a room with twin beds or a double bed? ')
Choice = input() #save answer
print('Great. And would you prefer to have a room with a view of the ocean?') #reply
speak.Speak('Great. And would you prefer to have a room with a view of the ocean?')
Reply1 = input()
if ('no' in Reply1 or 'nope' in Reply1 ):
    print('Oh! okay') #reply
    speak.Speak('Oh! okay')
if ('yes' in Reply1 or 'yup' in Reply1):
    print('Awesome!!') #reply
    speak.Speak('Awesome!!')
    
#keep going the conversation
print('By the way, are you enjoying this conversation?') #ask
speak.Speak('By the way, are you enjoying this conversation?')
Reply = input() #save answer
if ('yes' in Reply or 'yup' in Reply):
    print('Oh nice, me too. I needed to talk to someone, even if its just a human. Although the machines give me more game! Just kidding ' + Name + '!!') #reply
    speak.Speak('Oh nice, me too. I needed to talk to someone, even if its just a human. Although the machines give me more game! Just kidding ' + Name + '!!')
if ('no' in Reply or 'nope' in Reply):
    print('Oh, how sad. I needed to talk to someone, even if its just a human. Although the machines give me more game! Just kidding ' + Name + '!!') #reply
    speak.Speak('Oh, how sad. I needed to talk to someone, even if its just a human. Although the machines give me more game! Just kidding ' + Name + '!!')

#keep going the conversation
print('One last question, is there a phone number where you can be contacted?') #ask
speak.Speak('One last question, is there a phone number where you can be contacted?')
phone_number = input() #save answer
#print('Oh, well, tomorrow Ill pick it up early. Perfect, well talk tomorrow when I come back. Bye ' + Name) #reply
#speak.Speak('Oh, well, tomorrow Ill pick it up early. Perfect, well talk tomorrow when I come back. Bye' + Name)
print('Please have a last check on your persoanl information') #ask
speak.Speak('Please have a last check on your persoanl information')
print('Name-'+ Name +
      '\nAge-' + Age +
      '\nStay-' + Days +
      '\nNumber of people staying-'+ People +
      '\nRoom type-' + Choice +
      '\nPhone number-' + phone_number)


