"""
A python script tells you if number is prime or not

@usage python3 prime_number.py "7"
"""


def main():

    # Welcome message
    print("Welcome to prime number checker :)")

    # takes integer input from user
    number = int(input("Enter a number: "))

    # if-elif statement
    if (number == 1):
        print("1 is not a prime number")
    elif (number > 1):
        for num in range(2, number):  # loop through each number
            if (number % num == 0):  # if remainder is 0 then not prime
                print(f"{number} is not a prime number")
                break
        else:
            print(f"{number} is prime number")

    # if number les than 1, print this
    else:
        print(f"{number} is not prime number")


if __name__ == "__main__":
    main()
