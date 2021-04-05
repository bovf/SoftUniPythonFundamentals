cards = input()
number_of_shuffles = int(input())

cards_list = cards.split(" ")


for _ in range(number_of_shuffles):
    cards_list_first_half = []
    cards_list_second_half = []

    shuffled_cards = []

    card_counter = 0
    for card in cards_list:
        card_counter += 1
        if card_counter <= len(cards_list) / 2:
            cards_list_first_half.append(card)
        else:
            cards_list_second_half.append(card)
    for card_pair in range(int((len(cards_list) / 2))):
        shuffled_cards.append(cards_list_first_half[card_pair])
        shuffled_cards.append(cards_list_second_half[card_pair])
    cards_list = shuffled_cards

print(cards_list)
