import pygame
import random
import time

player_x = 100
player_y = 100
player_size = 25
player_speed = 10
player_hitbox = pygame.Rect(player_x, player_y, player_size, player_size)

class Enemy():
    def __init__(self, x, y, speed, size):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size-30
        self.hitbox = pygame.Rect(self.x, self.y, self.size, self.size)

    def update(self, screen):
        self.y += self.speed
        self.hitbox.y += self.speed
        pygame.draw.rect(screen, (0, 255, 0), self.hitbox)
        self.pic = pygame.image.load("bulletPlayer.png")
        screen.blit(self.pic,(self.x-35, self.y-140))




player_alive = True
player_health =500

pygame.init()
game_width = 1000
game_height = 1000
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True





enemies = []



enemy_timer_max = 5
enemy_timer = enemy_timer_max

background_pic = pygame.image.load("background.png")
player_pic = pygame.image.load("good-tank-1.png")





while running:
    screen.blit(background_pic, (0, 0))
    pygame.draw.rect(screen, (255, 255, 0), player_hitbox)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    screen.blit(player_pic, (player_x, player_y))
    enemy_timer -= 1
    if enemy_timer <= 0:
        new_enemy_y = -500
        new_enemy_x = random.randint(-450,1000)
        new_enemy_speed =  random.randint(10,15)
        enemies.append(Enemy(new_enemy_x, new_enemy_y, new_enemy_speed, 80))
        enemy_timer = enemy_timer_max
    if player_alive:
        for enemy in enemies:
            enemy.update(screen)
            if player_hitbox.colliderect(enemy.hitbox):
                enemies.remove(enemy)
                player_health -= 50
                if player_health <= 0:
                    player_alive = False
                    

        if player_alive:
            timing = time.perf_counter()






    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_x += 10
    if keys[pygame.K_LEFT]:
        player_x -= 10
    if keys[pygame.K_UP]:
        player_y -= 10
    if keys[pygame.K_DOWN]:
        player_y += 10
    player_hitbox.x = player_x+500
    player_hitbox.y = player_y+450
    player_hitbox.width = player_size + 100
    player_hitbox.height = player_size + 100


    health_font = pygame.font.SysFont("default", 30)
    health_text = health_font.render("Health: " + str(player_health), True, (255, 255, 255))
    screen.blit(health_text, (30, 30))

    score_font = pygame.font.SysFont("default", 30)
    score_text = score_font.render("Score: " + str(timing), True, (255, 255, 255))
    screen.blit(score_text, (30, 50))




    pygame.display.flip()
    clock.tick(50)
    pygame.display.set_caption("MY GAME fps: "+str(clock.get_fps()))
