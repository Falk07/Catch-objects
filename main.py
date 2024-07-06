import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catch the Falling Objects")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

basket_width = 100
basket_height = 20
basket_pos = [screen_width // 2, screen_height - basket_height - 10]
basket_speed = 10

object_width = 30
object_height = 30
object_pos = [random.randint(0, screen_width - object_width), 0]
object_speed = 10

clock = pygame.time.Clock()

game_over = False

font = pygame.font.SysFont("monospace", 35)

score = 0
missed_objects = 0
max_missed = 3

def detect_collision(basket_pos, object_pos):
    b_x = basket_pos[0]
    b_y = basket_pos[1]

    o_x = object_pos[0]
    o_y = object_pos[1]

    if (o_x >= b_x and o_x < (b_x + basket_width)) or (b_x >= o_x and b_x < (o_x + object_width)):
        if (o_y >= b_y and o_y < (b_y + basket_height)) or (b_y >= o_y and b_y < (o_y + object_height)):
            return True
    return False

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_pos[0] > 0:
        basket_pos[0] -= basket_speed
    if keys[pygame.K_RIGHT] and basket_pos[0] < screen_width - basket_width:
        basket_pos[0] += basket_speed

    object_pos[1] += object_speed

    if object_pos[1] > screen_height:
        object_pos = [random.randint(0, screen_width - object_width), 0]
        missed_objects += 1
        if missed_objects >= max_missed:
            game_over = True

    if detect_collision(basket_pos, object_pos):
        score += 1
        object_pos = [random.randint(0, screen_width - object_width), 0]

    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (basket_pos[0], basket_pos[1], basket_width, basket_height))
    pygame.draw.rect(screen, WHITE, (object_pos[0], object_pos[1], object_width, object_height))

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    missed_text = font.render(f"Missed: {missed_objects}", True, WHITE)
    screen.blit(missed_text, (10, 50))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
