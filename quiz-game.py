print('Welcome to my computer quiz!')

playing = input("Do you want to play my game? ")

score = 0;

if(playing.lower() == 'yes'):
    print('Ok, Lets play :)')

    #Question 1
    answer = input("What does CPU Stand for : ")

    if(answer.lower() == 'central processing unit'):
        print('correct')
        score +=1
    else:
        print('incorrect, correct answer is : central processing unit.')

    #Question 2
    answer = input("What does GPU Stand for : ")

    if(answer.lower() == 'graphics processing unit'):
        print('correct')
        score +=1
    else:
        print('incorrect, correct answer is : graphics processing unit.')

    #Question 3
    answer = input("What does RAM Stand for : ")

    if(answer.lower() == 'random access memory'):
        print('correct')
        score +=1
    else:
        print('incorrect, correct answer is : random access memory.')

    #Question 4
    answer = input("What does PSU Stand for : ")

    if(answer.lower() == 'power supply unit'):
        print('correct')
        score +=1
    else:
        print('incorrect, correct answer is : power supply unit.')
else:
    print('Ok, quitting game!!!')
    quit()
print('Game Over')
print('You scored : ' + str(score))
quit()