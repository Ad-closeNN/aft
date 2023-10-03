import json
import time
from mcdreforged.api.all import *
import os
import re
from typing import List, Dict
from math import ceil, floor
from typing import Optional, Any
from mcdreforged.api.types import PluginServerInterface, PlayerCommandSource
from mcdreforged.api.command import *
from mcdreforged.api.decorator import new_thread
from mcdreforged.api.utils import Serializable
import time

def on_load(server,parameter):    
    server.register_help_message('!Clear', '注册 §aGM §r插件')
    server.register_help_message('!c', '切换至§6旁观模式')
    server.register_help_message('!s', '切换回§6生存模式，并§c返回§r原来的地方')
    server.register_help_message('!gm help', '查看 §aGM §r插件的帮助信息')
    server.register_help_message('!gm del @s', '删除你在 §aGM §r插件中的信息(§c有确认§6，还要确认一遍)')
    server.register_help_message('!gm del @s confirm', '删除你在 §aGM §r插件中的信息(§c无确认§6，直接执行删除命令)')
    server.register_help_message('?ads', '查看 §aAd_Dev_Server §r插件的信息')
    server.register_help_message('?ads help', '查看 §aAd_Dev_Server §r插件的§6帮助§r信息')
    server.register_help_message('!!c', '切换成创造模式，且§c作弊榜§r会加 1')
    server.register_help_message('!!s', '切换成生存模式，§c作弊榜§a不会§r改变')
    server.register_help_message( '!!reloadall', '重新加载 §aMCDR §r的全部插件')
    server.logger.info('[§6ads§r]已重新加载插件')

def on_user_info(server, info):
    if info.content == '!Clear':
        server.reply(info, '§a你已成功注册 GM 插件！')
        server.reply(info, '§a你现在可以正常使用 !c 和 !s 指令了！')
        server.reply(info, '§a使用 §6!gm help §a可以查看 GM 插件的帮助信息！')
    if info.content == '!gm help':
        server.reply(info, '§a------------------ GM 插件指令帮助 --------------------')
        server.reply(info, '§6使用 §a!gm help §6命令可以显示这条插件指令帮助信息')
        server.reply(info, '§6使用 §a!Clear §6命令可以使你注册 §aGM §6插件')
        server.reply(info, '§6使用 §a!c §6命令可以使你进入旁观者模式')
        server.reply(info, '§6使用 §a!s §6命令可以使你返回生存模式，并回到你使用 §a!c §6的位置')
        server.reply(info, '§6使用 §a!gm del @s §6命令可以使你删除你在 §aGM §6插件的信息(§c有确认§6，还要确认一遍)')
        server.reply(info, '§6使用 §a!gm del @s confirm §6命令可以使你删除你在 §aGM §6插件的信息(§c无确认§6，直接执行删除命令)')
        server.reply(info, '§a------------------ GM 插件指令帮助 --------------------')
    if info.content == '!!yb':
        server.execute('give Supreme bedrock 1')        
        server.execute('tellraw @a [{"text":"Supreme","color":"gold"},{"text":"达成了目标","color":"white"},{"text":"[这太","color":"red","bold":true},{"text":"TM","color":"red","bold":"false"},{"text":"原版了]","color":"red","bold":"true"}]')
        server.execute('tellraw @a [{"text":"<"},{"text":"Supreme","color":"gold"},{"text":"> ","color":"white"},{"text":"Supreme，至高无上！","color":"white"}]')
    if info.content == 'byd':  
        server.execute('title @a title [{"text":"BYD！","color":"red"},{"selector":"@s"},{"text":"Fuck You！","color":"red"}]')
    if info.content == '原神':
        server.reply(info, '§c启动！')
    if info.content == 'ys':
        server.reply(info, '§c启动！')
    if info.content == 'YS':
        server.reply(info, '§c启动！')
    if info.content == 'gi':
        server.reply(info, '§c启动！')
    if info.content == 'Gi':
        server.reply(info, '§c启动！')
    if info.content == 'gI':
        server.reply(info, '§c启动！')
    if info.content == 'genshin impact':
        server.reply(info, '§c启动！')
    if info.content == 'Genshin Impact':
        server.reply(info, '§c启动！')
    if info.content == '!!s':
        server.execute("gamemode survival " +(info.player))
    if info.content == '!!c':
        server.execute("gamemode creative " +(info.player))
        server.execute("scoreboard players add " +(info.player) +" zb 1")
    if info.content == '!gm del @s':
        server.reply(info, '§6注意！\n你正在使用 §a!gm del @s §6命令！这个命令将会删除你在 §aGM §6插件的信息。如果删除，你在使用 §a!c §6前的位置将会丢失。这意味着你在使用§a!c §6命令时删除了你在 §aGM §6插件的信息，§a!s§6 将无法回到原来的位置，必须通过 §a!Clear §6切回生存模式。请谨慎操作。')
        server.reply(info, '§6如果你已知此操作的风险，并且已经在生存模式下，那么可以使用 §a!gm del @s confirm §6命令来删除你在 §aGM §6插件的信息')
    if info.content == '!gm del @s confirm':
        file_path = r"./plugins/gm/"+ (info.player)
        file_path_two = r"./plugins/gm/"+ (info.player) + '.dat'	
        if os.path.isfile(file_path):
            os.remove (file_path)
            server.logger.info('§6已删除玩家' + (info.player) + '在 §aGM §6插件中的信息')
            server.reply(info, '§6已删除你在 §aGM §6插件中的信息。')
            server.reply(info, '§6如需重新生成信息，请使用 §a!Clear §6命令注册 §aGM §6插件。')
        else :
            server.reply(info, '§6你在 §aGM §6插件中的信息已经被删除过了，无需再次删除。')
            server.logger.info('§c玩家' + (info.player) + '在 §aGM §c插件中的信息已经被删除过了')
        if os.path.isfile(file_path_two):    
            os.remove (file_path_two)
            server.logger.info('§6已删除玩家' + (info.player) + '在 §aGM §6插件中的".dat"信息')
        else :
            server.logger.info('§c玩家' + (info.player) + '在 §aGM §c插件中的".dat"信息已经被删除过了')
    
    if info.content == '?ads':
        server.reply(info, '§6-------------Ad_Dev_Server 插件信息-------------')
        server.reply(info, '插件名称: §aAd_Dev_Server')
        server.reply(info, '插件ID: §aads')
        server.reply(info, '插件版本: §aVer 1.0.1')
        server.reply(info, '运行状态: §a运行中')
        server.reply(info, '§5——只是个 GM 插件的小附属和自己加来玩玩的插件罢了')
        server.reply(info, '    §aCopyright © 2023 Ad_closeNN, All rights reserved')
        server.reply(info, '§6------------- Ad_Dev_Server 插件信息 -------------')
    if info.content == '?ads help':
        server.reply(info, '§6------------ Ad_Dev_Server 插件帮助信息 ------------')
        server.reply(info, '§6使用 §a?ads help §6命令可以显示这条插件帮助信息')
        server.reply(info, '§6使用 §a?ads §6命令可以查看 §aAd_Dev_Server §6插件的信息')
        server.reply(info, '§6使用 §a?ads line114 §6命令可以查看第114行代码的现状')
        server.reply(info, '§6使用 §a?ads reload§6命令可以重新加载 §aAd_Dev_Server §6插件')
        server.reply(info, '§6发送 §abyd §6可以生成一个标题')
        server.reply(info, '§6发送 §ays §6可以启动')
        server.reply(info, '§6使用 §a!gm help §6命令可以查看 §aGM §6插件的帮助信息')
        server.reply(info, '§6使用 §a!!yb §6命令可以让 §6Supreme 达成目标')
        server.reply(info, '§6使用 §a!!c §6命令可以切换成创造模式，且§c作弊榜§6会加 1')
        server.reply(info, '§6使用 §a!!s §6命令可以切换成生存模式，§c作弊榜§a不会§6改变')
        server.reply(info, '§6使用 §a!!reloadall §6命令可以重新加载 §aMCDR §6的全部插件')
        server.reply(info, '§6------------ Ad_Dev_Server 插件帮助信息 ------------')
    if info.content == '?ads line114':
        server.reply(info, '§a这里是插件代码中的第§6114§a行，好臭啊(恼)')
        server.reply(info, '§a你要是不信，就自己解包看看(恼)')
 #   if info.content == '?ads reload':
 #       server.say('§6插件重载已由' + (info.player) + '触发')
   #     server.say('§5正在重载插件')
   #     server.say('§aAd_Dev_Server §6插件已重新加载')

from mcdreforged.api.command import *
from mcdreforged.api.types import PluginServerInterface


def on_load(server: PluginServerInterface, prev_module):
    server.register_command(
        Literal('!!reloadall')
        .runs(handler)
        .then(
            GreedyText('content')
            .runs(handler)
        )
    )
    
def handler(src, ctx):
    src.get_server().execute_command(f'!!MCDR plugin reloadall {ctx.get("content", "")}', src)

