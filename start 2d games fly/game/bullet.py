import pygame
import constants


class Bullet(pygame.sprite.Sprite):
    """子弹类"""

    #子弹状态
    active = True

    def __init__(self, screen, plane, speed=None):
        super().__init__()
        #速度
        self.speed = speed or 10
        self.plane = plane
        self.image = pygame.image.load(constants.BULLET_IMG)
        self.rect = self.image.get_rect()
        self.rect.centerx = plane.rect.centerx
        self.rect.top = plane.rect.top
        self.screen = screen

        #发射的音乐效果
        self.shoot_sound = pygame.mixer.Sound(constants.BULLET_SHOOT_SOUND)
        self.shoot_sound.set_volume(0.3)
        self.shoot_sound.play()
    def update(self, war):
        """更新子弹的位置"""
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.remove(self.plane.bullets)
        self.screen.blit(self.image, self.rect)
        #碰撞检测,检测子弹是否碰撞到敌机
        rest = pygame.sprite.spritecollide(self, war.enemies, False)
        print(rest, 666)
        for r in rest:
            self.kill()
            r.broken_down()
            war.rest.score += constants.SCORE_SHOOT_SMALL
            war.rest.set_history()



