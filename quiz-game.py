print('Welcome to my computer quiz!')

playing = input("Do you want to play my game? ")

score = 0

if(playing.lower() == 'yes'):
    print('Ok, Lets play :)')

    #Question 1
    while True:
        answer = input("What does CPU Stand for : ")
        #Check to make sure user entered value
        if not answer:
            continue

        if(answer.lower() == 'central processing unit'):
            print('correct')
            score +=1
            
        else:
            print('incorrect, correct answer is : "central processing unit".')
        break
    #Question 2
    while True:
        answer = input("What does GPU Stand for : ")
        #Check to make sure user entered value
        if not answer:
            continue

        if(answer.lower() == 'graphics processing unit'):
            print('correct')
            score +=1
        else:
            print('incorrect, the corrent answer is : "graphics processing unit".')
        break
    #Question 3
    while True:
        answer = input("What does RAM Stand for : ")
        #Check to make sure user entered value
        if not answer:
            continue

        if(answer.lower() == 'random access memory'):
            print('correct')
            score +=1
        else:
            print('incorrect, correct answer is : "random access memory".')
        break
    #Question 4
    while True:
        answer = input("What does PSU Stand for : ")
        #Check to make sure user entered value
        if not answer:
            continue

        if(answer.lower() == 'power supply unit'):
            print('correct')
            score +=1
        else:
            print('incorrect, correct answer is : "power supply unit".')
        break
else:
    print('Ok, quitting game!!!')
    quit()

print()
print('Game Over')
print('You scored : ' + str(score) + '/4, well done.')
quit()