import nonebot

import config
import database

global db

if __name__ == '__main__':
    database.init_database()
    nonebot.init(config)
    nonebot.load_plugin('commands.list')
    nonebot.run()
