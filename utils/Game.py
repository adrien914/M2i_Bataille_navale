from utils.Board import Board
from utils.Ship import Ship
from utils.Fire import Fire
import random


class Game:
    def __init__(self, length, number_of_boats):
        self.length = length
        self.number_of_boats = number_of_boats

    def start(self):
        board = Board()
        for i in range(0, self.number_of_boats):
            ship = Ship(random.randrange(2, 5), random.randrange(0, board.length))
            board.add_ship(ship)
        while True:
            board.print_board()
            try:
                firing_position = input("Where to shoot > ")
                game_finished = board.evaluate_impact(Fire(int(firing_position)))
                if game_finished:
                    break
            except ValueError:
                print("Send an integer please")
                continue
