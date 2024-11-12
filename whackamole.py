import pygame
import random

def draw_grid(screen):
    #draw horizontal lines
    for i in range(0, 640, 32): #(640/32 = 20 columns)
        pygame.draw.line(
            screen,
            'black',
            (i, 0),
            (i, 512),
        )

    #draw vertical lines
    for i in range(0, 512, 32): #(512/32 = 16 rows)
        pygame.draw.line(
            screen,
            'black',
            (0, i),
            (640, i),
        )

def main():
    try:
        pygame.init()

        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        mole_x = 0
        mole_y = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # 3. When the user clicks on the mole's square, it should move to a different random square.
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if (mouse_x // 32 == mole_x // 32) and (mouse_y // 32 == mole_y // 32):
                        mole_x, mole_y = random.randint(0, 19) * 32, random.randint(0, 15) * 32


            screen.fill("light green")
            # 1. The window should be divided into a 20x16 grid of 32x32 squares
            draw_grid(screen)
            # 2. The mole image should be drawn in the top left square.
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
