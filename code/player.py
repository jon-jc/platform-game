from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.Surface((48, 56))
        self.image.fill('gray')

        #rects
        self.rect = self.image.get_frect(topleft=pos)
        self.old_rect = self.rect.copy()

        #movement
        self.direction = vector()
        self.speed = 250
        #collision
        self.collision_sprites = collision_sprites
        
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
        
        self.direction = input_vector.normalize() if input_vector else input_vector
       
    def move(self, dt):
        self.rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.rect.y == self.direction.y * self.speed * dt
        self.collision('vertical')

    def collision(self, axis):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if axis =="horizontal":
                    #left
                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right

                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left
                else:
                    pass

    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.input()
        self.move(dt)