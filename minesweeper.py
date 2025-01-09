#!/usr/bin/python3

class MineSweeper:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
    
    def display(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                print("#", end = "")
            print()

def game_iteration(game_number: int):
    for iteration in range(0, game_number):
        print(f"Game {iteration + 1}")
        minesweeper_games = MineSweeper(iteration + 1, 10 - iteration)
        minesweeper_games.display()


game_iteration(12)