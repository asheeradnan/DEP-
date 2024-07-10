import sys
class NimGame:
    def __init__(self, num_red, num_blue, version='standard', first_player='computer', depth=None):
        self.num_red = num_red
        self.num_blue = num_blue
        self.version = version
        self.current_player = first_player
        self.depth = depth

    def is_game_over(self, red, blue):
        if self.version == 'standard':
            return red == 0 or blue == 0
        else:
            return red == 0 or blue == 0

    def score(self):
        return self.num_red * 2 + self.num_blue * 3

    def human_move(self):
        while True:
            try:
                num_red = int(input("Enter number of red marbles to remove: "))
                num_blue = int(input("Enter number of blue marbles to remove: "))
                if 0 <= num_red <= self.num_red and 0 <= num_blue <= self.num_blue and (num_red + num_blue) > 0:
                    self.num_red -= num_red
                    self.num_blue -= num_blue
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Try again.")

    def computer_move(self):
        move = self.minimax(self.num_red, self.num_blue, True)
        num_red, num_blue = move[1], move[2]
        self.num_red -= num_red
        self.num_blue -= num_blue
        print(f"Computer removes {num_red} red marbles and {num_blue} blue marbles.")

    def minimax(self, red, blue, maximizing):
        if self.is_game_over(red, blue):
            if self.version == 'standard':
                return (-(red * 2 + blue * 3), 0, 0)
            else:
                return ((red * 2 + blue * 3), 0, 0)

        if maximizing:
            best_value = float('-inf')
            best_move = (0, 0)
            for move in self.get_possible_moves(red, blue):
                new_red, new_blue = red - move[0], blue - move[1]
                value = self.minimax(new_red, new_blue, False)[0]
                if value > best_value:
                    best_value = value
                    best_move = move
            return (best_value, best_move[0], best_move[1])
        else:
            best_value = float('inf')
            best_move = (0, 0)
            for move in self.get_possible_moves(red, blue):
                new_red, new_blue = red - move[0], blue - move[1]
                value = self.minimax(new_red, new_blue, True)[0]
                if value < best_value:
                    best_value = value
                    best_move = move
            return (best_value, best_move[0], best_move[1])

    def get_possible_moves(self, red, blue):
        moves = []
        if self.version == 'standard':
            if red >= 2: moves.append((2, 0))
            if blue >= 2: moves.append((0, 2))
            if red >= 1: moves.append((1, 0))
            if blue >= 1: moves.append((0, 1))
        else:
            if blue >= 1: moves.append((0, 1))
            if red >= 1: moves.append((1, 0))
            if blue >= 2: moves.append((0, 2))
            if red >= 2: moves.append((2, 0))
        return moves

    def play_game(self):
        while not self.is_game_over(self.num_red, self.num_blue):
            print(f"Red Marbles: {self.num_red}, Blue Marbles: {self.num_blue}")
            if self.current_player == 'human':
                self.human_move()
                self.current_player = 'computer'
            else:
                self.computer_move()
                self.current_player = 'human'
        print("Game over!")
        print(f"Final score: {self.score()}")

if __name__ == '__main__':
    num_red = int(input("Enter the number of red marbles: "))
    num_blue = int(input("Enter the number of blue marbles: "))
    version = input("Enter the game version (standard/misere): ")
    first_player = input("Enter the first player (computer/human): ")

    game = NimGame(num_red, num_blue, version, first_player)
    game.play_game()
