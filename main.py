from utils import *

WIN = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Pygame Window")
clock = pygame.time.Clock()


def main():
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

        draw(WIN)

    pygame.quit()


def draw(win: pygame.display):
    win.fill(WHITE)
    pygame.display.update()


if __name__ == "__main__":
    main()
