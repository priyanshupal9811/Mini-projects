import random
print("Choose Difficulty: Easy(1), Medium(2), Hard(3)")
choice = input("enter choice:")
if choice =="1":
    n = random.randint(1,20)
elif choice=="2":
    n = random.randint(1,50)
else:
    n = random.randint(1,100)
a = -1
max_attempts = 10
guesses = 0
while(a != n and guesses < max_attempts):
    guesses += 1
    a = int(input("Guess the Number:"))
    if(a > n):
        print("Enter lower Number Please!")
    elif(a<n):
        print("Enter higher Number Please!")
    else:
        print(f"You have guessed the Number Correctly in {guesses} Attempt")
if (guesses == max_attempts and a != n):
    print(f"Game Over! the Number was {n}")
   

