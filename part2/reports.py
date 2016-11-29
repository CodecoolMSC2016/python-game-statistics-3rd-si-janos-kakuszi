#def most played game (name)
def get_most_played(file_name):
    game_list = []
    most = 0
    name = ''
    with open(file_name, "r") as f:
        for line in f.readlines():
            game_list.append(line.split("\t"))
    for game in game_list:
        if float(game[1]) > float(most):
            most = float(game[1])
            name = game[0]
    return name

#def avarage date (number)
def get_date_avg(file_name):
    game_list = []
    date = []
    num = 0
    with open(file_name, "r") as f:
        for line in f.readlines():
            game_list.append(line.split("\t"))
    num = len(game_list)
    for game in game_list:
        date.append(float(game[2]))
    return round(sum(date) / num)

# def game properties (list)
def get_game(file_name, title):
    game = []
    with open(file_name) as f:
        for line in f:
            if line.split('\t')[0] == title:
                game.append(line.split('\t')[0])
                game.append(float(line.split('\t')[1]))
                game.append(int(line.split('\t')[2]))
                game.append(line.split('\t')[3])
                game.append((line.split('\t')[4]).rstrip('\n'))
        return game

#def avarage selling (number)
def get_selling_avg(file_name):
    game_list = []
    counter = 0
    total = 0
    with open(file_name, "r") as f:
        for line in f.readlines():
            game_list.append(line.split("\t"))
    for game in game_list:
        counter += 1
        total += float(game[1])
    average_selling = total / counter
    return average_selling

#def total numbers of sold (number)
def sum_sold(file_name):
    game_list = []
    sum = 0
    with open(file_name, "r") as f:
        for line in f.readlines():
            game_list.append(line.split("\t"))
    for game in game_list:
        sum += float(game[1])
    return sum

#def longest title in the game list (number)
def count_longest_title(file_name):
    game_list = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            game_list.append(line.split("\t"))
        return max([len(game[0]) for game in game_list])
