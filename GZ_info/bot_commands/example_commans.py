import lightbulb
import hikari


plugin = lightbulb.Plugin('Example')

@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_messages(event):
    print(event.content)


@plugin.command
@lightbulb.command(name='ex', description='一個範例')
@lightbulb.implements(lightbulb.SlashCommand)
async def ex(ctx):
    await ctx.respond('恭喜成功執行範例')











def load(bot):
    bot.add_plugin(plugin)














