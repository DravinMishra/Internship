# Write a python program to find the factorial of a number

# number = int(input("Enter a number : "))
# if number < 0 :
#     print("Please enter a positive integer")
# elif number == 0 or number == 1 :
#     number = 1
#     print(number)
# else :
#     number = number * (number - 1)
#     print(number)

def factorial(number) :
    if number < 0 :
        return ("Please enter a positive integer")
    elif number == 0 or number == 1 :
        return 1
    else :
        a = 1
        for i in range (2 , number+1) :
            a *= i
        return a
number = int(input("Enter a number : "))
b = factorial(number)
print(f'factorial of given number is : {b} ')