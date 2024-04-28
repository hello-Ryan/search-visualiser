import pygame
from pygame_gui import UIManager, UI_DROP_DOWN_MENU_CHANGED
from pygame_gui.elements import UIDropDownMenu, UIButton
from map import Map

HEIGHT, WIDTH = 900, 1600

pygame.init()
pygame.display.set_caption('Search Algorithms Visualiser')

manager = UIManager((WIDTH, HEIGHT))

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.Surface((WIDTH, HEIGHT))
background.fill(pygame.Color('#808080'))
map = Map(WIDTH, HEIGHT)

search_dropdown = UIDropDownMenu(options_list=['DFS','BFS','A*'],
                                       starting_option='DFS',
                                       relative_rect=pygame.Rect((WIDTH//16, 50), (WIDTH//8, 50)),
                                       manager=manager)

clear_walls = UIButton(manager = manager, relative_rect=pygame.Rect((WIDTH//16, 200), (WIDTH//8, 50)), text="clear", command=map.clearWalls)


run = True
while run:
    time_delta = clock.tick(60)/1000.0
    mouse = pygame.mouse.get_pos()
    mouse_x, mouse_y = mouse
    screen.fill("grey")

    # Render pygame gui buttons etc.
    manager.update(time_delta)
    screen.blit(background, (0, 0))
    manager.draw_ui(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == UI_DROP_DOWN_MENU_CHANGED:
          print("Selected option:", event.text)
        
        if (WIDTH//4 + 20 < mouse_x < WIDTH -20) and (event.type == pygame.MOUSEBUTTONDOWN or pygame.mouse.get_pressed()[0]):
            map.addWall(mouse)
        


        manager.process_events(event)


    # Render native pygame modules
    pygame.draw.line(screen, (0,0,0), (WIDTH//4, 0), (WIDTH//4, HEIGHT), 1)

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(WIDTH//4 + 20, 20, WIDTH - WIDTH//4 - 40, HEIGHT - 40), 1)

    map.drawMap(screen, mouse)



    pygame.display.update()

    
pygame.quit()