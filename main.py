import tictactoe


if __name__ == "__main__":
    ttt = tictactoe.TicTacToe()
    winner = None
    run = True
    while run:
        ttt.print()
        move = int(input())
        ttt.play(move)
        winner = ttt.evaluate()
        if winner:
            run = False
    ttt.print()
    print(f'Congratulations Player {winner} for winning the game!')
