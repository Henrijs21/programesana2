import random 
number = random.randint(1, 100)
guess = 0
tries = []


while guess != number:
    if guess < number:
        print("pameiģini lielāku skaitli.")
    else:
        print("pameiģini mazāku skaitli.") 
    guess = int(input("Uzmini skaitli: "))
    tries.append(guess)
else:
   print(f"You win from {len(tries)} tries!")
   print("Here is you guessing history")
   print(tries)

   sun_of_diffrence = 0 
   for t in tries:
       sun_of_diffrence += abs(t-number)
   print(f"average diffrence was{sun_of_diffrence/len(tries)}")
