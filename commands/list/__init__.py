from nonebot import on_command, CommandSession

import database


@on_command('list', aliases=('列表', '清单'), only_to_me=False)
async def item_list(session: CommandSession):
    l = '【商品列表】'
    for i in database.Item.all():
        l += '\n[{}] {} | ￥{}'.format(i.id, i.name, i.price)

    await session.send(l)
