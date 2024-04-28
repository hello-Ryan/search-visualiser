import pygame


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
    
    def drawMap(self, screen, mouse):
        for i in range(self.width//4 + 20,  self.width - 20, 20):
            pygame.draw.line(screen, (0,0,0), (i, 20), (i, self.height - 20), 1)

        for i in range(0, self.height - 20, 20):
            pygame.draw.line(screen, (0,0,0), (self.width//4 + 20, i + 20), (self.width-20, i + 20), 1)

        for x, y in self.walls:
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(((self.width//4 + 20*x), 20*y), (20, 20)))

        

    def addWall(self, screen, mouse):
        mouse_x, mouse_y = mouse
        if (self.width//4 + 20 < mouse_x < self.width - 20) and (20 < mouse_y < self.height - 20):
            x = (mouse_x - (self.width//4)) // 20
            y = (mouse_y) // 20

            self.walls.append((x,y))
