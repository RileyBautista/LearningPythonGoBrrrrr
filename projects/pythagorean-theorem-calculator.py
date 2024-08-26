print('==============================')
print('Pythagorean Theorem Calculator')
print('==============================')

print('Literally to practice my coding skills, if you need to legitimately use this that\'s sad and pay attention better?')

legA = 0
legB = 0
hypotenuse = 0

grah = input('Are you solving for hypotenuse or leg?').lower()

if grah == 'hypotenuse':
    legA = int(input('What is the value of Leg A?'))
    legB = int(input('What is the value of Leg B'))
    hypotenuse = (legA ** 2 + legB ** 2) ** 0.5
    print('The value of the hypotenuse is', hypotenuse)
elif grah == 'leg':
    legA = int(input('What is the value of the Leg?'))
    hypotenuse = int(input('What is the value of the Hypotenuse?'))
    if hypotenuse < legA:
        print('Invalid Triangle')
    else:
        legB = ((hypotenuse ** 2)-(legA ** 2)) ** 0.5
        print('The value of the missing leg is', legB)
elif grah == '0':
    print('Leg or Hypotenuse')

