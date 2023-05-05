from utils import *
from tictactoe import TicTacToe

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
clock = pygame.time.Clock()

ttt = TicTacToe()
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

            mouse_pos = pygame.mouse.get_pos()
            x = int(mouse_pos[0] / tile_size)
            y = int(mouse_pos[1] / tile_size)
            print(x, y)

        draw(WIN)

    pygame.quit()


def draw(win: pygame.display):
    win.fill(WHITE)

    line_width = 5
    for i in range(1, 3):
        line_pos = tile_size*i - line_width/2
        pygame.draw.line(WIN, BLACK, (line_pos, 0), (line_pos, HEIGHT), line_width)
        pygame.draw.line(WIN, BLACK, (0, line_pos), (WIDTH, line_pos), line_width)

    pygame.display.update()


if __name__ == "__main__":
    main()
