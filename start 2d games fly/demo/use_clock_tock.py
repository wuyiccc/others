import pygame, sys

pygame.init()

screen = pygame.display.set_mode((500, 500))
image = pygame.image.load('hero1.png')
image2 = pygame.image.load('hero2.png')

clock = pygame.time.Clock()
counter = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #利用帧速率进行图片切换控制，一秒钟60帧
    clock.tick(60)

    #屏幕绘制白色背景
    screen.fill(pygame.Color(255, 255, 255))
    if counter % 5 == 0:
        screen.blit(image, (20, 20))
    #绘制图片
    else:
        screen.blit(image2, (20, 20))
    pygame.display.flip()
    counter+=1