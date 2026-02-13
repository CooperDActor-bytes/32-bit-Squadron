import pygame,time,random

pygame.init()
pygame.display.Info
pygame.display.set_icon(pygame.image.load("Assets/32bit Squadron logo.png"))
pygame.display.set_caption("32-bit Squadron v1.1.0-Alpha")

screen = pygame.display.set_mode((pygame.display.Info().current_w / 2, pygame.display.Info().current_h / 2),pygame.RESIZABLE)
run = True
page = "menu"
pts = 0
keys = pygame.key.get_pressed()
prev_time = time.time()

def text(text,font,color,x,y):
    txtsprite = font.render(text,True,color)
    screen.blit(txtsprite,(x,y))

while run:
    x,y = screen.get_width(),screen.get_height()
    # define variables related to delta time
    curr_time = time.time()
    delta_time = curr_time - prev_time
    prev_time = curr_time
    # define the velocity
    spvel = y / 720 * 100 * delta_time
    vel = y / 720 * 600 * delta_time
    # scaling 
    scale = (x + y) / (1280 + 720)

    text("test", pygame.font.SysFont("freesansbold", int(scale * 70)), (255, 255, 255),100 * scale, 100 * scale)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    
pygame.quit()
