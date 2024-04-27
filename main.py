import pygame
import pygame_gui
HEIGHT, WIDTH = 900, 1600

pygame.init()
manager = pygame_gui.UIManager((WIDTH, HEIGHT))

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))



run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    screen.fill("grey")


    # Render
    pygame.draw.line(screen, (0,0,0), (WIDTH//4, 0), (WIDTH//4, HEIGHT), 1)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(WIDTH//4 + 20, 20, WIDTH - WIDTH//4 - 40, HEIGHT - 40), 1)

    for i in range(WIDTH//4 + 20,  WIDTH - 20, 20):
            pygame.draw.line(screen, (0,0,0), (i, 20), (i, HEIGHT - 20), 1)

    for i in range(0, HEIGHT - 20, 20):
        pygame.draw.line(screen, (0,0,0), (WIDTH//4 + 20, i + 20), (WIDTH-20, i + 20), 1)


    pygame.display.flip()
    


pygame.quit()