import  sys, pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

ball = pygame.image.load("intro_ball.gif")
red = pygame.Color(255, 0, 0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #画线
    pygame.draw.line(screen, red, (10, 10), (200, 200),  10)
    #画矩形 pygame.draw.rect(screen,red,(10,20,200,300),10)#坐标加长宽
    #画圆 pygame.draw.circle(screen,red,(100,100),50,5)
    #图片的绘制
    screen.blit(ball, (100, 100))
    pygame.display.flip()