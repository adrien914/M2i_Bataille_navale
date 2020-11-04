from utils.Fire import Fire
from utils.Ship import Ship


class Board:
    length = 100
    layout = []
    ships = []

    def __init__(self):
        for i in range(0, self.length):
            self.layout.append(' ')

    def add_ship(self, ship: Ship) -> None:
        """
        This method adds a ship to the board
        :param ship: The ship that has to be added
        """
        self.ships.append(ship)
        # For the length of the boat
        for i in range(0, ship.length):
            # Set the layout's index as an "o" to tell it's a ship
            self.layout[ship.position + i] = "o"

    def print_board(self) -> None:
        """
        This method prints the board to the player
        """
        for i in range(0, 5):
            start_line = i * self.length // 5
            end_line = (i + 1) * self.length // 5
            print(self.layout[start_line:end_line])

    def check_ship_destroyed(self, position):
        sunk = False
        for index, ship in enumerate(self.ships):
            if ship.position <= position < ship.position + ship.base_length:
                ship.length -= 1
                if ship.length == 0:
                    print("coulé")
                    sunk = True
                    self.ships.pop(index)
        return sunk

    def evaluate_impact(self, fire: Fire) -> bool:
        """
        This method takes a fire as an argument and evaluates the shot
        :param fire: The shot that needs to be evaluated
        :return: A boolean that tells if the game has ended or not
        """
        try:
            if self.layout[fire.position] == "o":
                self.layout[fire.position] = "x"
                is_sunk = self.check_ship_destroyed(fire.position)
                if "o" not in self.layout:
                    return True
                elif not is_sunk:
                    print("touché")
            else:
                print("raté")
        except IndexError:
            print("Please give a number between 0 and " + str(self.length))
        return False
