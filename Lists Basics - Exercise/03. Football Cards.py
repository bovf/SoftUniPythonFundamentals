red_cards_user_input = input()
cards_list = red_cards_user_input.split(" ")

a_team = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
b_team = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]

a_team_removed_players = 0
b_team_removed_players = 0

for card in cards_list:
    if "B" in card:
        for player in b_team:
            if card == player:
                b_team.remove(player)
                b_team_removed_players += 1
    if "A" in card:
        for player in a_team:
            if card == player:
                a_team.remove(player)
                a_team_removed_players += 1
    if a_team_removed_players > 4 or b_team_removed_players > 4:
        break

print(f"Team A - {len(a_team)}; Team B - {len(b_team)}")
if len(a_team) < 7 or len(b_team) < 7:
    print("Game was terminated")
