import pygame,time,random

pygame.init()
pygame.display.set_icon(pygame.image.load("Assets/32bit Squadron logo.png"))
pygame.display.set_caption("32-bit Squadron") 

screen = screen = pygame.display.set_mode((pygame.display.Info().current_w / 2, pygame.display.Info().current_h / 2),pygame.RESIZABLE)
run = True
page = "menu"
pts = 0
keys = pygame.key.get_pressed()
prev_time = time.time()

def text(text,font,txtcol,txx,txy):
    txtsprite = font.render(text,True,txtcol)
    screen.blit(txtsprite,(txx,txy))

while run:
    x,y = screen.get_width(),screen.get_height()
    curr_time = time.time()
    delta_time = curr_time - prev_time
    prev_time = curr_time
    spvel = y / 720 * 1000 * delta_time
    vel = y / 720 * 600 * delta_time
    scaling = (x + y) / (1280 + 720)
    fontsize = int(scaling * 70)

    if page == "menu":
        screen.fill((0,50,0))
        pygame.draw.rect(screen,(70, 70, 70), pygame.Rect(0,  0, scaling* 700,  y))
        pygame.draw.rect(screen,(80, 80, 80), pygame.Rect(0, 0, scaling* 700, y-(scaling * 150)))
        gamestart = screen.blit(pygame.transform.scale(pygame.image.load("Assets/Start.png"), (scaling * 500, scaling * 105)),(scaling * 100, y / 2 - (scaling * 125)))
        gamecredits = screen.blit(pygame.transform.scale(pygame.image.load("Assets/Credits.png"), (scaling * 238, scaling * 100)),(scaling * 100, y / 2))
        gamequit = screen.blit(pygame.transform.scale(pygame.image.load("Assets/Quit.png"), (scaling * 238, scaling * 100)), (scaling * 362, y / 2))
        screen.blit(pygame.transform.scale(pygame.image.load("Assets/32bit Squadron logo.png"), (scaling * 400, scaling * 400)), ((x - (scaling * 300)) / 2 + (scaling * 300),y / 2 - (scaling * 250)))
        text("Points:",pygame.font.SysFont("freesansbold", fontsize), (255,255,255), scaling * 100, y-(scaling * 100))
        text(str(pts),pygame.font.SysFont("freesansbold", fontsize), (255,255,255), scaling * 352, y-(scaling * 100))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if gamestart.collidepoint(event.pos):
                    playersprite = "Assets/Player.png"
                    px = x / 2 - 40
                    py = y - 100
                    cx1 = random.randint(0, x-80)
                    cy1 = random.randint(-1000,0)
                    cx2 = random.randint(0, x-80)
                    cy2 = random.randint(-1000, 0)
                    cx3 = random.randint(0, x-80)
                    cy3 = random.randint(-1000, 0)
                    tx1 = random.randint(0, x-80)
                    ty1 = random.randint(-1000, 0)
                    tx2 = random.randint(0, x-80)
                    ty2 = random.randint(-1000, 0)
                    lx = random.randint(0, x-80)
                    ly = random.randint(-1000, 0)
                    ex1 = random.randint(0, x-80)
                    ey1 = random.randint(-1000, 0)
                    ex2 = random.randint(0, 1000)
                    ey2 = random.randint(-1000, 0)
                    ex3 = random.randint(0, x-80)
                    ey3 = random.randint(-1000, 0)
                    ex4 = random.randint(0, x-80)
                    ey4 = random.randint(-1000, 0)
                    ex5 = random.randint(0, x-80)
                    ey5 = random.randint(-1000, 0)
                    e1bmbx = ex1 + 35
                    e1bmby = ey1
                    e3bmbx = ex3 + 35
                    e3bmby = ey3
                    e5bmbx = ex5 + 35
                    e5bmby = ey5
                    bx = random.randint(0, x-80)
                    by = random.randint(-1000, 0)
                    prx = random.randint(0, x-80)
                    pry = random.randint(-1000, 0)
                    pts = 0
                    page = "game"
                if gamecredits.collidepoint(event.pos):
                    page = "credits"
                if gamequit.collidepoint(event.pos):
                    run = False
        if event.type == pygame.QUIT:
            run = False

    if page == "credits":
        screen.fill((0,50,0))
        pygame.draw.rect(screen,(70, 70, 70), pygame.Rect(0,  0, scaling* 700,  y))
        screen.blit(pygame.transform.scale(pygame.image.load("Assets/32bit Squadron logo.png"), (scaling * 400, scaling * 400)), ((x - (scaling * 300)) / 2 + (scaling * 300),y / 2 - (scaling * 250)))
        screen.blit(pygame.transform.scale(pygame.image.load("Assets/Credits Scene.png"), (scaling * 485, scaling * 282)),(scaling * 100,(y / 2 - (235 * scaling))))
        gamemenu= screen.blit(pygame.transform.scale(pygame.image.load("Assets/Main menu.png"), (scaling * 500, scaling * 105)), (scaling * 100, (y / 2 + 100 * scaling)))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if gamemenu.collidepoint(event.pos):
                   page = "menu"
            if event.type == pygame.QUIT:
                run = False
    
    if page == "game":
        screen.fill((0,50,0))

        py = y - 100 * scaling

        screen.blit(pygame.transform.scale(pygame.image.load("Assets/Lake.png"),(scaling * 100, scaling * 100)), (lx, ly))
        screen.blit(pygame.transform.scale(pygame.image.load("Assets/Tree.png"),(scaling * 100, scaling *100)), (tx1,ty1))
        screen.blit(pygame.transform.scale(pygame.image.load("Assets/Tree.png"),(scaling * 100, scaling *100)),(tx2,ty2))
        screen.blit(pygame.transform.scale(pygame.image.load("Assets/Base.png"),(scaling * 100, scaling * 100)), (bx, by))
        screen.blit(pygame.transform.scale(pygame.image.load("Assets/Parachute.png"), (scaling * 100, scaling * 100)), (prx,pry))
        player = screen.blit(pygame.transform.scale(pygame.image.load(playersprite), (scaling * 100, scaling * 100)), (px,py))
        enemy1 = screen.blit(pygame.transform.scale(pygame.image.load("Assets/BF-109.png"), (scaling *100, scaling * 100)), (ex1,ey1))
        e1bomb = screen.blit(pygame.transform.scale(pygame.image.load("Assets/bomb.png"), (scaling * 32, scaling * 32)),(e1bmbx,e1bmby))
        enemy2 = screen.blit(pygame.transform.scale(pygame.image.load("Assets/Avro Lancaster.png"), (scaling * 100, scaling * 100)), (ex2,ey2))
        enemy3 = screen.blit(pygame.transform.scale(pygame.image.load("Assets/Bomber.png"), (scaling * 100, scaling * 100)), (ex3,ey3))
        e3bomb = screen.blit(pygame.transform.scale(pygame.image.load("Assets/bomb.png"), (scaling * 32, scaling * 32)), (e3bmbx,e3bmby))
        enemy4 = screen.blit(pygame.transform.scale(pygame.image.load("Assets/Warthog.png"), (scaling * 100, scaling * 100)), (ex4,ey4))
        enemy5 = screen.blit(pygame.transform.scale(pygame.image.load("Assets/Tomcat.png"), (scaling * 100, scaling * 100)), (ex5,ey5))
        e5bomb = screen.blit(pygame.transform.scale(pygame.image.load("Assets/bomb.png"), (scaling * 32, scaling * 32)), (e5bmbx,e5bmby))
        screen.blit(pygame.transform.scale(pygame.image.load("Assets/Cloud 1.png"), (scaling * 150, scaling * 48)), (cx1,cy1))
        screen.blit(pygame.transform.scale(pygame.image.load("Assets/Cloud 2.png"), (scaling * 150, scaling * 72)), (cx2,cy2))
        screen.blit(pygame.transform.scale(pygame.image.load("Assets/Cloud 3.png"), (scaling * 150, scaling * 51)), (cx3,cy3))
        text(str(pts),pygame.font.SysFont("freesansbold",int(120 * scaling)),(255,255,255),10,10)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] and px < x - scaling * 100 and keys[pygame.K_a] and px > 0 or keys[pygame.K_RIGHT] and px < x - scaling * 100 and keys[pygame.K_LEFT] and px > 0:
            playersprite = "Assets/Player.png"
        elif keys[pygame.K_d] and px < x - scaling * 100 or keys[pygame.K_RIGHT] and px < x - scaling * 100:
            px += spvel
            playersprite = "Assets/Player R.png"
        elif keys[pygame.K_a] and px > 0 or keys[pygame.K_LEFT] and px > 0:
            px -= spvel
            playersprite = "Assets/Player L.png"
        else:
            playersprite = "Assets/Player.png"

        if px > x - scaling * 100:
            px = x - scaling * 100

        if (pygame.Rect.colliderect(player, enemy1) or
            pygame.Rect.colliderect(player, e1bomb) or
            pygame.Rect.colliderect(player, enemy2) or
            pygame.Rect.colliderect(player, enemy3) or
            pygame.Rect.colliderect(player, e3bomb) or
            pygame.Rect.colliderect(player, enemy4) or
            pygame.Rect.colliderect(player, enemy5) or
            pygame.Rect.colliderect(player, e5bomb)):
                page = "menu"
                
        if cx1 > x or cy1 > y:
            cx1 = random.randint(-80,y)
            cy1 = random.randint(-1000,-100)
        else:
            cy1 += vel
            cx1 += 50 * delta_time
        if cx2 > x or cy2 > y:
            cx2 = random.randint(-80,y)
            cy2 = random.randint(-1000,-100)
        else:
            cy2 += vel
            cx2 += 50 * delta_time
        if cx3 > x or cy3 > y:
            cx3 = random.randint(-80,y)
            cy3 = random.randint(-1000,-100)
        else:
            cy3 += vel
            cx3 += 50 * delta_time

        if ty1 > y:
            tx1 = random.randint(0,x-80)
            ty1 = random.randint(-1000,-100)
        else:
           ty1 += vel
        if ty2 > y:
            tx2 = random.randint(0,x-80)
            ty2 = random.randint(-1000,-100)
        else:
            ty2 += vel

        if ly > y:
            lx = random.randint(0,x-80)
            ly = random.randint(-1000,-100)
        else:
            ly += vel

        if by > y:
            bx = random.randint(0,x-80)
            by = random.randint(-1000,-100)
        else:
            by += vel

        if pry > y:
            prx = random.randint(0,x-80)
            pry = random.randint(-1000,-100)
        else:
            pry += vel

        if ey1 > y:
            ex1 = random.randint(0,x-80)
            ey1 = random.randint(-1000,-100)
            e1bmbx = ex1 + 34 * scaling
            e1bmby = ey1 + 50 * scaling
            pts += 1
        else:
            ey1 += spvel
            e1bmby += spvel + 2 * scaling
        if ey2 > y:
            ex2 = random.randint(0,x-80)
            ey2 = random.randint(-1000,-100)
            pts += 1
        else:
            ey2 += spvel
        if ey3 > y:
            ex3 = random.randint(0,x-80)
            ey3 = random.randint(-1000,-100)
            e3bmbx = ex3 + 34 * scaling
            e3bmby = ey3 + 50 * scaling
            pts += 1
        else:
            ey3 += spvel
            e3bmby += spvel + 2 * scaling
        if ey4 > y:
            ex4 = random.randint(0,x-80)
            ey4 = random.randint(-1000,-100)
        else:
           ey4 += spvel
        if ey5 > y:
            ex5 = random.randint(0,x-80)
            ey5 = random.randint(-1000,-100)
            e5bmbx = ex5 + 34 * scaling
            e5bmby = ey5 + 50 * scaling
            pts += 1
        else:
            ey5 += spvel
            e5bmby += spvel + 2 * scaling
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.display.update()
    
pygame.quit()
