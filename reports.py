#1 How many games are in the file?
#Expected name of the function: count_games(file_name)
#Expected output of the function: a number
def count_games(file_name):
    count = 0
    with open(file_name, "r") as file:
        for line in file:
            count += 1
    return count


#2 Is there a game from a given year?
#Expected name of the function: decide(file_name, year)
#Expected output of the function: boolean value
def decide(file_name, year):
    game_list = []
    with open(file_name, "r") as file:
        for lines in file:
            game_list.append(lines.strip("\n").split("\t"))
    #the third column in the txt file shows the release year
    for i in range(len(game_list)):
        if int(game_list[i][2]) == year:

            return True


#3 Which was the latest game?
#Expected name of the function: get_latest(file_name)
#Expected output of the function: the title of the latest game as a string
def get_latest(file_name):
    game_list = []
    latest_game = ""
    with open(file_name, "r") as my_file:
        for lines in my_file:
            game_list.append(lines.replace('\n', "").split(sep='\t'))

    latest_game_year = 0

    for game in game_list:
        if int(game[2]) > latest_game_year:
            latest_game_year = int(game[2])
            latest_game = game[0]

    return latest_game


#4 How many games do we have by genre?
#Expected name of the function: count_by_genre(file_name, genre)
#Expected output of the function: a number
#1 How many games are in the file?
#Expected name of the function: count_games(file_name)
#Expected output of the function: a number
def count_by_genre(file_name):
    count = 0
    with open(file_name, "r") as file:
        for line in file:
            count += 1
    return count


#2 Is there a game from a given year?
#Expected name of the function: decide(file_name, year)
#Expected output of the function: boolean value
def decide(file_name, year):
    game_list = []
    with open(file_name, "r") as file:
        for lines in file:
            game_list.append(lines.strip("\n").split("\t"))
    #the third column in the txt file shows the release year
    for i in range(len(game_list)):
        if int(game_list[i][2]) == year:

            return True


#3 Which was the latest game?
#Expected name of the function: get_latest(file_name)
#Expected output of the function: the title of the latest game as a string
def get_latest(file_name):
    game_list = []
    latest_game = ""
    with open(file_name, "r") as my_file:
        for lines in my_file:
            game_list.append(lines.replace('\n', "").split(sep='\t'))

    latest_game_year = 0

    for game in game_list:
        if int(game[2]) > latest_game_year:
            latest_game_year = int(game[2])
            latest_game = game[0]

    return latest_game


#4 How many games do we have by genre?
#Expected name of the function: count_by_genre(file_name, genre)
#Expected output of the function: a number
def count_by_genre(file_name, genre):
    counter = 0
    game_list = []
    with open(file_name, "r") as my_file:
        for lines in my_file:
            game_list.append(lines.replace('\n', "").split(sep='\t'))

    for game in game_list:
        if game[3] == genre:
            counter += 1

    return counter

#5 What is the line number of the given game (by title)?
#Expected name of the function: get_line_number_by_title(file_name, title)
#Expected output of the function: a number (if there is no game found, then raises ValueError exception)

#get_line_number_by_title(file_name, title)
def get_line_number_by_title(file_name, title):
    game_list = []
    with open(file_name, "r") as my_file:
        for lines in my_file:
            game_list.append(lines.replace('\n', "").split(sep='\t'))
        counter = 0
        for k in game_list:
            counter += 1
            if title == k[0]:
                return counter
    raise ValueError
