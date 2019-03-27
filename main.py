import nonebot

import config
import database
import webui

global db

if __name__ == '__main__':
    #初始化数据库
    database.init_database()

    webui.start()

    nonebot.init(config)
    #加载命令
    nonebot.load_plugin('commands.list')

    nonebot.run()
