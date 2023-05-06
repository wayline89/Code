import pygame

from utils import *
from tictactoe import TicTacToe

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
clock = pygame.time.Clock()

players = ["x", "o"]
images = [pygame.image.load('assets/art/cross.png'), pygame.image.load('assets/art/naught.png')]
dict_player_image = dict(zip(players, images))

ttt = TicTacToe(players)
ttt.print()
tile_size = WIDTH / ttt.grid_size

def main():
    winner = None
    run = True
    while run:
        clock.tick(FPS)

        # Get all the events that happen this frame
        events = pygame.event.get()

        # Respond to the pygame events this frame
        for event in events:
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left Click
                    mouse_pos = pygame.mouse.get_pos()
                    x, y = int(mouse_pos[0] / tile_size), int(mouse_pos[1] / tile_size)
                    ttt.play((x, y))
                    ttt.print()
                    over, winner = ttt.evaluate()
                    if over:
                        run = False
                        break

        draw(WIN, ttt)

    ttt.print()
    if winner:
        print(f'Congratulations Player {winner} for winning the game!')
    else:
        print(f"It's a tie!")
    pygame.quit()


def draw(win: pygame.display, ttt: TicTacToe):
    def draw_tic_tac_toe():
        # Draw the Game Grid
        line_width = 5
        for i in range(1, ttt.grid_size):
            line_pos = tile_size * i - line_width / 2
            pygame.draw.line(WIN, BLACK, (line_pos, 0), (line_pos, HEIGHT), line_width)
            pygame.draw.line(WIN, BLACK, (0, line_pos), (WIDTH, line_pos), line_width)

        # Draw the Naughts and Crosses
        for y, row in enumerate(ttt.grid):
            for x, player in enumerate(row):
                if player in players:
                    rect = pygame.Rect(x * tile_size, y * tile_size, tile_size - line_width, tile_size - line_width)
                    WIN.blit(dict_player_image[player], rect)

    win.fill(WHITE)

    draw_tic_tac_toe()

    pygame.display.update()


if __name__ == "__main__":
    main()
