from reports import *

def export_results(result):
    file =open("result.txt", "a+")
    file.write(str(result) + "\n")

export_results(str(get_most_played("game_stat.txt")))
export_results(str(sum_sold("game_stat.txt")))
export_results(str(get_selling_avg("game_stat.txt")))
export_results(str(count_longest_title("game_stat.txt")))
export_results(str(get_date_avg("game_stat.txt")))
export_results(str(get_game("game_stat.txt", "Diablo II")))
