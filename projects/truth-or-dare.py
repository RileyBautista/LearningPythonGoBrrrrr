import random
import time

# Truths and Dares completely stolen from https://github.com/Kaydonbob03/kaydonbot/blob/master/truthordare.json
truths = ['what\'s the most embarrassing thing you\'ve ever done?', 
         'What\'s your biggest fear?', 
         'What\'s one thing you\'d never do, even for a million dollars?', 
         'Have you ever lied to get out of trouble?', 
         'What\'s the biggest lie you\'ve ever told?', 
         'Do you have a secret talent?', 
         'What\'s the worst gift you\'ve ever received?', 
         'What\'s one thing you wish you could change about yourself?', 
         'Who is your secret crush?', 
         'What\'s the most childish thing you still do?', 
         'Have you ever cheated on a test?', 
         'What\'s the biggest mistake you\'ve ever made?', 
         'What\'s the weirdest dream you\'ve ever had?', 
         'Have you ever broken the law?', 
         'What\'s the most embarrassing thing in your room?', 
         'What\'s the worst date you\'ve ever been on?', 
         'What\'s your guilty pleasure?', 
         'Have you ever lied about your age?', 
         'What\'s the biggest misconception about you?', 
         'What\'s the craziest thing you\'ve done in public?', 
         'What\'s the meanest thing you\'ve ever said to someone?', 
         'What\'s something you\'re glad your mom doesn\'t know about you?', 
         'What\'s the worst advice you\'ve ever given someone?', 
         'What\'s the weirdest thing you\'ve ever eaten?', 
         'What\'s the most childish thing you\'re afraid of?']

dares = ["Imitate a celebrity for the next three rounds.",
        "Dance without music for two minutes.",
        "Let someone else style your hair and keep it that way for the rest of the day.",
        "Speak in an accent for the next 10 minutes.",
        "Do 20 pushups.",
        "Eat a spoonful of a condiment of the group's choosing.",
        "Post an embarrassing photo of yourself online.",
        "Wear socks on your hands for the next 15 minutes.",
        "Make up a rap about a person of the group's choosing.",
        "Do your best impression of a baby being born.",
        "Try to juggle 3 items of the group's choosing.",
        "Let the group pose you in an embarrassing position and take a picture.",
        "Use your toes to make a text post on social media.",
        "Hold an ice cube in your hand until it melts.",
        "Try to lick your elbow.",
        "Speak in rhymes for the next 5 minutes.",
        "Do a cartwheel.",
        "Act like a dog for the next minute.",
        "Let someone draw on your face with a pen.",
        "Do your best impression of a mime stuck in a box.",
        "Let the group give you a new hairstyle.",
        "Sing the chorus of a random song loudly.",
        "Talk without closing your mouth.",
        "Walk backwards wherever you go for the next 3 minutes.",
        "Do 10 squats while holding a book above your head."]

value = input('Truth or Dare?').lower()
keep_going = True

while keep_going == True: 
    if value == 'truth':
        print(truths[random.randint(1, 24)])
    elif value == 'dare':
        print(dares[random.randint(1,24)])
    else:
        print("It's literally Truth or Dare, nothing else")
    time.sleep(1)
    retry = input('Retry? Y or N')
    if retry == 'Y':
        time.sleep(1)
    elif retry == 'N':
        keep_going = False
    else: 
        print('Y or N') 
