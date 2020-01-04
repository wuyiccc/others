import pygame, sys

pygame.init()
screen = pygame.display.set_mode((500, 500))


red = pygame.Color(255, 0, 0)
#字体，从系统中获取字体，必须是存在的
# font = pygame.font.SysFont('华文新魏', 40, False, False)# 是否粗体,斜体
#从字体文件中加载字体
font=pygame.font.Font('./STXINWEI.TTF',40)
#文字对象渲染
text = font.render('得分', True, red)


#加载音乐
bg_music = pygame.mixer.music.load("neverM.mp3")
pygame.mixer.music.set_volume(0.2)#0~1，值越小音量越小
pygame.mixer.music.play(-1)#-1,循环播放背景音乐
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #设置字体位置
    screen.blit(text, (20, 20))
    #更新
    pygame.display.flip()