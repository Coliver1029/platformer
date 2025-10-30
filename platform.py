import pygame
time=pygame.time.Clock()
pygame.init()

screen=pygame.display.set_mode((736,414))

pygame.display.set_caption("My Game")

platform=pygame.transform.scale(pygame.image.load("photo/platform.png"), (50,100))
platform1=pygame.transform.scale(pygame.image.load("photo/platform1.jpg"), (50,30))
platform2=pygame.transform.scale(pygame.image.load("photo/platform2.png"), (50,70))
platform3=pygame.transform.scale(pygame.image.load("photo/platform2.png"), (50,100))
goblin=pygame.transform.scale(pygame.image.load("photo/goblin/goblin1.png"), (50,50))
block=pygame.transform.scale(pygame.image.load("photo/block.jpg"), (40,40))
bg=pygame.image.load("photo/bg.jpg").convert()
jump_sound=pygame.mixer.Sound("sound/jump.mp3")
bg_sound=pygame.mixer.Sound("sound/sound.wav")
bg_sound.play()
def coloissia(w):
        global velocity_y, jumping, x_player, y_player, player_rect
        if player_rect.colliderect(w):
            if velocity_y > 0 and player_rect.bottom <= w.top + velocity_y:
                y_player = w.top - razmer_persa
                velocity_y = 0
                jumping = True

            elif velocity_y < 0 and w.top >= w.bottom - velocity_y:
                y_player = w.bottom
                velocity_y = 0
                
            elif player_rect.left < w.right and player_rect.centerx > w.right:
                x_player = w.right

            elif player_rect.right > w.left and player_rect.centerx < w.left:
                x_player = w.left - razmer_persa
def poloshenie(yslovie):
    if yslovie==True:
        screen.blit(walk_left[0], (x_player, y_player))
    elif yslovie==False:
        screen.blit(walk_right[0], (x_player, y_player))
razmer_persa=60
walk_left=[
    pygame.transform.scale(pygame.image.load("photo/sprite/left/sprite 1.png"), (razmer_persa, razmer_persa)),
    pygame.transform.scale(pygame.image.load("photo/sprite/left/sprite 2.png"), (razmer_persa, razmer_persa)),
    pygame.transform.scale(pygame.image.load("photo/sprite/left/sprite 3.png"), (razmer_persa, razmer_persa)),
    pygame.transform.scale(pygame.image.load("photo/sprite/left/sprite 4.png"), (razmer_persa, razmer_persa)),
]
walk_right=[
    pygame.transform.scale(pygame.image.load("photo/sprite/right/sprite 1.png"), (razmer_persa, razmer_persa)),
    pygame.transform.scale(pygame.image.load("photo/sprite/right/sprite 2.png"), (razmer_persa, razmer_persa)),
    pygame.transform.scale(pygame.image.load("photo/sprite/right/sprite 3.png"), (razmer_persa, razmer_persa)),
    pygame.transform.scale(pygame.image.load("photo/sprite/right/sprite 4.png"), (razmer_persa, razmer_persa)),
]
left=False
right=True
anim=0
anim_delay=5
poza=None
x_player, y_player=250, 300
gravity=1.2
velocity_y=0
player_speed=10
jump_force=17
bg_x=0
jumping=None
zemla=380
bg_width, bg_height=bg.get_size()
x_platform=[600,800,1000,1200]
y_platform=[285,330,300,285]
x_block=[415,455,495,455]
y_block=[340,340,340,300]
while True:
    time.tick(60)

    velocity_y += gravity
    y_player += velocity_y

    if y_player + razmer_persa >=zemla :
        y_player = zemla - razmer_persa
        velocity_y = 0
        jumping = True
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()

    if bg_x<=-bg_width: #передвижение фона
        bg_x=0 
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x+bg_width, 0))
    screen.blit(bg, (bg_x-bg_width, 0))

    if anim==3:
        anim=0
    if keys[pygame.K_a]:
        left=True
        right=False
        anim_delay+=1
        if anim_delay>=7:
            anim_delay=0
            anim+=1
        poza=None
        x_player-=player_speed
    elif keys[pygame.K_d]:
        left=False
        right=True
        anim_delay+=1
        if anim_delay>=7:
            anim_delay=0
            anim+=1
        poza=None
        x_player+=player_speed
    if keys[pygame.K_SPACE] and jumping==True:
        jump_sound.play()
        jumping = False
        velocity_y = -jump_force
    if right==True:
        screen.blit(walk_right[anim], (x_player, y_player))
    elif left==True:
        screen.blit(walk_left[anim], (x_player, y_player))
    if x_player<=50: #стоп игрока у края экрана слева
        x_player=50
    
    if keys[pygame.K_d] and x_player>=600: #движение фона влево
        bg_x-=10
        x_player=600
        for i in range(len(x_block)):
            x_block[i]-=10
        for i in range(len(x_platform)):
            x_platform[i]-=10
    elif keys[pygame.K_a] and x_player<=150: #движение фона вправо
        bg_x+=10
        x_player=150
        for i in range(len(x_block)):
            x_block[i]+=10
        for i in range(len(x_platform)):
            x_platform[i]+=10
    if bg_x==-bg_width:
        bg_x=0
    elif bg_x>=bg_width:
        bg_x=0

    if event.type == pygame.KEYUP:   # анимация стояния персонажа         
        if event.key == pygame.K_a:
            anim=0
            poza=True
        elif event.key == pygame.K_d:                                                                                           
            anim=0
            poza=False      
        poloshenie(poza)                          

    player_rect = pygame.Rect(x_player, y_player, razmer_persa, razmer_persa)
    screen.blit(platform, (x_platform[0], y_platform[0]))


    screen.blit(platform, (x_platform[0], y_platform[0]))
    platform_rect = platform.get_rect(topleft=(x_platform[0], y_platform[0]))
    coloissia(platform_rect)

    screen.blit(platform1, (x_platform[1], y_platform[1]))
    platform1_rect = platform1.get_rect(topleft=(x_platform[1], y_platform[1]))
    coloissia(platform1_rect)

    screen.blit(platform2, (x_platform[2], y_platform[2]))
    platform2_rect = platform2.get_rect(topleft=(x_platform[2], y_platform[2]))
    coloissia(platform2_rect)

    screen.blit(platform, (x_platform[3], y_platform[3]))
    platform3_rect = platform.get_rect(topleft=(x_platform[3], y_platform[3]))
    coloissia(platform3_rect)

    for i in range(len(x_block)):
        screen.blit(block, (x_block[i], y_block[i]))
        block_rect = block.get_rect(topleft=(x_block[i], y_block[i]))
        coloissia(block_rect)


    pygame.display.update()