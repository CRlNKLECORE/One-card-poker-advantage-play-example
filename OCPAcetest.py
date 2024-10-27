import random

def create_shoe():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    single_deck = ranks * 4
    return single_deck * 6

def card_value(card):
    value_map = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return value_map[card]

def play_game(starting_money, bet_size, tie_bet_size, num_shoes):
    shoe = create_shoe()
    random.shuffle(shoe)
    player_money = starting_money
    cards_dealt = 0
    special_tie_wins = 0
    ace_20_percent_count = 0
    shoe_count = 0

    while shoe_count < num_shoes:
        if len(shoe) <= 0.2 * len(create_shoe()):
            shoe = create_shoe()
            random.shuffle(shoe)
            shoe_count += 1

        if len(shoe) < 2:
            continue

        ace_concentration = shoe.count('A') / len(shoe)
        if ace_concentration > 0.20:
            ace_20_percent_count += 1

        player_card = shoe.pop()
        dealer_card = shoe.pop()
        cards_dealt += 2

        player_value = card_value(player_card)
        dealer_value = card_value(dealer_card)

        if player_value > dealer_value:
            player_money += bet_size
        elif player_value < dealer_value:
            player_money -= bet_size
        else:
            player_money -= bet_size / 2
        
        if ace_concentration > 0.21:
            if player_card == 'A' and dealer_card == 'A':
                player_money += tie_bet_size * 25
                special_tie_wins += 1
            else:
                player_money -= tie_bet_size

    return player_money, special_tie_wins, shoe_count, ace_20_percent_count

starting_money = float(input("Enter the starting money for the player: "))
bet_size = float(input("Enter the bet size per round: "))
tie_bet_size = float(input("Enter the tie bet size: "))
num_shoes = int(input("Enter the number of shoes to play through: "))

final_amount, special_tie_wins, shoes_played, times_ace_concentration_exceeded_20 = play_game(starting_money, bet_size, tie_bet_size, num_shoes)
print(f"The player finished with: ${final_amount:.2f}")
print(f"Special tie bets won: {special_tie_wins}")
print(f"Total shoes played: {shoes_played}")
print(f"Times Ace concentration exceeded 20%: {times_ace_concentration_exceeded_20}")