num1IsInt = True
num2IsInt = True
answerIsInt = True

while True:
    num1 = input("Enter 1st number to calculate : ")
    if not num1:
        print("Please enter a 'VALUE' for 1st number.")
        continue
    else:
        try:
            int(num1)
        except ValueError:
            try:
                float(num1)
                num1IsInt = False
            except:
                print("Please enter a 'DIGIT' for 1st number.")
                continue
    break

while True:
    num2 = input("Enter 2nd number to calculate : ")
    if not num2:
        print("Please enter a 'VALUE' for 2nd number.")
        continue
    else:
        try:
            int(num2)
        except ValueError:
            try:
                float(num2)
                num2IsInt = False
            except:
                print("Please enter a 'DIGIT' for 2nd number.")
                continue
    break

while True:
    calcType = input("Enter calculation type (+,-,*,/) : ")
    if (calcType != '+' and calcType != '-' and calcType != '*' and calcType != '/'):
        print("Please Enter a calculation type (+,-,*,/)")
        continue
    break

if num1IsInt:
    if num2IsInt:
        if calcType == '+':
            answer = int(num1) + int(num2)
        elif calcType == '-':
            answer = int(num1) - int(num2)
        elif calcType == '*':
            answer = int(num1) * int(num2)
        else:
            answer = int(num1) / int(num2)
    else:
        if calcType == '+':
            answer = int(num1) + float(num2)
        elif calcType == '-':
            answer = int(num1) - float(num2)
        elif calcType == '*':
            answer = int(num1) * float(num2)
        else:
            answer = int(num1) / float(num2)
else:
    if not num2IsInt:
        if calcType == '+':
            answer = float(num1) + float(num2)
        elif calcType == '-':
            answer = float(num1) - float(num2)
        elif calcType == '*':
            answer = float(num1) * float(num2)
        else:
            answer = float(num1) / float(num2)
    else:
        if calcType == '+':
            answer = float(num1) + int(num2)
        elif calcType == '-':
            answer = float(num1) - int(num2)
        elif calcType == '*':
            answer = float(num1) * int(num2)
        else:
            answer = float(num1) / int(num2)


#convert answer back to a string, to we can try to convert to int to find out datatype
answer = str(answer)

try:
    int(answer)
except ValueError:
    answerIsInt = False
    answer = float(answer)

if answerIsInt:
    print(str(num1) + " " + calcType + " " + str(num2) + " = " + str(answer))
else:
    answer = "{:.2f}".format(answer)
    print(str(num1) + " " + calcType + " " + str(num2) + " = " + answer)
    


