players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

# TODO здесь писать код
new_players = []
for key, value in players.items():
    result = key + value
    new_players.append(result)

print(new_players)