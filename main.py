import random 

repeat = True
while repeat:
    number = random.randint(1, 1000000)
    tries = 0 
    guess = 0

    
    while guess != number:
        if guess < number:
            print("pameiģini lielāku skaitli.")
        else:
            print("pameiģini mazāku skaitli.") 
        guess = int(input("Uzmini skaitli: "))
        tries += 1
    else:
        if tries < 5:
            print("WoW!!!")
        elif tries <30:
            print ("Nav slikt")
        elif tries >30:
            print ("izmanto lab'aku stategiju")    
        print(f"tu uzmiēji pec {tries} reizem ! ")
    respones = input("Vai girbi turpin'at y/n: ")
    if respones == "y":
        repeat = True
    elif respones == "n":
        repeat = False 
        print ("Paldies par speli Bye, Bye")
    else : 
        repeat = False  
        print ("Paldies par speli Bye, Bye")   

 