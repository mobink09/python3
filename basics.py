# t learn basics + move to DS + explore python + competitve programming deep and deep

# print and geting information from users

# print('***********************Hello World In python**************************')
# userInput = input('Say Somethings ')
# print('User Says : ' + userInput)

# assigning the value

# num = 1
# print(num)
# num = num + 10
# print(num)

# reserved words -- python have lots of reserved words which we can't used in place of variables because its value is already defined in python and they can't be changed

# conditionals statement : - in which we examined the value based on conditions

# num = input("enter number between 0 and 20 ")  # user enter num
# inum = int(num)

# if inum < 20:
#     print('Num is less than 20 num itself is :', num)
# else:
#     print('Num grater or equal to 20 num itself is : ', num)
# print('Well you done that')


# loop: iterate counting or repeatative task

# num = 5
# while num < 10:
#     print(num)
#     num = num + 1


# mathematical operator: we know well this section bcz we know maths of class 5
# addition  +
# subtraction -
# multiplication *
# division /
# power **   e.g print(2 ** 3)
# modulo operator
# modulo operator or remainder operator
# print(2 ** 3)
# print(3 % 2)
# mukeshTotal = 1 + 5
# print(mukeshTotal)


# string concatenation
# firstName = input("Enter your first name ")
# lastName = input("Enter your last name ")
# fullName = firstName + " "+lastName
# print(fullName)

# type of data .... extra in js to find out which  type of data is is we used typeof operator
# but in python type
# typeChecker = 10.4
# print(type(typeChecker))

# convertor data types

def dataChecker(userData):
    if type(userData) == int:
        print(" User Data is Integer: ", userData)
        print("Counting of number from userData number to 0")
        while userData >= 0:
            print("userData number is : ", userData)
            userData = userData - 1
    elif type(userData) == float:
        print("User Data is In Float or Decimal Values : ", userData)
        intNum = int(userData)
        while intNum >= 0:
            print("userData number is : ", intNum)
            intNum = intNum - 1
    else:
        print("User Data is in String :", userData)
        strInNumber = len(userData)
        while strInNumber >= 0:
            print("String in Number is : ", strInNumber)
            strInNumber = strInNumber - 1


dataChecker(5.7)
