import sys
import pygame
from colors import Colors
from game import Game

pygame.init()

title_font =pygame.font.Font(None, 40)
choi_lai_font=pygame.font.Font(None,25)
button=pygame.font.Font(None,22)
score_surface=title_font.render(" Diem",True,Colors.white)
game_over_surface=title_font.render(" Thua Cuoc",True,Colors.white)
choi_lai=choi_lai_font.render("Nhan Space de choi lai",True, Colors.white)
sang_trai=button.render("Sang trai: Mui ten trai",True, Colors.white)
sang_phai=button.render("Sang phai: Mui ten phai ",True, Colors.white)
di_xuong=button.render("Di xuong: Mui ten xuong",True, Colors.white)
quay_khoi=button.render("Quay block: Mui ten len",True, Colors.white)
score_rect=pygame.Rect(320,55,170,60)

screen=pygame.display.set_mode((500,620))
pygame.display.set_caption("Tetris")

clock=pygame.time.Clock()

game=Game()
GAME_UPDATE=pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE,300)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and game.game_over==True:
                game.game_over=False
                game.reset()
            if event.key==pygame.K_LEFT and game.game_over==False:
                game.move_left()
            if event.key==pygame.K_RIGHT and game.game_over==False:
                game.move_right()
            if event.key==pygame.K_DOWN and game.game_over==False:
                game.move_down()
                game.update_score(0,1)
            if event.key==pygame.K_UP and game.game_over==False:
                game.rotate()
        if event.type==GAME_UPDATE and game.game_over==False:
           game.move_down()

    score_value_surface=title_font.render(str(game.score),True,Colors.white)
    screen.fill(Colors.dark_blue)
    screen.blit(score_surface,(365,20,50,50))
    screen.blit(sang_phai,(320, 200, 0, 0))
    screen.blit(sang_trai,(320, 250, 0, 0))
    screen.blit(di_xuong,(320, 300, 0, 0))
    screen.blit(quay_khoi,(320, 350, 0, 0))
    if game.game_over == True:
        screen.blit(game_over_surface,(320,450,50,50))
        screen.blit(choi_lai,(310,500,50,50))
    pygame.draw.rect(screen,Colors.light_blue,score_rect,0,10)
    screen.blit(score_value_surface,score_value_surface.get_rect(centerx=score_rect.centerx,centery=score_rect.centery))
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)