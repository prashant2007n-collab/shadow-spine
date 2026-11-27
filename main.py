import pygame
import math

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Mr.Spinny")
screen.fill((0, 0, 0))

circle_x = 640
circle_y = 360

is_running = True
radius = 50
stop_distance = radius * 2
speed = 5


while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            
    screen.fill((0, 0, 0))
    target_x, target_y = pygame.mouse.get_pos()

    dx = target_x - circle_x
    dy = target_y - circle_y

    distance = math.hypot(dx, dy)

    if distance > stop_distance:
        move_distance = min(speed, distance - stop_distance)
        circle_x += (dx / distance) * move_distance
        circle_y += (dy / distance) * move_distance


    pygame.draw.circle(screen, (255, 0, 0), (int(circle_x), int(circle_y)), radius)
    clock.tick(60)
    
   
    print(circle_x, circle_y)
    pygame.display.flip()
    
    

pygame.quit()
