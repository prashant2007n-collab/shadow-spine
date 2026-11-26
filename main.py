import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Mr.Spinny")
screen.fill((0, 0, 0))


is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            
    screen.fill((0, 0, 0))
    x, y = pygame.mouse.get_pos()
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 50)
    clock.tick(60)
    
   
    print(x, y)
    pygame.display.flip()
    
    

pygame.quit()
