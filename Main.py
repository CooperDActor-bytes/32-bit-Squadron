import pygame,time,random

pygame.init()
pygame.display.set_icon(pygame.image.load("Assets/32bit Squadron logo.png"))
pygame.display.set_caption("32-bit Squadron") 

screen = pygame.display.set_mode((1280,720),pygame.RESIZABLE)
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
    vel = y / 720 * 800 * delta_time

    if page == "menu":
        screen.fill((0,50,0))
        
        pygame.draw.rect(screen,(70,70,70),pygame.Rect(0,0,700,y))
        pygame.draw.rect(screen,(80,80,80),pygame.Rect(0,0,700,y-150))
        gamestart = screen.blit(pygame.image.load("Assets/Start.png"),(100,y / 2 - 125))
        gamecredits = screen.blit(pygame.image.load("Assets/Credits.png"),(100,y / 2 + 10))
        gamequit = screen.blit(pygame.image.load("Assets/Quit.png"),(362,y / 2 + 10))
        screen.blit(pygame.image.load("Assets/32bit Squadron logo.png"),((x - 300) / 2 + 300,y / 2 - 250))
        text("Points:",pygame.font.SysFont("Bahnscript",100),(255,255,255),100,y-100)
        text(str(pts),pygame.font.SysFont("Bahnscript",100),(255,255,255),352,y-100)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if gamestart.collidepoint(event.pos):
                    playersprite = "Assets/Player.png"
                    px = x / 2 - 40
                    py = y - 100
                    cx1 = random.randint(0,x-80)
                    cy1 = random.randint(-1000,0)
                    cx2 = random.randint(0,x-80)
                    cy2 = random.randint(-1000,0)
                    cx3 = random.randint(0,x-80)
                    cy3 = random.randint(-1000,0)
                    tx1 = random.randint(0,x-80)
                    ty1 = random.randint(-1000,0)
                    tx2 = random.randint(0,x-80)
                    ty2 = random.randint(-1000,0)
                    lx = random.randint(0,x-80)
                    ly = random.randint(-1000,0)
                    ex1 = random.randint(0,x-80)
                    ey1 = random.randint(-1000,0)
                    ex2 = random.randint(0,1000)
                    ey2 = random.randint(-1000,0)
                    ex3 = random.randint(0,x-80)
                    ey3 = random.randint(-1000,0)
                    ex4 = random.randint(0,x-80)
                    ey4 = random.randint(-1000,0)
                    ex5 = random.randint(0,x-80)
                    ey5 = random.randint(-1000,0)
                    e1bmbx = ex1 + 35
                    e1bmby = ey1
                    e3bmbx = ex3 + 35
                    e3bmby = ey3
                    e5bmbx = ex5 + 35
                    e5bmby = ey5
                    bx = random.randint(0,x-80)
                    by = random.randint(-1000,0)
                    prx = random.randint(0,x-80)
                    pry = random.randint(-1000,0)
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
        pygame.draw.rect(screen,(80,80,80),pygame.Rect(0,0,700,y))
        screen.blit(pygame.image.load("Assets/32bit Squadron logo.png"),((x - 300) / 2 + 300,y / 2 - 250))
        screen.blit(pygame.image.load("Assets/Credits Scene.png"),((100),y / 2 - 235))
        gamemenu = screen.blit(pygame.image.load("Assets/Main menu.png"),(100,y / 2 + 100))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if gamemenu.collidepoint(event.pos):
                   page = "menu"
            if event.type == pygame.QUIT:
                run = False
    
    if page == "game":
        screen.fill((0,50,0))

        py = y - 100

        screen.blit(pygame.image.load("Assets/Lake.png"),(lx,ly))
        screen.blit(pygame.image.load("Assets/Tree.png"),(tx1,ty1))
        screen.blit(pygame.image.load("Assets/Tree.png"),(tx2,ty2))
        screen.blit(pygame.image.load("Assets/Base.png"),(bx,by))
        screen.blit(pygame.image.load("Assets/Parachute.png"),(prx,pry))
        player = screen.blit(pygame.image.load(playersprite),(px,py))
        enemy1 = screen.blit(pygame.image.load("Assets/BF-109.png"),(ex1,ey1))
        e1bomb = screen.blit(pygame.image.load("Assets/bomb.png"),(e1bmbx,e1bmby))
        enemy2 = screen.blit(pygame.image.load("Assets/Avro Lancaster.png"),(ex2,ey2))
        enemy3 = screen.blit(pygame.image.load("Assets/Bomber.png"),(ex3,ey3))
        e3bomb = screen.blit(pygame.image.load("Assets/bomb.png"),(e3bmbx,e3bmby))
        enemy4 = screen.blit(pygame.image.load("Assets/Warthog.png"),(ex4,ey4))
        enemy5 = screen.blit(pygame.image.load("Assets/Tomcat.png"),(ex5,ey5))
        e5bomb = screen.blit(pygame.image.load("Assets/bomb.png"),(e5bmbx,e5bmby))
        screen.blit(pygame.image.load("Assets/Cloud 1.png"),(cx1,cy1))
        screen.blit(pygame.image.load("Assets/Cloud 2.png"),(cx2,cy2))
        screen.blit(pygame.image.load("Assets/Cloud 3.png"),(cx3,cy3))
        text(str(pts),pygame.font.SysFont("Bahnscript",150),(255,255,255),10,10)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] and px < x-80 and keys[pygame.K_a] and px > 0 or keys[pygame.K_RIGHT] and px < x-80 and keys[pygame.K_LEFT] and px > 0:
            playersprite = "Assets/Player.png"
        elif keys[pygame.K_d] and px < x-80 or keys[pygame.K_RIGHT] and px < x-80:
            px += spvel
            playersprite = "Assets/Player R.png"
        elif keys[pygame.K_a] and px > 0 or keys[pygame.K_LEFT] and px > 0:
            px -= spvel
            playersprite = "Assets/Player L.png"
        else:
            playersprite = "Assets/Player.png"

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
            cy1 = random.randint(-100,0)
        else:
            cy1 += vel
            cx1 += 50 * delta_time
        if cx2 > x or cy2 > y:
            cx2 = random.randint(-80,y)
            cy2 = random.randint(-100,0)
        else:
            cy2 += vel
            cx2 += 50 * delta_time
        if cx3 > x or cy3 > y:
            cx3 = random.randint(-80,y)
            cy3 = random.randint(-100,0)
        else:
            cy3 += vel
            cx3 += 50 * delta_time

        if ty1 > y:
            tx1 = random.randint(0,x-80)
            ty1 = random.randint(-100,0)
        else:
           ty1 += vel
        if ty2 > y:
            tx2 = random.randint(0,x-80)
            ty2 = random.randint(-100,0)
        else:
            ty2 += vel

        if ly > y:
            lx = random.randint(0,x-80)
            ly = random.randint(-100,0)
        else:
            ly += vel

        if by > y:
            bx = random.randint(0,x-80)
            by = random.randint(-100,0)
        else:
            by += vel

        if pry > y:
            prx = random.randint(0,x-80)
            pry = random.randint(-100,0)
        else:
            pry += vel

        if ey1 > y:
            ex1 = random.randint(0,x-80)
            ey1 = random.randint(-100,0)
            e1bmbx = ex1 + 34
            e1bmby = ey1 + 50
            pts += 1
        else:
            ey1 += spvel
            e1bmby += spvel + 2
        if ey2 > y:
            ex2 = random.randint(0,x-80)
            ey2 = random.randint(-100,0)
            pts += 1
        else:
            ey2 += spvel
        if ey3 > y:
            ex3 = random.randint(0,x-80)
            ey3 = random.randint(-100,0)
            e3bmbx = ex3 + 34
            e3bmby = ey3 + 50
            pts += 1
        else:
            ey3 += spvel
            e3bmby += spvel + 2
        if ey4 > y:
            ex4 = random.randint(0,x-80)
            ey4 = random.randint(-100,0)
        else:
           ey4 += spvel
        if ey5 > y:
            ex5 = random.randint(0,x-80)
            ey5 = random.randint(-100,0)
            e5bmbx = ex5 + 34
            e5bmby = ey5 + 50
            pts += 1
        else:
            ey5 += spvel
            e5bmby += spvel + 2
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.display.update()
    
pygame.quit()
