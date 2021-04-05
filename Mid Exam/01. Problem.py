experience_needed = float(input())
count_of_battles = int(input())

experience_collected = 0
current_battle = 0

for battle in range(1, count_of_battles + 1):
    experience_gained = float(input())
    current_battle = battle
    bonus_exp = 0

    if battle % 15 == 0:
        bonus_exp += experience_gained * 0.05
    elif battle % 3 == 0:
        bonus_exp += experience_gained * 0.15
    elif battle % 5 == 0:
        bonus_exp -= experience_gained * 0.1

    experience_collected += experience_gained + bonus_exp

    if experience_collected >= experience_needed:
        break

if experience_needed <= experience_collected:
    print(f"Player successfully collected his needed experience for {current_battle} battles.")
else:
    print(f"Player was not able to collect the needed experience, {abs(experience_needed - experience_collected):.2f}"
          f" more needed.")
