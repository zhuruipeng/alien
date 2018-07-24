import pygame

import scoreboard
from setting import Settings

from ship import Ship

import game_functions as gf

from pygame.sprite import Group

from alien import Alien

from game_stats import  GameStats

from button import Button

from scoreboard import Scoreboard


def run_game():
    #初始化一个游戏并创建一个屏幕对象
    pygame.init()
    ai_settings =Settings()
    screen =pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("飞船大战")

    #创建play按钮
    play_button = Button(ai_settings,screen,'Play')
    #创建一个用于存储游戏统计信息的实例
    stats =GameStats(ai_settings)


    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    #创建用于存储子弹的编组
    bullets = Group()
    aliens = Group()
    alien=Alien(ai_settings,screen)
    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #创建存储游戏的统计信息实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)



    #开始游戏主循环
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
        else:
            aliens.empty()
            bullets.empty()

            
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()
