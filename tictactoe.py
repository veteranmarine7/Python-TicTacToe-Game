class TicTacToe:
    
    def __init__(self, player1_name, player2_name):
        # Initialize the players, game board and scores.
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.board = ['-'] * 9
        self.scores = {self.player1_name: 0, self.player2_name: 0, 'Draw': 0}

    def play(self, times):
        # Play the game.
        for j in range(times):
            print(f'Game {j+1} of {times}')
            self.display()
            if j % 2 == 0:
                # Alternate the players.
                for i in range(9):
                    if i % 2 == 0:
                        position = input(f'{self.player1_name}, mark your position (1-9): ')
                        position = self.check(position)
                        self.board[position] = 'X'
                        self.display()
                        status = self.score('X')
                        if status == 'Winner':
                            self.scores[self.player1_name] += 1
                            print(f'{self.player1_name} wins game {j+1}!')
                            break
                    elif i % 2 != 0:
                        position = input(f'{self.player2_name}, mark your position (1-9): ')
                        position = self.check(position)
                        self.board[position] = 'O'
                        self.display()
                        status = self.score('O')
                        if status == 'Winner':
                            self.scores[self.player2_name] += 1
                            print(f'{self.player2_name} wins game {j+1}!')
                            break
            else:
                for i in range(9):
                    # Alternate the players.
                    if i % 2 == 0:
                        position = input(f'{self.player2_name}, mark your position (1-9): ')
                        position = self.check(position)
                        self.board[position] = 'X'
                        self.display()
                        status = self.score('X')
                        if status == 'Winner':
                            self.scores[self.player2_name] += 1
                            print(f'{self.player2_name} wins game {j+1}!')
                            break
                    elif i % 2 != 0:
                        position = input(f'{self.player1_name}, mark your position (1-9): ')
                        position = self.check(position)
                        self.board[position] = 'O'
                        self.display()
                        status = self.score('O')
                        if status == 'Winner':
                            self.scores[self.player1_name] += 1
                            print(f'{self.player1_name} wins game {j+1}!')
                            break
            # If no one wins, the game ends in a draw.
            if i == 8 and status != 'Winner':
                self.scores['Draw'] += 1
                print('The game ends in a draw!\n')
            # Display scores after each game.
            print(f"Scores: {self.player1_name}: {self.scores[self.player1_name]} | {self.player2_name}: {self.scores[self.player2_name]} | Draw: {self.scores['Draw']}\n")
            self.board = ['-'] * 9    
        self.final_score()

    def check(self, position):
        # Check if the chosen position is valid and available.
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] or self.board[int(position)-1] != '-':
            print('Invalid position. Choose an empty position from 1-9.')
            position = input('Enter a new position (1-9): ')
        return int(position) - 1

    def score(self, mark):
        # Check if there's a winner based on the current board configuration.
        for i in range(0, 9, 3): # Check rows.
            if mark == self.board[i] == self.board[i+1] == self.board[i+2]:
                return 'Winner'

        for i in range(3): # Check columns.
            if mark == self.board[i] == self.board[i+3] == self.board[i+6]:
                return 'Winner'

        if mark == self.board[0] == self.board[4] == self.board[8]: # Check diagonals.
            return 'Winner'
        if mark == self.board[2] == self.board[4] == self.board[6]:
            return 'Winner'

    def display(self):
        # Display the current state of the board.
        print(f'{self.board[0]} {self.board[1]} {self.board[2]}\n{self.board[3]} {self.board[4]} {self.board[5]}\n{self.board[6]} {self.board[7]} {self.board[8]}')

    def final_score(self):
        # Display the final scores and overall winner.
        if self.scores[self.player1_name] == self.scores[self.player2_name]:
            print('The game ends in a tie!')
        elif self.scores[self.player1_name] > self.scores[self.player2_name]:
            print(f'{self.player1_name} is the overall winner!')
        else:
            print(f'{self.player2_name} is the overall winner!')

# Get player names and number of games from user input.
player_1 = input('Enter Player 1 name: ')
player_2 = input('Enter Player 2 name: ')
while player_1 == player_2:
    player_2 = input("You can't have the same name as Player 1. Enter a new name: ")

while True:
    try:
        num_games = int(input('How many games do you want to play?: '))
        if num_games <= 0:
            raise ValueError("Number of games must be a positive integer.")
        break  # Exit the loop if input is valid
    except ValueError as ve:
        print(f"Error: {ve}")
        print("Please enter a positive integer for the number of games.")

# Create an instance of TicTacToe class and start playing
game = TicTacToe(player_1, player_2).play(num_games)