import time
end_time = time.strftime("%Y%m%d-%H%M%S")
filename = f"{end_time}.txt"

def game_saver_human(moves,black_holes,message):
    with open(filename, "a+") as f:
        if message == " " : message = "You lost the game "
        f.write("Human_Player \n")
        f.write(f"Total moves = {moves}\n")
        f.write(f"total blackhole hits = {black_holes}\n")
        f.write(message)
        f.write("\n\n")

def game_saver_com(moves,black_holes,message):
    with open(filename, "a+") as f:
        if message == " " : message = "Computer lost the game "
        f.write("Computer \n")
        f.write(f"Total moves = {moves}\n")
        f.write(f"total blackhole hits = {black_holes}\n")
        f.write(message)
        f.write("\n")