import pygame
time=pygame.time.Clock()
pygame.init()

screen=pygame.display.set_mode((736,414))

pygame.display.set_caption("My Game")

interface=pygame.image.load("photo/interface.jpg").convert_alpha()
button=pygame.transform.scale(pygame.image.load("photo/button.png"), (200,100))
button_hover=pygame.transform.scale(pygame.image.load("photo/button1.png"), (200,100))
interface=pygame.transform.scale(pygame.image.load("photo/interface.jpg"), (736,414))
pause=pygame.transform.scale(pygame.image.load("photo/pause.png"), (70,65))
pause_hover=pygame.transform.scale(pygame.image.load("photo/pause1.png"), (70,65))
enemy=pygame.transform.scale(pygame.image.load("photo/enemy.png"), (50,50))
dead=pygame.transform.scale(pygame.image.load("photo/dead.png"), (300,140))
dead_button=pygame.transform.scale(pygame.image.load("photo/dead_button.png"), (175,80))
flag=pygame.transform.scale(pygame.image.load("photo/flag.png"), (100,90))
win=pygame.transform.scale(pygame.image.load("photo/win.jpg"), (736,414))
menu_button=pygame.transform.scale(pygame.image.load("photo/menu.png"), (240,150))
game_state="menu"
button_rect = button.get_rect(topleft=(270, 150))
menu_button_rect = button.get_rect(topleft=(250, 270))
dead_button_rect = dead_button.get_rect(topleft=(280,250))
pause_rect = pause.get_rect(topleft=(665, 0))
interface_rect = interface.get_rect(topleft=(0, 0))

platform_files = [
    "photo/platform.png",
    "photo/platform1.jpg",
    "photo/platform2.png",
    "photo/platform.png",
    "photo/platform4.png",
    "photo/platform5.png",
    "photo/platform5.png",
    "photo/platform5.png",
]
platform_size=((50, 100), (50, 30), (50, 70), (50, 100), (50, 120),(65,40),(65,40),(65,40))
platform=[]
for file, size in zip(platform_files, platform_size):
    platform.append(pygame.transform.scale(pygame.image.load(file), (size)))

goblin=pygame.transform.scale(pygame.image.load("photo/goblin/goblin1.png"), (60,60))
block=pygame.transform.scale(pygame.image.load("photo/block.jpg"), (40,40))
coin=pygame.transform.scale(pygame.image.load("photo/coin.png"), (50,40))
bg=pygame.image.load("photo/bg.jpg").convert()
jump_sound=pygame.mixer.Sound("sound/jump.mp3")
bg_sound=pygame.mixer.Sound("sound/sound.wav")
over_sound=pygame.mixer.Sound("sound/over.mp3")
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
def reboot(x_coin,y_coin,x_player,y_player,x_platform,y_platform,x_block,y_block,x_enemy,y_enemy,x_flag,y_flag):
    x_coin,y_coin=1600,330
    x_player, y_player=250,300
    x_platform=[600,800,1000,1200,1400,1600,1750,1850]
    y_platform=[285,330,300,285,255,265,265,265]
    x_block=[415,455,495,455]
    y_block=[340,340,340,300]
    x_enemy=[1500,1760]
    y_enemy=[320,218]
    x_flag,y_flag=2200,285
    return x_coin,y_coin,x_player,y_player,x_platform,y_platform,x_block,y_block,x_enemy,y_enemy,x_flag,y_flag
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
music=False
anim=0
anim_delay=5
poza=None
x_player, y_player=250, 300
x_enemy=[1500,1760]
y_enemy=[320,218]
x_coin=1600
y_coin=330
gravity=1.2
velocity_y=0
player_speed=10
jump_force=17
bg_x=0
jumping=None
zemla=380
x_flag,y_flag=2200,285
bg_width, bg_height=bg.get_size()
x_platform=[600,800,1000,1200,1400,1600,1750,1850]
y_platform=[285,330,300,285,255,265,265,265]
x_block=[415,455,495,455]
y_block=[340,340,340,300]
coin_rect = dead_button.get_rect(topleft=(x_coin, y_coin))
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
    if game_state=="menu":  #состояние игры
        if music==True:
            bg_sound.stop()
            music=False
        pygame.display.update()
        screen.blit(interface, interface_rect)
        screen.blit(button_hover, button_rect)
        mouse_pos=pygame.mouse.get_pos()
        mouse_click=pygame.mouse.get_pressed()
        if button_rect.collidepoint(mouse_pos):
            screen.blit(button, button_rect)
        if button_rect.collidepoint(mouse_pos) and mouse_click[0]:
            bg_sound.play()
            game_state="play"
    if game_state=="dead":
        bg_sound.stop()
        pygame.display.update()
        screen.blit(interface, interface_rect)
        screen.blit(dead, (218,50))
        screen.blit(dead_button, dead_button_rect)
        mouse_pos=pygame.mouse.get_pos()
        mouse_click=pygame.mouse.get_pressed()
        if dead_button_rect.collidepoint(mouse_pos) and mouse_click[0]:
            over_sound.stop()
            x_coin,y_coin,x_player,y_player,x_platform,y_platform,x_block,y_block,x_enemy,y_enemy,x_flag,y_flag = reboot(x_coin,y_coin,x_player,y_player,x_platform,y_platform,x_block,y_block,x_enemy,y_enemy,x_flag,y_flag)
            bg_x=0
            bg_sound.play()
            game_state="play" 
    if game_state=="win":
        pygame.display.update()
        screen.blit(win, (0,0))
        screen.blit(menu_button,menu_button_rect)
        mouse_pos=pygame.mouse.get_pos()
        mouse_click=pygame.mouse.get_pressed()
        if menu_button_rect.collidepoint(mouse_pos) and mouse_click[0]:
            game_state="menu"
            x_coin,y_coin,x_player,y_player,x_platform,y_platform,x_block,y_block,x_enemy,y_enemy,x_flag,y_flag = reboot(x_coin,y_coin,x_player,y_player,x_platform,y_platform,x_block,y_block,x_enemy,y_enemy,x_flag,y_flag)
    if game_state=="play":
        bg_sound.play
        if music==False:
            music=True
        keys = pygame.key.get_pressed()
        if bg_x<=-bg_width: #передвижение фона
            bg_x=0 
            
        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x+bg_width, 0))
        screen.blit(bg, (bg_x-bg_width, 0))

        screen.blit(coin,(x_coin,y_coin))
        screen.blit(flag,(x_flag,y_flag)) 

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
        
        if keys[pygame.K_d] and x_player>=450: #движение фона влево
            x_flag-=10
            x_coin-=10
            for i in range(len(x_enemy)):
                x_enemy[i]-=10
            bg_x-=10
            x_player=450
            for i in range(len(x_block)):
                x_block[i]-=10
            for i in range(len(x_platform)):
                x_platform[i]-=10
        elif keys[pygame.K_a] and x_player<=150: #движение фона вправо
            x_flag+=10
            x_coin+=10
            for i in range(len(x_enemy)):
                x_enemy[i]+=10
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
        for i in range(len(x_platform)):
            screen.blit(platform[i], (x_platform[i], y_platform[i]))
            platform_rect = platform[i].get_rect(topleft=(x_platform[i], y_platform[i]))
            coloissia(platform_rect)

        for i in range(len(x_block)):
            screen.blit(block, (x_block[i], y_block[i]))
            block_rect = block.get_rect(topleft=(x_block[i], y_block[i]))
            coloissia(block_rect)
        for x,y in zip(x_enemy, y_enemy):
            screen.blit(enemy,(x,y))
            if player_rect.colliderect(enemy.get_rect(topleft=(x,y))):
                over_sound.play()
                game_state="dead"
        if player_rect.colliderect(flag.get_rect(topleft=(x_flag, y_flag))):
            game_state="win"
        if player_rect.colliderect(coin.get_rect(topleft=(x_coin,y_coin))):
            y_coin=900
        mouse_pos=pygame.mouse.get_pos()
        mouse_click=pygame.mouse.get_pressed()
        screen.blit(pause, pause_rect)
        if pause_rect.collidepoint(mouse_pos):
            screen.blit(pause_hover, pause_rect)
        if pause_rect.collidepoint(mouse_pos) and mouse_click[0]:
            game_state="menu"
        pygame.display.update()