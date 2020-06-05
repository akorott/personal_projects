# Welcome to the Blackjack game:

import time
import random

acceptable_input = {
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 11
}
dealer_total = 0
user_total = 0

dealer_card_1 = random.choice(list(acceptable_input.keys()))
dealer_card_2 = random.choice(list(acceptable_input.keys()))

dealer_total = acceptable_input[dealer_card_1] + acceptable_input[dealer_card_2]

user_card_1 = random.choice(list(acceptable_input.keys()))
user_card_2 = random.choice(list(acceptable_input.keys()))

user_total = acceptable_input[user_card_1] + acceptable_input[user_card_2]

print('')
time.sleep(1)
print("The dealer shuffles the deck and deals the cards.")
print('')
time.sleep(2)
print("The dealer's hand is: {} - {}".format(dealer_card_1, dealer_card_2))
time.sleep(3)
print("Your flipped cards are: {} - {}".format(user_card_1, user_card_2))
time.sleep(2)
print('')
user_response_1 = input("Do you want to hit again? (y/n): ")
print(user_response_1)

if user_response_1 == 'y':
    user_card_3 = random.choice(list(acceptable_input.keys()))
    user_total += acceptable_input[user_card_3]
    time.sleep(3)
    print("You now have the following: {} - {} - {}". format(user_card_1, user_card_2, user_card_3))
    if user_total > 21:
        time.sleep(2)
        print('You went over 21, you lose!')
        quit()
elif user_response_1 == 'n':
    pass

time.sleep(2)
if dealer_total < 17:
    dealer_card_3 = random.choice(list(acceptable_input.keys()))
    time.sleep(2)
    print("The dealer dealt a 3rd card and now has: {} - {} - {}". format(dealer_card_1, dealer_card_2, dealer_card_3))
    dealer_total += acceptable_input[dealer_card_3]
    if dealer_total < 17:
        dealer_card_4 = random.choice(list(acceptable_input.keys()))
        dealer_total += acceptable_input[dealer_card_4]
        time.sleep(2)
        print(
            "The dealer dealt a 3rd card and now has: {} - {} - {} - {}".format(dealer_card_1, dealer_card_2, dealer_card_3, dealer_card_4))

        if dealer_total < 17:
            dealer_card_5 = random.choice(list(acceptable_input.keys()))
            dealer_total += acceptable_input[dealer_card_5]
            time.sleep(2)
            print(
                "The dealer dealt a 3rd card and now has: {} - {} - {} - {} - {}".format(dealer_card_1, dealer_card_2,
                                                                                    dealer_card_3, dealer_card_4, dealer_card_5))

time.sleep(2)

if dealer_total > 21:
    print("Congratulations, you won!!!")
elif user_total > dealer_total:
    print('Congratulations, you won!!!')
elif dealer_total > user_total:
    print('The dealer\'s total is {} and you have {}, YOU LOSE!'.format(dealer_total, user_total))





