# module that makes use of random integer generator
from random import randint

# the list of choices that the computer can choose from
play = ["Rock", "Paper", "Scissors"]

# this is where the computer makes its play
computer = play[randint(0, 2)]
computer_wins = 0
player_wins = 0

win = 'win'
lose = 'lose'
tie = 'tie'

choose = "Computer chose " + computer + '.'  # statement saying what the computer "chose"

# statements for the different outcomes
win_statement = "You have achieved peak brain cells.\n"
lose_statement = "Imagine losing to the computer.\n"
tie_statement = "You have neither gained nor lost brain cells.\n"

# allows for a loop later in the code, to keep the game going until the player wants to stop
player = True


# determines what to do in the case of each outcome
def outcome(out):
    # had to make these global so that they could be permanently changed when used in functions
    # if I didn't make them global, weird things would happen and errors would pop up
    global computer_wins
    global player_wins
    global score

    if out == tie:
        print(choose)
        print(tie_statement)
        score = "Computer: " + str(computer_wins) + " Humanity: " + str(player_wins) + "\n"
        print(score)
    elif out == win:
        player_wins += 1
        print(choose)
        print(win_statement)
        score = "Computer: " + str(computer_wins) + " Humanity: " + str(player_wins) + "\n"
        print(score)
    else:
        computer_wins += 1
        print(choose)
        print(lose_statement)
        score = "Computer: " + str(computer_wins) + " Humanity: " + str(player_wins) + "\n"
        print(score)


# determines the outcome of the game, whether you've won, lost, or tied
def rules(play1, play2):
    if play1 == 'Rock':
        if play2 == 'Rock':
            outcome(tie)
        elif play2 == 'Paper':
            outcome(lose)
        else:
            outcome(win)
    elif play1 == 'Paper':
        if play2 == 'Rock':
            outcome(win)
        elif play2 == 'Paper':
            outcome(tie)
        else:
            outcome(lose)
    else:
        if play2 == 'Rock':
            outcome(lose)
        elif play2 == 'Paper':
            outcome(win)
        else:
            outcome(tie)


# the loop for the game to occur
while player:  # since player is True, then the loop will always run until the player breaks
    player = input("Choose Rock, Paper, or Scissors. Or type 'break' to end the game: ")  # asks the player for their choice
    while player != "Rock" and player != "Scissors" and player != "Paper" and player != 'break':  # if player doesn't type it in correctly
        print("Do you are have stupid? Try and spell it right this time.\n")
        player = input("Choose Rock, Paper, or Scissors. Or type 'break' to end the game: ")
    if player != 'break':  # proceeds with game
        rules(player, computer)
    else:
        if player_wins > computer_wins:
            print("Congratulations! Humanity prevails!")
        elif player_wins < computer_wins:
            print("Wow, you lost. Hopefully this doesn't foreshadow anything.")
        else:
            print("Wow! You're neck and neck with the computer!")
        break  # breaks out of loop
    computer = play[randint(0, 2)]  # makes the computer choose again
    choose = "Computer chose " + computer + '.'
