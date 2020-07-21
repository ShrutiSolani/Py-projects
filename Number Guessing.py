import random, time
print("Welcome to number guessing game !!!")
time.sleep(2)
x = random.randint(1, 10)
print("The number is generated!!!")
time.sleep(1)
print("You have 4 chances to guess")
count = 4
while count != 0:
    a = int(input("Guess the number : "))
    if a == x:
        print("You are right, correct number is ", x)
        print("Congratulations! You won")
        break
    elif a > x:
        print("The number is less than ", a)
    else:
        print("The number is greater than ", a)
    count -= 1


