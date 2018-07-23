class Settings():
    """存储外星人入侵的所有设置的类"""

    def __init__(self):
        self.screen_width =1200
        self.screen_height =800
        self.bg_color =(230,230,230)
        self.ship_speed_factor =5
        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed =10
        #fleet_direction 为1 表示向右移动，-1像左移动
        self.fleet_direction =1


        #子弹设置
        self.bullet_speed_factor = 5
        self.bullet_width =300
        self.bullet_height =15
        self.bullet_color = 60,60,60
        self.bullets_allowed =5

        
