partAsolution = 0
partBsolution = 0

def decodeGame(game):
    id, gamelist = game.split(':')
    gamelist = gamelist.strip()
    gamelist = gamelist.split(';')

    colours = ['red', 'green', 'blue']
    for i in range(0, len(gamelist)):
        gamelist[i] = gamelist[i].strip().split(',')
        gamedict = {}
        for j in gamelist[i]:
            for k in colours:
                if j.strip().find(k) != -1:
                    gamedict[k] = int(j.strip().split(' ')[0].strip())
        gamelist[i] = gamedict

    id = id.split(' ')[-1].strip()

    return int(id), gamelist

def validGameList(gamelist):
    default = {'red': 12, 'green': 13, 'blue': 14}
    for game in gamelist:
        for color in game.keys():
            if game[color] > default[color]:
                return False

    return True

def cubePower(gamelist):
    default = {'red': 0, 'green': 0, 'blue': 0}
    for game in gamelist:
        for color in game.keys():
            default[color] = max(game[color], default[color])
    return default['red'] * default['blue'] * default['green']

with open('input.txt', 'r') as file:
    games = file.readlines()

    for game in games:
        gameId, gamelist = decodeGame(game)

        # Part A
        if validGameList(gamelist):
            partAsolution += gameId

        # Part B
        partBsolution += cubePower(gamelist)

    print(partAsolution)
    print(partBsolution)
