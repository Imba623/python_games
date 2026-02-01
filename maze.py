from pygame import *
from time import sleep
# цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# инициализация
font.init() # шрифт
mixer.init() # музыка

# настройки окна
is_win = False
game = True
win_width = 700
win_height = 500
window = display.set_mode(
(win_width, win_height)
)
display.set_caption("Maze")
background = transform.scale(image.load("bg.jpg"),  (win_width, win_height))

# Создание шрифта
font1 = font.SysFont('arial', 36)


#игрок
player = Rect(550, 450, 50, 50)
speed = 5
player_image = image.load("player.png") 
player_image = transform.scale(player_image, (50, 50))

# стена
wall1 = Rect(100, 100, 200, 20)
wall1_direction = 1 # 1 = вправо, -1 = влево


# Внутренние стены
wall2 = Rect(150, 100, 20, 150)   # Вертикальная 1
wall2_direction = 1

wall3 =Rect(400, 50, 200, 20)   # Горизонтальная 1
wall3_direction = 1

wall4 = Rect(350, 100, 20, 200)   # Вертикальная 2
wall4_direction = 1

wall5 = Rect(200, 250, 150, 20)   # Горизонтальная 2
wall5_direction = 1

wall6 = Rect(200, 250, 20, 150)   # Вертикальная 3
wall6_direction = 1

wall7 = Rect(300, 400, 200, 20)  # Горизонтальная 3
wall7_direction = 1

wall8 = Rect(400, 400, 20, 200)  # Вертикальная 4
wall8_direction = 1

wall9 = Rect(450, 150, 200, 20)  # Горизонтальная 4
wall9_direction = 1

#приз
win = Rect(0, 0, 70, 70)
# кадры в секунду
clock = time.Clock()
FPS = 60
#музыка
mixer.music.load('bg_sound.mp3')
mixer.music.play(-1)


while game:
    for e in event.get():
       if e.type == QUIT:
           game = False
    keys = key.get_pressed()
    if keys[K_LEFT] or keys[K_a]:
        player.x -= speed
    if keys[K_RIGHT]:
        player.x += speed
    if keys[K_UP]:
        player.y -= speed
    if keys[K_DOWN]:
        player.y += speed
    
    if player.colliderect(wall1) or player.colliderect(wall2) or player.colliderect(wall3) or player.colliderect(wall4) or player.colliderect(wall5) or player.colliderect(wall6) or player.colliderect(wall7) or player.colliderect(wall8) or player.colliderect(wall9):
            game = False
    
    if player.colliderect(win):
        game = False
        is_win = True

    wall1.x += speed * wall1_direction
    if wall1.right >= 700 or wall1.left <= 0:
        wall1_direction *= -1

    wall3.x += speed * wall3_direction
    if wall3.right >= 700 or wall3.left <= 0:
        wall3_direction *= -1
    
    wall5.x += speed * wall5_direction
    if wall5.right >= 700 or wall5.left <= 0:
        wall5_direction *= -1

    wall7.x += speed * wall7_direction
    if wall7.right >= 700 or wall7.left <= 0:
        wall7_direction *= -1
    
    wall9.x += speed * wall9_direction
    if wall9.right >= 700 or wall9.left <= 0:
        wall9_direction *= -1

    wall2.y += speed * wall2_direction
    if wall2.top >= 500 or wall2.bottom <= 0:
        wall2_direction *= -1
    
    wall4.y += speed * wall4_direction
    if wall4.top >= 500 or wall4.bottom <= 0:
        wall4_direction *= -1
    
    wall6.y += speed * wall6_direction
    if wall6.top >= 500 or wall6.bottom <= 0:
        wall6_direction *= -1
    
    wall8.y += speed * wall8_direction
    if wall8.top >= 500 or wall8.bottom <= 0:
        wall8_direction *= -1


    window.blit(background,(0, 0))
    draw.rect(window, BLUE, win)

    draw.rect(window, (255,255,255), wall1)
    draw.rect(window, (255,255,255), wall2)
    draw.rect(window, (255,255,255), wall3)
    draw.rect(window, (255,255,255), wall4)
    draw.rect(window, (255,255,255), wall5)
    draw.rect(window, (255,255,255), wall6)
    draw.rect(window, (255,255,255), wall7)
    draw.rect(window, (255,255,255), wall8)
    draw.rect(window, (255,255,255), wall9)

    draw.rect(window, (0,0,0), player)
    window.blit(player_image, player)
    
    display.update()
    clock.tick(FPS)


# Создание текстовой поверхности
if is_win:
    text_surface = font1.render('Победа', True, BLUE, WHITE)
else:
    text_surface = font1.render('Поражение', True, RED, WHITE)
# Область для текста
text_rect = text_surface.get_rect()
text_rect.center = (120, 20)

window.blit(text_surface, text_rect)
display.update()
sleep(2)