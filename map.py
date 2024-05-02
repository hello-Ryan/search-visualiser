import pygame
import heapq


class Map:
    def __init__(self,screen, width, height):
        self.width = width
        self.height = height
        self.screen = screen
        self.walls = []
        self.colors = {
            "wall": (0,0,0),
            "start": (0, 255, 127),
            "goal": (220, 20, 60),

        }
        self.start = (2, 2)
        self.goal = (30, 30)
        self.search = "DFS"

        self.mapWidth = (3*width//4 - 40) // 20
        self.mapHeight = (height - 40) // 20

    
    def drawMap(self):
        # * Draw the horizontal and vertical lines that make up the grid
        for i in range(self.width//4 + 20,  self.width - 20, 20):
            pygame.draw.line(self.screen, (0,0,0), (i, 20), (i, self.height - 20), 1)

        for i in range(0, self.height - 20, 20):
            pygame.draw.line(self.screen, (0,0,0), 
                             (self.width//4 + 20, i + 20), 
                             (self.width-20, i + 20), 1)

        # * Draw the walls that have been placed
        for x, y in self.walls:
            pygame.draw.rect(self.screen, 
                             (0,0,0), 
                             pygame.Rect(((self.width//4 + 20*x), 20*y), (20, 20)))

        # * Draw the start and goal cells
        x, y = self.start
        pygame.draw.rect(self.screen, 
                        (0, 255, 127), 
                        pygame.Rect(((self.width//4 + 20*x), 20*y), (21, 21)))

        x, y = self.goal
        pygame.draw.rect(self.screen, 
                        (220,20,60), 
                        pygame.Rect(((self.width//4 + 20*x), 20*y), (21, 21)))

    def addWall(self, mouse):
        # * Adds a wall to the map making sure no walls overlap and not placed on the start and goal cells
        mouse_x, mouse_y = mouse
        x = (mouse_x - (self.width//4)) // 20
        y = (mouse_y) // 20

        if (x,y) == self.start or (x,y) == self.goal:
            return

        if (self.width//4 + 20 < mouse_x < self.width - 20) and (20 < mouse_y < self.height - 20):
            if (x,y) not in self.walls:
                self.walls.append((x,y))
            else: return

    def getNeighbours(self, node):
        # * Gets the neighbours the node
        x, y = node
        print(self.mapHeight, self.mapWidth)


    def clearWalls(self):
        # * reset the walls array
        self.walls = []

    def updateSearchAlgorithm(self, alg):
        self.search = alg

    def startSearch(self):
        if self.search == "DFS":
            self.dfs()

        elif self.search == "BFS":
            self.bfs()

        else:
            self.astar()


    def dfs(self):
        pass

    def bfs(self):
        pass
    
    def heuristic(self, x1, y1, x2, y2):
        return abs(x1-x2) + abs(y1-y2)

    def astar(self):
        open = []
        closed = set()

        x1, y1 = self.start
        x2, y2 = self.goal
        heapq.heappush(open, (self.start, self.heuristic(x1, y1, x2, y2)))


        while open:
            currentNode, cost = heapq.heappop(open)
            closed.add(currentNode)
            self.getNeighbours(currentNode)

            if currentNode == self.goal:
                return
            
m = Map(None, 400, 400)

m.astar()