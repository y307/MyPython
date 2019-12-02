#!/url/bin/env python3
# -*- coding: utf-8 -*-

import json5

filename = "payers.txt"
myfile = open(filename, mode='w') # encoding='Latin-1'

player1 = {
    'PlayerName': "Donald Trump",
    'Score': 345,
    'Awards': ["OR", "NV", "NY"]
}

player2 = {
    'PlayerName': "Hillary Clinton",
    'Score': 346,
    'Awards': ["WI", "TX", "MI"]
}

myPlayers = []
myPlayers.append(player1)
myPlayers.append(player2)

# ------ SAVE BY JSON ------

json5.dump(myPlayers, myfile)
myfile.close()

# ------ LOAD BY JSON ------

myfile = open(filename, mode='r')
json_data = json5.load(myfile)

for user in json_data:
    print("Player Name is: " + str(user['PlayerName']))
    print("Player Score is: " + str(user['Score']))
    print("Player Awards is: " + str(user['Awards'][0]))
    print("Player Awards is: " + str(user['Awards'][1]))
    print("Player Awards is: " + str(user['Awards'][2]))
    print("--------------------------------------------\n\n")

