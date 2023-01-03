import lightbulb
import hikari


plugin = lightbulb.Plugin('Info')

@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_messages(event):
    print(event.content)

@plugin.command
@lightbulb.command(name='info', description='週末加倍資訊')
@lightbulb.implements(lightbulb.SlashCommand)

async def info(ctx):
    await ctx.respond('顯示週末加倍資訊')











def load(bot):
    bot.add_plugin(plugin)


def unload(bot):
    bot.remove_plugin(plugin)












