import random
import time
print('===================')
print('Rock Paper Scissors')
print('===================')

print('1) ✊')
print('2) ✋')
print('3) ✌️')

option = int(input('Choose an answer:'))
cpuOption = (random.randint(1, 3))
retry = True

if cpuOption == option:
    print('Draw')
elif cpuOption == 1:
    if option == 3:
        print('I chose ✊ it breaks ✌️, I win')
    else:
        print('I chose ✊ it\'s covered by ✋, You win')
elif cpuOption == 2:
    if option == 3:
        print('I chose ✋ it\'s cut by ✌️, You win')
    else:
        print('I chose ✋ it covers ✊, I win') 
else: 
    if option == 1:
        print('I chose ✌️ it\'s broken by ✊, You win')
    else:
        print('I chose ✌️ it cuts ✋, I win')