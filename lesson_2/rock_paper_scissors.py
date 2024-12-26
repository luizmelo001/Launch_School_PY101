import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
CHOICE_ALIAS = {"rock": "r", "paper": "p", "scissors": "s", "lizard": "l", "spock": "sp"}

def prompt(message):
    print(f"{message}")

def display_winner(player_choice, computer_choice):
    prompt(f"You chose {player_choice}, computer chose {computer_choice}")

    match player_choice, computer_choice:
        case "rock", "scissors" | "lizard":
            result = "You win"
        case "paper", "rock" | "spock":
            result = "You win"
        case "scissors", "paper" | "lizard":
            result = "You win"
        case "lizard", "paper" | "spock":
            result = "You win"
        case "spock", "rock" | "scissors":
            result = "You win!"
        case _ if player_choice == computer_choice:
            result = "It's a tie!"
        case _:
            result = "Computer wins!"

    prompt(result)
    return result

again = 'y'
player_score = 0
computer_score = 0

while again == 'y':
    
    # Display choice with aliases and ask for input
    choices_str = ', '.join(f"{choice} ({CHOICE_ALIAS[choice]})" for choice in VALID_CHOICES)
    prompt(f"Choose one: {choices_str}")
    choice = input().lower()

    #convert alias to full choice name if an alias was entered
    player_choice = next((full_choice for full_choice, alias in CHOICE_ALIAS.items() if full_choice == choice or alias == choice ), None)

    while player_choice is None:
        prompt("That is not a valid choice")
        choice = input().lower()
        player_choice = next((full_choice for full_choice, alias in CHOICE_ALIAS.items() if full_choice == choice or alias == choice), None)

    computer_choice = random.choice(VALID_CHOICES)

    # call the display winner function to get the results and compute the score
    result = display_winner(player_choice, computer_choice)
    if "Computer wins" in result:
        computer_score += 1
    elif "You win" in result:
        player_score += 1

    print(f"Current score => Player: {player_score} / Computer: {computer_score}")

    if player_score == 5 or computer_score == 5:
        print("Thanks for playing")
        break

    prompt("Do you want to play again? ('y' or 'n')")
    again = input()

    while again not in ['y', 'n']:
        prompt("That is not a valid answer")
        again = input()

    if again == 'n':
        prompt("Thanks for playing!")


# implementations:
# create a score
# change "r", "p" and "s" to make it shorter
# add Lizzard and Spock as choices and change the rules