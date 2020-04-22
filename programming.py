print('Hello World')

print('What is your name?')
name = input()
print('Hello ' + name +'!')

print('Give me a number.')
number = int(input())
sum = 0
for i in range(1,  number + 1):
    sum = sum + i

print('Sum from 1 to', number, 'is', sum)



## find the secret number

secret_number = 5
current_tries = 0

print('Guess a number')
guess = int(input())
current_tries = current_tries + 1

while guess != secret_number:
   
    if guess > secret_number:
        print('Your number is too large! Guess again!')
        guess = int(input())
    if guess < secret_number:
        print('Your number is too small! Guess again!')
        guess = int(input())
    current_tries = current_tries + 1
else:
    print("Congrats! You found the secret number after", current_tries, "guesses")


## factorial

n = int(input())

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial (n-1)

print (factorial(n))

factorial_of_10 = factorial (10)
print(factorial_of_10)
