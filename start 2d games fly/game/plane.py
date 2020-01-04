import random

import pygame

import constants
from game.bullet import Bullet


class Plane(pygame.sprite.Sprite):
    """
    飞机的基类
    """
    #飞机图片
    plane_images = []
    #飞机爆炸图片
    destroy_images = []
    #坠毁时播放的音乐地址
    down_sound_src = None
    #飞机的状态,true表示活的
    active = True
    #该飞机发射的子弹的精灵组
    bullets = pygame.sprite.Group()

    def __init__(self, screen, speed=None):
        super().__init__()
        self.screen = screen
        #加载静态资源
        self.img_list = []
        self._destroy_img_list = []
        self.down_sound = None
        self.load_src()
        #飞机飞行的速度
        self.speed = speed or 10
        #获取飞机的位置
        self.rect = self.img_list[0].get_rect()
        #飞机的宽高
        self.plane_w, self.plane_h = self.img_list[0].get_size()
        #游戏窗口的宽度和高度
        self.width, self.height = self.screen.get_size()
        #初始化位置
        self.rect.left = int((self.width-self.plane_w) /2)
        self.rect.top = int(self.height /2)

    def load_src(self):
        """加载静态资源"""
        #加载飞机图片
        for img in self.plane_images:
            self.img_list.append(pygame.image.load(img))
        for img in self.destroy_images:
            self._destroy_img_list.append(pygame.image.load(img))
        if self.down_sound_src:
            self.down_sound = pygame.mixer.Sound(self.down_sound_src)

    @property
    def image(self):
        return self.img_list[0]

    def blit_me(self):
        self.screen.blit(self.image, self.rect)
    def move_up(self):
        """飞机向上移动"""
        self.rect.top -= self.speed
    def move_down(self):
        """飞机向下移动"""
        self.rect.top += self.speed
    def move_left(self):
        """飞机向左移动"""
        self.rect.left -= self.speed
    def move_right(self):
        """飞机向右移动"""
        self.rect.right += self.speed
    def broken_down(self):
        """飞机坠毁效果"""
        #播放坠毁音乐
        if self.down_sound:
            self.down_sound.play()#播放一次
            # 播放坠毁动画
        for img in self._destroy_img_list:
            self.screen.blit(img, self.rect)
            # 设置飞机状态
        self.active = False
    def shoot(self):
        """飞机发射子弹"""
        bullet = Bullet(self.screen, self, 15)
        self.bullets.add(bullet)


class OurPlane(Plane):
    """我方飞机"""
    #飞机图片
    plane_images = constants.OUR_PLAN_IMG_LIST
    #飞机爆炸图片
    destory_images = constants.OUR_DESTROY_IMG_LIST
    #坠毁时播放的音乐地址
    down_sound_src = None

    def update(self, war):
        self.move(war.key_down)
        if war.frame % 5:
            self.screen.blit(self.img_list[0], self.rect)
        else:
            self.screen.blit(self.img_list[1], self.rect)
        #碰撞检测
        rest = pygame.sprite.spritecollide(self, war.enemies, False)
        if rest:
            war.status = war.OVER
            war.enemies.empty()
            war.small_enemies.empty()
            self.broken_down()
    def move(self,key):
            if key == pygame.K_w or key == pygame.K_UP:
                self.move_up()
            elif key == pygame.K_s or key == pygame.K_DOWN:
                self.move_down()
            elif key == pygame.K_a or key == pygame.K_LEFT:
                self.move_left()
            elif key == pygame.K_d or key == pygame.K_RIGHT:
                self.move_right()


    def move_up(self):
        super().move_up()
        if self.rect.top <= 0:
            self.rect.top = 0
    def move_down(self):
        super().move_down()
        if self.rect.top >= self.height - self.plane_h:
            self.rect.top = self.height - self.plane_h
    def move_left(self):
        super().move_left()
        if self.rect.left <= 0:
            self.rect.left = 0
    def move_right(self):
        super().move_right()
        if self.rect.left >= self.width - self.plane_w:
            self.rect.left = self.width - self.plane_w

class SmallEnemyPlane(Plane):
    """敌方的小型飞机"""
    #飞机图片
    plane_images =constants.SMALL_ENEMY_PLANE_IMG_LIST
    #飞机爆炸图片
    destory_images = constants.SMALL_ENEMY_DESTROY_LIST
    #坠毁时播放的音乐地址
    down_sound_src = constants.SMALL_ENEMY_PLANE_DOWN_SOUND
    def __init__(self,screen, speed):
        super().__init__(screen, speed)
        self.init_pos()
    def update(self, *args):
        """"更新飞机的移动"""
        super().move_down()
        #画飞机
        self.blit_me()
        #超出范围后的处理
        if self.rect.top >= self.height:
            # self.kill()
            self.active = False
            self.reset()
    def init_pos(self):
        #生成随机位置
        self.rect.left = random.randint(0, self.width - self.plane_w)
        self.rect.top = random.randint(-5*self.plane_h, -self.plane_h)
    def reset(self):
        """重置飞机的状态"""
        self.active = True
        self.init_pos()

    def broken_down(self):
        super().broken_down()
        self.reset()



