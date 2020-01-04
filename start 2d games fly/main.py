import pygame, sys
from game.war import PlaneWar
import constants
from game.plane import OurPlane, SmallEnemyPlane


def main():
    """游戏入口"""
    war = PlaneWar()
    #添加敌方飞机
    war.add_small_enemies(6)
    war.run_game()








if __name__ == '__main__':
    main()