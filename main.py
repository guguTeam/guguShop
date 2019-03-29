import nonebot

import config
import database
import webui

global db

if __name__ == '__main__':
    #初始化数据库
    database.init_database()
    #初始化WebUI
    webui.start()
    #读取nonebot配置
    nonebot.init(config)
    #加载命令
    nonebot.load_plugin('commands.user.shop')
    #nonebot 冲鸭
    nonebot.run()
