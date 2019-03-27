import nonebot

import config
import database

global db

if __name__ == '__main__':
    #初始化数据库
    database.init_database()

    nonebot.init(config)
    #加载list命令
    nonebot.load_plugin('commands.list')
    nonebot.run()
