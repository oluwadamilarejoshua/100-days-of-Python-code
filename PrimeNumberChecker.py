
from curses.ascii import isprint
from operator import truediv


number = int(input("What number do you wish to check?"))

def prime_number_checker(number):
    if number == 1 or number == 2 or number == 3 or number == 5 or number == 7:
        print(f"{number} is a prime number")
    else:
        the_number = number - 1
        for i in range(2, the_number):
            divisible = False
            while divisible == False:
                if number % i == 0:
                    divisible = True
                    print(f"{number} is a prime number")
                    break
                else:
                    print(f"{number} is not a prime number")

def the_prine_checker(number):
    is_prime = True
    for i in range(2, number - 1):
        if number % i == 0:
            is_prime = False
        else:
            is_prime = True
    if is_prime == True:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
