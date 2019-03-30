from nonebot import on_command, CommandSession
from nonebot.command.argfilter import extractors

import database


@on_command('shop', aliases=('店铺', '商店', '超市'), only_to_me=False)
async def item_list(session: CommandSession):
    l = '【超市列表】'
    for i in database.Item.all():
        l += '\n[{}] {} | 库存: {} | ￥{}'.format(i.id, i.name, i.count if (i.count > 0) else '缺货', i.price)

    await session.send(l)
    #session.get('info', prompt='请输入‘购买 [序号] [数量] [宿舍号] [备注(可为空)]’提交购买订单~'）


@item_list.args_parser
async def _(session: CommandSession):
    pass
