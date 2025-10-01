import pygame
time=pygame.time.Clock()
pygame.init()

screen=pygame.display.set_mode((736,414))

pygame.display.set_caption("My Game")
sprite=pygame.image.load("photo/sprite/sprite.png")
platform=pygame.transform.scale(pygame.image.load("photo/platform.png"), (70,70))
bg=pygame.image.load("photo/bg.jpg").convert()
jump_sound=pygame.mixer.Sound("sound/jump.mp3")
bg_sound=pygame.mixer.Sound("sound/sound.wav")
bg_sound.play()
def coloissia(w):
        global velocity_y, jumping, x_player, y_player
        if player_rect.colliderect(w):
            if velocity_y > 0 and player_rect.bottom <= w.top + velocity_y:
                y_player = w.top - razmer_persa
                velocity_y = 0
                jumping = True

            elif velocity_y < 0 and w.top >= w.bottom - velocity_y:
                y_player = w.bottom
                velocity_y = 0
                
            elif player_rect.left < platform_rect.right and player_rect.centerx > platform_rect.right:
                x_player = platform_rect.right

            elif player_rect.right > platform_rect.left and player_rect.centerx < platform_rect.left:
                x_player = platform_rect.left - razmer_persa
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
poza=None
x_player, y_player=400, 300
gravity=3
velocity_y=0
player_speed=20
jump_force=25
bg_x=0
jumping=None
zemla=380
bg_width, bg_height=bg.get_size()
x_platform=[600]
y_platform=[310]
while True:
    time.tick(15)

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
    screen.blit(bg, (bg_x+736, 0))

    if anim==3:
        anim=0
    if keys[pygame.K_a]:
        left=True
        right=False
        anim += 1
        poza=None
        x_player-=player_speed
    elif keys[pygame.K_d]:
        left=False
        right=True
        anim += 1
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
        bg_x-=20
        x_player=600
        x_platform[0]-=20

    if bg_x==-736:
        bg_x=0

    if event.type == pygame.KEYUP:   # анимация стояния персонажа             
        if event.key == pygame.K_a:
            anim=0
            poza=True
        elif event.key == pygame.K_d:                                                                                           
            anim=0
            poza=False      
        poloshenie(poza)                          

    screen.blit(platform, (x_platform[0], y_platform[0]))
    player_rect = pygame.Rect(x_player, y_player, razmer_persa, razmer_persa)
    platform_rect = platform.get_rect(topleft=(x_platform[0], y_platform[0]))
    coloissia(platform_rect) 



    pygame.display.update()