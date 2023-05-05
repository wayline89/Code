import tictactoe


if __name__ == "__main__":
    ttt = tictactoe.TicTacToe()
    winner = None
    run = True
    while run:
        ttt.print()
        move = int(input())
        ttt.play(move)
        over, winner = ttt.evaluate()
        if over:
            run = False
    ttt.print()
    if winner:
        print(f'Congratulations Player {winner} for winning the game!')
    else:
        print(f"It's a tie!")
