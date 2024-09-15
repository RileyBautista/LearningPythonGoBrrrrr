import random
print('===================')
print('Rock Paper Scissors')
print('===================')

print('1) ✊')
print('2) ✋')
print('3) ✌️')

player = int(input('Pick A Number:'))
computer = (random.randint(1, 3))

if computer == player:
    print('Draw')
elif computer == 1:
    if player == 3:
        print('You Chose ✌️ \nCPU Chose ✊ \nCPU wins')
    else:
        print('You Chose ✋ \nCPU Chose ✊ \nYou win') 
elif computer == 2:
    if player == 3:
        print('You Chose ✌️ \nCPU Chose ✋ \nYou win') 
    else:
        print('You Chose ✊ \nCPU Chose ✋ \nCPU wins')  
else: 
    if computer == 1:
        print('You Chose ✊ \nCPU Chose ✌️ \nYou win')  
    else:
        print('You Chose ✋ \nCPU Chose ✌️ \nCPU wins')
