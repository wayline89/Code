import tictactoe


if __name__ == "__main__":
    ttt = tictactoe.TicTacToe()
    run = True
    while run:
        ttt.print()
        move = int(input())
        ttt.play(move)
        ttt.evaluate()
