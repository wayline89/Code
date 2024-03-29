import pygame

from utils import *
from tictactoe import TicTacToe

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
clock = pygame.time.Clock()

players = ["x", "o"]
ttt = TicTacToe(players)
tile_size = WIDTH / ttt.grid_size
images = [
    load_image_scaled('assets/art/cross.png', (tile_size, tile_size)),
    load_image_scaled('assets/art/naught.png', (tile_size, tile_size))
]
dict_player_image = dict(zip(players, images))

img_board = load_image_scaled('assets/art/board.png', (WIDTH * 0.925, HEIGHT * 0.925))
img_background = load_image_scaled('assets/art/background.png', (WIDTH, HEIGHT))

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
                    over, winner = ttt.play((x, y))
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
        # Draw the Background
        WIN.blit(img_background, (0, 0))
        # Draw the Game Grid
        WIN.blit(img_board, ((WIDTH - img_board.get_width()) / 2, (HEIGHT - img_board.get_width()) / 2))

        # Draw the Naughts and Crosses
        for y, row in enumerate(ttt.grid):
            for x, player in enumerate(row):
                if player in players:
                    rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
                    WIN.blit(dict_player_image[player], rect)

        # Draw Move Indicator
        text_surface = ttt_font.render(f'Current Player: {ttt.get_current_player()}', False, BLACK)
        WIN.blit(text_surface, (10, 0))

    win.fill(WHITE)

    draw_tic_tac_toe()

    pygame.display.update()


if __name__ == "__main__":
    main()
