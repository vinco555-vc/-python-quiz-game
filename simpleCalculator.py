while True:
    num1 = input("Enter 1st number to calculate : ")
    if not num1:
        print("Please enter a 'VALUE' for 1st number.")
        continue
    elif not num1.strip().isdigit():
        print("Please enter a 'DIGIT' for 1st number.")
        continue
    break

while True:
    num2 = input("Enter second number to calculate : ")
    if not num2:
        print("Please enter a 'VALUE' for 2nd number.")
        continue
    elif not num2.strip().isdigit():
        print("Please enter a 'DIGIT' for 2nd number.")
        continue
    break

while True:
    calcType = input("Enter calculation type (+,-,*,/) : ")
    if (calcType != '+' and calcType != '-' and calcType != '*' and calcType != '/'):
        print("Enter calculation type (+,-,*,/)")
        continue
    break

if calcType == '+':
    answer = int(num1) + int(num2)
elif calcType == '-':
    answer = int(num1) - int(num2)
elif calcType == '*':
    answer = int(num1) * int(num2)
else:
    answer = int(num1) / int(num2)
    
print(str(num1) + " " + calcType + " " + str(num2) + " = " + str(answer))

