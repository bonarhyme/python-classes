import random

options = ["R", "P", "S"]

def game():
    user_input = input("Enter a value between R, P, S \n").upper()

    if(user_input in options):
        cpu_selection = random.choice(options)
        print("------------------------------")
        print("Player {} : CPU {}".format(user_input, cpu_selection))

        if(cpu_selection == user_input):
            print("Draw! The cpu and player picked the same move  \n")
            game()
        if((cpu_selection == "R" ) and (user_input == "S")):
            print("------------------------------")
            print("Winner: CPU")
            print("------------------------------")

        if((cpu_selection ==  "S") and (user_input ==  "P")):
            print("------------------------------")
            print("Winner: CPU")
            print("------------------------------")

        if((cpu_selection ==  "P") and (user_input ==  "R")):
            print("------------------------------")
            print("Winner: CPU")
            print("------------------------------")

        if((user_input == "R" ) and (cpu_selection == "S")):
            print("------------------------------")
            print("Winner: Player")
            print("------------------------------")

        if((user_input ==  "S") and (cpu_selection ==  "P")):
            print("------------------------------")
            print("Winner: Player")
            print("------------------------------")

        if((user_input ==  "P") and (cpu_selection ==  "R")):
            print("------------------------------")
            print("Winner: Player")
            print("------------------------------")

    else:
        print("Invalid selection. Try again.  \n")
        game()

game()