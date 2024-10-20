list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

ConntPlayer = len(list_players)
AveragePlayerNumber = round(ConntPlayer / 2)

print(list_players[:AveragePlayerNumber])
print(list_players[AveragePlayerNumber:])
