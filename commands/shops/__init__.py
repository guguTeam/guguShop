from nonebot import on_command, CommandSession

import database


@on_command('shops', aliases=('店铺', '商店', '超市'), only_to_me=False)
async def item_list(session: CommandSession):
    l = '【超市列表】'
    for i in database.Item.all():
        l += '\n[{}] {} | 库存: {} | ￥{}'.format(i.id, i.name, i.count if (i.count > 0) else '缺货', i.price)

    await session.send(l)
