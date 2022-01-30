import random
def rps_decision(user_choice, computer_choice):
    if (user_choice.lower()) == computer_choice:
        print("That's a tie")
    elif user_choice.lower() == 'rock' and computer_choice == 'scissors':
        print("You Win! :^)")
    elif user_choice.lower() == 'paper' and computer_choice == 'rock':
        print("You Win! :^)")
    elif user_choice.lower() == 'scissors' and computer_choice == 'paper':
        print("You Win! :^)")
    else:
        print("You lose :^(")
def rps_game(entry):
    computer_value = random.randrange(1,4,1)
    computer_value = computer_value - 1
    options = ['rock','paper','scissors','Rock','Paper','Scissors']
    computer_choice = options[computer_value]
    if entry in options:
        if entry == "rock" or entry == "Rock":
            print("The computer chooses: %s" % computer_choice)
            rps_decision(entry, computer_choice)
            
        elif entry == "paper" or entry == "Paper":
            print("The computer chooses: %s" % computer_choice)
            rps_decision(entry, computer_choice)
        
        elif entry == "scissors" or entry == "Scissors":
            print("The computer chooses: %s" % computer_choice)
            rps_decision(entry, computer_choice)

    else:
        print("invalid entry")
        return None





if __name__ == '__main__':
    print("Welcome to rock, paper, scissors!")
    print("Type rock, paper, or scissors")
    user_choice=str(input())
    rps_game(user_choice)

    