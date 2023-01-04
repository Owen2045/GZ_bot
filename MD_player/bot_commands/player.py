import lightbulb
import hikari


plugin = lightbulb.Plugin('Playtool')

@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_messages(event):
    pass


@plugin.command
@lightbulb.command(name='np', description='現在播放')
@lightbulb.implements(lightbulb.SlashCommand)
async def ex(ctx):
    await ctx.respond('play your mon')











def load(bot):
    bot.add_plugin(plugin)


def unload(bot):
    bot.remove_plugin(plugin)












