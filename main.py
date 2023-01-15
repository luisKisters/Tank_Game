import pygame
import math
import os 

HULL1_BRONZE = pygame.image.load("Hull_01.png")
HULL1_BRONZE = pygame.transform.scale(HULL1_BRONZE, (50,50))

WEAPON1_BRONZE = pygame.image.load("Assets/Weapon_Color_A/Gun_01.png")
WEAPON1_BRONZE = pygame.transform.scale(WEAPON1_BRONZE, (20,40))

TRACK1_1 = pygame.image.load("Assets/Tracks/Track_1_A.png")
TRACK1_1 = pygame.transform.scale(TRACK1_1, (15,55))

TRACK1_2 = pygame.image.load("Assets/Tracks/Track_1_A.png")
TRACK1_2 = pygame.transform.scale(TRACK1_2, (15,55))

BULLET1 = pygame.image.load("./Assets/Effects/Exhaust_Fire.png")
BULLET1 = pygame.transform.scale(BULLET1, (40,40))

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
WHITE = (255,255,255)

bullets = []
BLT_SPEED = 10

TANK_SHOOT_ALLOW = True

class Tank():
    def __init__(self,x,y):
        self.x = x
        self.y = y 
        self.direction = ""
        self.rotation = 0
        self.hull_texture = HULL1_BRONZE
        self.hull = ""
        self.weapon_texture = WEAPON1_BRONZE
        self.weapon = ""
        self.track_texture = TRACK1_1
        self.track = ""
        self.direction = "up"
        # self.rect = pygame.Rect(, top, width, height) 
        # self.texture = HULL1_BRONZE
    
    def move(self):
        # def move(self, keys_pressed):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_w]:
            self.y -= 1
            self.direction = "up"
            self.rotation = 0    
        if keys_pressed[pygame.K_a]:
            self.direction = "left"
            # while self.rotation < 91:
            #     self.rotation += 1
            #     pygame.time.delay(100)
            self.rotation = 90 
            self.x -= 1   
        if keys_pressed[pygame.K_s]:
            self.y += 1
            self.rotation = 180
            self.direction = "down"
        if keys_pressed[pygame.K_d]:
            self.x += 1
            self.rotation = -90
            self.direction = "right"

    def show(self):     
        # print(self.rotation)
        # self.rotation = 
        
        # self.track = pygame.transform.rotate(self.track_texture, self.rotation)
        # self.track = pygame.transform.rotate(self.track_texture, self.rotation)
        self.hull = pygame.transform.rotate(self.hull_texture, self.rotation)
        # self.weapon = pygame.transform.rotate(self.weapon_texture, self.rotation)
        # WIN.blit(self.track, (self.x + 7,self.y + 5))
        # WIN.blit(self.track, (self.x + 38,self.y + 5))
        WIN.blit(self.hull, (self.x,self.y))
        # WIN.blit(self.weapon, (self.x + 20,self.y + 10))
        # math.atan2((mouse.y - self.y), (mouse.x - self.x))
        # degs = radians * (180 / math.pi)
        # WEAPON1_BRONZE = pygame.transform.rotate(WEAPON1_BRONZE, degs)
        # WIN.blit(WEAPON1_BRONZE, (self.x + 20,self.y + 10))
        # # pygame.transform.rotate(-degs)

    def shoot(self):             
        if self.direction == "up":
            bullet = Bullet(self.x + 5, self.y -10)
        if self.direction == "down":
            bullet = Bullet(self.x + 5, self.y +20)
        if self.direction == "right":
            bullet = Bullet(self.x + 20, self.y +5)
        if self.direction == "left":
            bullet = Bullet(self.x - 10, self.y +5)
        bullets.append(bullet)  
        

class Bullet():
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.speed = BLT_SPEED
        self.texture = BULLET1
        self.bullet = ""
        self.direction = tank.direction
        self.rotation = tank.rotation
    
    def update_pos(self):
        if self.direction == "up":
            self.y -= self.speed
        if self.direction == "down":
            self.y += self.speed
        if self.direction == "left":
            self.x -= self.speed
        if self.direction == "right":
            self.x += self.speed
            
    def show(self):
        self.update_pos()
        self.bullet = pygame.transform.rotate(self.texture, self.rotation)
        WIN.blit(self.bullet, (self.x,self.y))
        
        
    

tank = Tank(100, 100)

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        keys_pressed = pygame.key.get_pressed()
        tank.move()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  
        if keys_pressed[pygame.K_SPACE]:
            if TANK_SHOOT_ALLOW == True:
                tank.shoot()
                TANK_SHOOT_ALLOW = False
        if not keys_pressed[pygame.K_SPACE]:
            TANK_SHOOT_ALLOW = True
                
        if keys_pressed[pygame.K_ESCAPE]:
            run = False
        
        print(tank.direction)

        draw_window()
    pygame.quit()


def draw_window():
    WIN.fill(WHITE)
    tank.show()
    print(TANK_SHOOT_ALLOW)
    #  bullet.show()
    # print(bullets)
    for bullet in bullets:
        bullet.show()
    pygame.display.update()

if __name__ == "__main__":
    main()