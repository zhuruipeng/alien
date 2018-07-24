class GameStats():
    """跟踪个游戏统计信息"""
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        #游戏刚启动处于活跃状态
        self.game_active =False
        #任何情况都不重置最高得分
        self.high_score =0
    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left =self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
    def check_high_score(stats,sb):
        """检查是否诞生最高分"""
        if stats.score > stats.high_score:
            stats.high_score =stats.score
            sb.prep_high_score()