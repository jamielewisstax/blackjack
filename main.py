import random
from art import logo


def welcome():
    print(logo)
    print("Welcome to Blackjack!")
    print("The goal of Blackjack is simple: beat the dealer.\n")
    print("How do you beat the dealer?\nBy getting closer to 21 than the dealer, without going over 21.\n")
    print(
        "How do you lose? Either by:\nThe dealer gets closer to 21 than you.\nOR if you go over 21, you lose right "
        "away.\n")
    print("The game uses a full deck of cards. The score is calculated as follows:")
    print(
        "2 - 10 = Face value\nJack, Queen, King = 10\nAce = 1 or 11 (whichever is going to be the best for the hand)\n")
    print(
        "You can either 'hit' or 'stand'. Hit will grant you another card, and stand will lock in your cards.\nAfter "
        "you stand, it's the dealers turn. Dealer must hit until he has at least a 17.\n")
    input("Let's start a game! Whenever you're ready, press enter: ")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal(amount):
    global user_score
    global computer_score
    for x in range(amount):
        user_cards.insert(0, random.choice(cards))
        if user_score == 11 and user_cards[0] == 11:
            user_score += 1
        else:
            user_score += user_cards[0]
        computer_cards.insert(0, random.choice(cards))
        if computer_score == 11 and computer_cards[0] == 11:
            user_score += 1
        else:
            computer_score += computer_cards[0]


def hit():
    global user_score
    user_cards.insert(0, random.choice(cards))
    user_score += user_cards[0]
    if user_cards[0] == 11:
        print(f"You drew an Ace!\n")
        if user_score > 21:
            user_score -= 10
    else:
        print(f"You drew a {user_cards[0]}!\n")


def stand():
    global computer_score
    if len(computer_cards) == 2:
        print(f"The dealer reveals their second card: {computer_cards[1]}. Their current score is: {computer_score}.")
    while computer_score < 17:
        computer_cards.insert(0, random.choice(cards))
        computer_score += computer_cards[0]
        print(f"Dealer drew a {computer_cards[0]}. Their current score is: {computer_score}.\n")


def check_score():
    if user_score > 21:
        print(f"Your score is {user_score}. You busted.\nYou lose!\n")
        return False
    elif user_score > computer_score:
        print(
            f"Your score of {user_score} is higher than the dealers score of {computer_score}.\nCongratulations! You win!\n")
        return False
    elif computer_score > 21:
        print(f"The dealers score is {computer_score}. He busted, which means you win!\nCongratulations!\n")
        return False
    elif computer_score > user_score:
        print(f"Your score of {user_score} is lower than the dealers score of {computer_score}.\nYou lose!\n")
        return False
    elif computer_score == user_score:
        print(f"Your score of {user_score} is equal to that of the dealer.\nYou lose!\n")
        return False


print(welcome())
print(logo)
while True:
    user_score = 0
    computer_score = 0
    user_cards = []
    computer_cards = []
    deal(2)
    print(f"The dealer has a {computer_cards[0]} and a hidden card.")
    end = True
    if user_score == 21:
        print(f"Your cards: {user_cards}. Current score: {user_score}. Congratulations, you got a blackjack!\n")
        print(f"The dealer reveals their card second card: {computer_cards[1]}")
        if computer_score == 21:
            print("The dealer also has a blackjack... You lose!")
        else:
            print("Congratulations! You won!\n")
    else:
        while end:
            print(f"Your cards: {user_cards}. Current score: {user_score}.")
            hit_or_stand = (input("Would you like to 'hit' or 'stand'? ").lower())
            if hit_or_stand == 'hit':
                hit()
                if user_score > 21:
                    end = check_score()
            elif hit_or_stand == 'stand':
                stand()
                end = check_score()
            else:
                print("Please type only 'hit' or 'stand'.\n")
                continue
    play = input("Do you want to play another game? type 'y' or 'n': ")
    if play == 'y':
        print(logo)
        continue
    else:
        break
