
my_list = [1, 10, 15, 8, 9, 11, 21, 65, 45, 89, 45, 76, 40, 28, 56, 11, 39, 99, 30]

def fizz_buzz (num):
        if num % 3 == 0 and num % 5 == 0:
            return(" FizzBuzz")
        elif num  % 5 == 0:
            return(" Buzz")
        elif num % 3 == 0:
            return(" Fizz")
        else:
            return(num)

for number in my_list:
    print(fizz_buzz(number))
