import pygame
import math

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Mr.Spinny")
screen.fill((0, 0, 0))

circle_x = 640
circle_y = 360


radius = 50
stop_distance = radius

speed = 5
min_speed = 1

direction_x = 1.0
direction_y = 0

turn_speed = 0.08

deceleration_distance = 150



is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            
    screen.fill((0, 0, 0))
    target_x, target_y = pygame.mouse.get_pos()

    dx = target_x - circle_x
    dy = target_y - circle_y
    distance = math.hypot(dx, dy)
    
    desired_x = dx/distance
    desired_y = dy/distance

    direction_x += (desired_x - direction_x) * turn_speed
    direction_y += (desired_y - direction_y) * turn_speed

    direction_length = math.hypot(direction_x, direction_y)

    direction_x /= direction_length
    direction_y /= direction_length

    if distance > stop_distance:
        if distance - stop_distance > deceleration_distance:
            current_speed = speed
        else:
            deceleration_distance = 150

            current_speed = max(min_speed, speed * (distance - stop_distance) / deceleration_distance)

            
        move_distance = min(current_speed, distance - stop_distance)
        

        circle_x += direction_x * move_distance
        circle_y += direction_y * move_distance


    pygame.draw.circle(screen, (255, 0, 0), (int(circle_x), int(circle_y)), radius)
    clock.tick(60)
    
   
    print(circle_x, circle_y)
    pygame.display.flip()
    
    

pygame.quit()

