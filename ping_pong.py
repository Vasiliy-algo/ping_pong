from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_width, player_height, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1 (GameSprite):
    
    def update (self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y <= 820:
            self.rect.y += self.speed
        elif keys_pressed[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed

class Player2 (GameSprite):
    
    def update (self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y <= 820:
            self.rect.y += self.speed
        elif keys_pressed[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed    

class Ball (GameSprite):
    def __init__(self, player_image, player_width, player_height, player_x, player_y, player_speed):
        super().__init__(player_image, player_width, player_height, player_x, player_y, player_speed)
        self.y = 2
        self.x = 2
        self.h1 = 0
        self.h2 = 0

    def update (self):
        global p
        if self.h1 != 3 and self.h2 != 3:
            if self.y == 2:
                self.rect.y -= self.speed

            if self.y == 1:
                self.rect.y += self.speed

            if self.x == 2:
                self.rect.x -= self.speed

            if self.x == 1:
                self.rect.x += self.speed
            
            if self.rect.y <= 0:

                self.y = 1
            if self.rect.y >= 945:

                self.y = 2
            if sprite.collide_rect(ball, raketka1):
                self.x = 1
                p = 1
            if sprite.collide_rect(ball, raketka2):
                self.x = 2
                p = 2
    
    def win (self):
        
        if self.rect.x > 1500 and self.h1 != 3:
            global g1
            self.h1 += 1
            self.rect.x = 700
            self.rect.y = 500
            g1 += 1

        if self.rect.x < -150 and self.h2 != 3:
            global g2
            self.h2 += 1
            self.rect.x = 700
            self.rect.y = 500
            g2 += 1            
            
            
        if self.h1 >= 3 or self.h2 >= 3:
            global text_win
            window.blit(text_win, (400, 500))
            
            #text

        



#window.blit(text_win, (600, 500))
window = display.set_mode((1400, 1000))
display.set_caption('fon.jpg')

fon = transform.scale(image.load('fon.jpg'), (1400, 1000))

raketka1 = Player1('raketka1.png', 40, 200, 50, 400, 4)

raketka2 = Player2('raketka2.png', 40, 200, 1310, 400, 4)

ball = Ball('ball.png', 70, 70, 700, 500, 5 )

font.init()
font2 = font.Font(None, 72)



g1 = 0
g2 = 0
p = 2
game = True
clock = time.Clock()
FPS = 60
while game:
    text_win = font2.render('Победил игрок под номером ' + str(p), 1,(100,255,100))
    text_score1 = font2.render('Счёт первого ' + str(g1), 1,(30,0,255))
    text_score2 = font2.render('Счёт второго ' + str(g2), 1,(255,0,30))
    text_player1 = font2.render('1', 1,(30,0,255))
    text_player2 = font2.render('2', 1,(255,0,30))
    
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    window.blit(fon, (0,0))
    window.blit(text_player1, (10,10))
    window.blit(text_player2, (1360,10))
    window.blit(text_score1, (300,0))
    window.blit(text_score2, (700,0))
    
    raketka1.reset()
    raketka1.update()
    raketka2.reset()
    raketka2.update()
    ball.reset()
    ball.update()
    ball.win()        
    








    display.update()
    clock.tick(FPS)





#if sprite.collide_rect():