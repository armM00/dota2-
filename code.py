player_game_history = []
# delete the lines 45-47 and 4-5. Modify the lines 8-159 and implement this code
while True:
    input_user1 = input("double below, below, above, or double above, "
                        "and any other character to see the result: ").lower()

    match input_user1:
        case "double below":
            player_game_history.append(float(-25))
        case "below":
            player_game_history.append(float(0))
        case "above":
            player_game_history.append(float(+25))
        case "double above":
            player_game_history.append(float(+50))
        case _:
            break

player_average = sum(player_game_history) / len(player_game_history)

games_quantity = len(player_game_history)
max_average = 25 * games_quantity / len(player_game_history)

normal_average = max_average * 100/3*2 / 100.0


def average(last_game):
    next_game_above_team = []
    next_game_below_team = []

    for player in last_game:
        if player_average >= normal_average:
            next_game_above_team.append(player)
            print("\nPlayer classified as above average")
            return next_game_above_team

        elif player_average < normal_average:
            next_game_below_team.append(player)
            print("\nPlayer classified as below average")
            return next_game_below_team


average(player_game_history)

print("Maximum could be:", max_average)
print("The average is:", normal_average)
print("is", player_average)


