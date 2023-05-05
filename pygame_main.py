from utils import *
from tictactoe import TicTacToe

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
clock = pygame.time.Clock()

def main():
    ttt = TicTacToe()
    tile_size = WIDTH / ttt.grid_size
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

            mouse_pos = pygame.mouse.get_pos()
            x = int(mouse_pos[0] / tile_size)
            y = int(mouse_pos[1] / tile_size)
            print(x, y)

        draw(WIN)

    pygame.quit()


def draw(win: pygame.display):
    win.fill(WHITE)
    pygame.display.update()


if __name__ == "__main__":
    main()
