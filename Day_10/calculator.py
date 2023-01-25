from art import logo
def addition(num1,num2):
  return num1+num2

def subtraction(num1,num2):
  return num1-num2

def multiplication(num1,num2):
  return num1*num2

def division(num1,num2):
  return num1/num2

def calc():
    print(logo)
    your_decision = 'yes'
    menu = {'+':addition,'-':subtraction,'*':multiplication,'/':division}
    num1 = float(input("Enter the first number "))
    while your_decision == 'yes':
        print('This are the options available ')
        for i in menu:
            print(i)
        choice = input('Enter your choice :- ')
        num2 = float(input("Enter the number "))
        answer = menu[choice](num1,num2)
        print(f"{num1} {choice} {num2} = {answer}")
        your_decision = input("If you wish to continue with your calculation type 'yes' if you want to stop the calculation type 'no' and if you want to start all new type 'new' ")
        if your_decision == 'yes':
            num1 =answer
        elif your_decision == 'new':
            calc()

calc()
  