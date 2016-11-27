import reports

# Printing functions from reports.py
file_name = "game_stat.txt"
print(reports.decide(file_name, 1995))
print(reports.count_games(file_name))
print(reports.get_latest(file_name))
print(reports.count_by_genre(file_name, "First-person shooter"))
print(reports.get_line_number_by_title(file_name, "Counter-Strike: Condition Zero"))
