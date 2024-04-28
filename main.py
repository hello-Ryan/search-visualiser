import pygame
from pygame_gui import UIManager, UI_DROP_DOWN_MENU_CHANGED
from pygame_gui.elements import UIDropDownMenu, UIButton

HEIGHT, WIDTH = 900, 1600

pygame.init()
pygame.display.set_caption('Search Algorithms Visualiser')

manager = UIManager((WIDTH, HEIGHT))

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.Surface((WIDTH, HEIGHT))
background.fill(pygame.Color('#808080'))

button_layout_rect = pygame.Rect(30, 20, 100, 20)

search_dropdown = UIDropDownMenu(options_list=['DFS','BFS','A*'],
                                       starting_option='DFS',
                                       relative_rect=pygame.Rect((WIDTH//16, 50), (WIDTH//8, 50)),
                                       manager=manager)


run = True
while run:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == UI_DROP_DOWN_MENU_CHANGED:
          print("Selected option:", event.text)

        manager.process_events(event)



    screen.fill("grey")


    # Render pygame gui buttons etc.
    manager.update(time_delta)
    screen.blit(background, (0, 0))
    manager.draw_ui(screen)


    # Render native pygame modules
    pygame.draw.line(screen, (0,0,0), (WIDTH//4, 0), (WIDTH//4, HEIGHT), 1)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(WIDTH//4 + 20, 20, WIDTH - WIDTH//4 - 40, HEIGHT - 40), 1)

    for i in range(WIDTH//4 + 20,  WIDTH - 20, 20):
            pygame.draw.line(screen, (0,0,0), (i, 20), (i, HEIGHT - 20), 1)

    for i in range(0, HEIGHT - 20, 20):
        pygame.draw.line(screen, (0,0,0), (WIDTH//4 + 20, i + 20), (WIDTH-20, i + 20), 1)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    if (WIDTH//4 + 20 < mouse_x < WIDTH - 20) and (20 < mouse_y < HEIGHT - 20):
        x = (mouse_x - (WIDTH//4)) // 20
        y = (mouse_y) // 20

        pygame.draw.rect(screen, (0,0,0), pygame.Rect(((WIDTH//4 + 20*x), 20*y), (20, 20)))
        print(x,y)
    else:
        print("out")

    

    pygame.display.update()

    
pygame.quit()