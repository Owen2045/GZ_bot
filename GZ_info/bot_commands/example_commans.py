import lightbulb
import hikari


plugin = lightbulb.Plugin('Example')

@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_messages(event):
    pass


@plugin.command
@lightbulb.command(name='ex', description='一個範例')
@lightbulb.implements(lightbulb.SlashCommand)
async def ex(ctx):
    await ctx.respond('text1dd')











def load(bot):
    bot.add_plugin(plugin)


def unload(bot):
    bot.remove_plugin(plugin)












