from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface((48, 56))
        self.image.fill('gray')
        self.rect = self.image.get_frect(topleft=pos)

        #movement
        self.direction = vector()
        self.speed = 1.5

    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = vector(0, 0)

        if keys[pygame.K_w]:
            input_vector.y = -1
        if keys[pygame.K_s]:  
            input_vector.y = 1
        if keys[pygame.K_a]:
            input_vector.x = -1
        if keys[pygame.K_d]:
            input_vector.x = 1
        
        self.direction = input_vector
       
    def move(self):
        self.rect.topleft += self.direction * self.speed
    def update(self):
        self.input()
        self.move()