import random
import time


while True : 
    score = 0 
    while True : 
        print("Rolling the dice ....")
        time.sleep(1.5)
        random_number = random.randint(1,6)
        score += random_number
        print("You rolled the dice and you got a",random_number)
        time.sleep(1)
        if random_number == 1: 
            print("Sorry, you lost the game")
            time.sleep(0.5)
            break
        else: 
            print("Now your score is",score)
            time.sleep(0.5)
        roll_again = input("Do you want to keep rolling the dice? Yes(Y) or No(N): ")
        roll_again = str(roll_again)
        if roll_again.lower() not in ["y","yes"]:
            print("Congrats, you have earned",score,"points")
            break

    play_again = input("Do you want to play again? Yes(Y) or No(N): ")
    if play_again.lower() not in ["y", "yes"]:
        print("Thanks for playing!")
        break
        


    
        
