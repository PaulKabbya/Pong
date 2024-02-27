import pygame as py, sys, random

py.init()

WIDTH, HEIGHT = 1280, 720

FONT = py.font.SysFont("Consolas", int(WIDTH/20))

SCREEN = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Pong!")
CLOCK = py.time.Clock()

#Paddles
player = py.Rect(WIDTH-110, HEIGHT/2-50, 10, 100)
opp = py.Rect(110, HEIGHT/2-50, 10, 100)
player_score, opp_score = 0, 0
#Ball
ball = py.Rect(WIDTH/2 - 10, HEIGHT/2 - 10, 20, 20)
x_speed, y_speed = 2, 2

while True:
    pressed = py.key.get_pressed()

    if pressed[py.K_UP]:
        if player.top>0:
            player.top-=2
            player.bottom-=2
    if pressed[py.K_DOWN]:
        if player.bottom<HEIGHT:
            player.top+=2
            player.bottom+=2
    if pressed[py.K_ESCAPE]:
        py.quit()
        sys.exit()
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
    
    if ball.y >= HEIGHT or ball.y <= 0:
        y_speed = y_speed*-1
    if ball.x <= 0:
        player_score+=1
        ball.center = (WIDTH/2, HEIGHT/2)
        x_speed, y_speed = random.choice([2, -2]), random.choice([2, -2])
    if ball.x >= WIDTH:
        opp_score+=1
        ball.center = (WIDTH/2, HEIGHT/2)
        x_speed, y_speed = random.choice([1, -1]), random.choice([2, -2])
    if player.x - ball.width <= ball.x and ball.x <= player.x and ball.y in range(player.top-ball.width, player.bottom+ball.width):
        x_speed = x_speed*-1
    if opp.x - ball.width <= ball.x and ball.x <= opp.x and ball.y in range(opp.top-ball.width, opp.bottom+ball.width):
        x_speed = x_speed*-1

    ball.x += x_speed
    ball.y += y_speed

    player_score_text = FONT.render(str(player_score), True, "white")
    opp_score_text = FONT.render(str(opp_score), True, "white")

    if opp.y<ball.y:
        opp.top+=1
    if opp.bottom>ball.y:
        opp.bottom-=1

    SCREEN.fill("Black")

    py.draw.rect(SCREEN, "white", player)
    py.draw.rect(SCREEN, "white", opp)
    py.draw.circle(SCREEN, "white", ball.center, 10)

    SCREEN.blit(player_score_text, (WIDTH/2 + 50, 50))
    SCREEN.blit(opp_score_text, (WIDTH/2 - 50, 50))

    py.display.update()
    CLOCK.tick(300)