import random
import miru
import hikari
import typing as t
import asyncio
import datetime
import lightbulb


def choose_colour():
    return random.choice(
        (
            0x1ABC9C,
            0x11806A,
            0x2ECC71,
            0x1F8B4C,
            0x3498DB,
            0x206694,
            0x9B59B6,
            0x71368A,
            0xE91E63,
            0xAD1457,
            0xF1C40F,
            0xC27C0E,
            0xE67E22,
            0xA84300,
            0xE74C3C,
            0x992D22,
        )
    )

# æååæ
REACTION_SUCCESS = 'ð'

# å¤±æåæ
REACTION_FAILURE = 'ð'

# åååæ
REACTION_FORWARD = 'â¡'

# åå¾åæ
REACTION_BACKWARD = 'â¬'

REACTION_TABA = 'ð'

class BasicModal(miru.Modal):
    # Define our modal items
    # You can also use Modal.add_item() to add items to the modal after instantiation, just like with views.
    name = miru.TextInput(label="Name", placeholder="Enter your name!", required=True)
    bio = miru.TextInput(label="Biography", value="Pre-filled content!", style=hikari.TextInputStyle.PARAGRAPH)

    # The callback function is called after the user hits 'Submit'
    async def callback(self, ctx: miru.ModalContext) -> None:
        # You can also access the values using ctx.values, Modal.values, or use ctx.get_value_by_id()
        await ctx.respond(f"Your name: `{self.name.value}`\nYour bio: ```{self.bio.value}```")


class BasicView(miru.View):
    # å»ºç«åºæ¬çview
    async def basic_select(self, select: miru.Select, ctx: miru.ViewContext) -> None:
        await ctx.respond(f"ä½ é¸äº {select.values[0]}!")

    @miru.button(label="ç¢ºèª", style=hikari.ButtonStyle.SUCCESS)
    async def basic_button(self, button: miru.Button, ctx: miru.ViewContext) -> None:
        await ctx.respond("æç¢ºèª")

    @miru.button(label="åæ­¢æ¥è©¢", style=hikari.ButtonStyle.DANGER)
    async def stop_button(self, button: miru.Button, ctx: miru.ViewContext) -> None:
        await ctx.respond("çµææ¥è©¢")
        self.stop()

    # èªå®ç¾©è¼¸å¥
    @miru.button(label="Click me!", style=hikari.ButtonStyle.PRIMARY)
    async def modal_button(self, button: miru.Button, ctx: miru.ViewContext) -> None:
        modal = BasicModal(title="Example Title")
        # You may also use Modal.send(interaction) if not working with a miru context object. (e.g. slash commands)
        # Keep in mind that modals can only be sent in response to interactions.
        await ctx.respond_with_modal(modal)
        

# èªå®ç¾©æé
class YesButton(miru.Button):
    def __init__(self) -> None:
        super().__init__(style=hikari.ButtonStyle.SUCCESS, label="é¸æ")

    async def callback(self, ctx: miru.ViewContext) -> None:
        await ctx.respond("è³ç ç­å°äº", flags=hikari.MessageFlag.EPHEMERAL)
        self.view.answer = True
        # self.view.stop()

class ExitButton(miru.Button):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    async def callback(self, ctx: miru.ViewContext) -> None:
        await ctx.respond("bye bitch", flags=hikari.MessageFlag.EPHEMERAL)
        self.view.answer = False
        self.view.stop()

class SelectMenu(miru.Select):
    def __init__(self, df, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.df = df

    async def callback(self, ctx: miru.ViewContext) -> None:
        select_value = ctx.interaction.values[0]
        df_date = self.df[self.df['info_time_str']==select_value]
        df_dict = df_date.to_dict('records')
        if len(df_dict) > 0:
            df_dict = df_dict[0]
            select_time = df_dict.get('info_time_str')
            url = df_dict.get('url')
            en = df_dict.get('update_info_en')
            zh = df_dict.get('update_info_zh')
            await ctx.respond(f"{zh} \n\nåç¶²å: {url}", flags=hikari.MessageFlag.EPHEMERAL)
        else:
            await ctx.respond(f"{select_value}: æ¥ç¡æ´æ°è³è¨", flags=hikari.MessageFlag.EPHEMERAL)

class CustomHelp(lightbulb.BaseHelpCommand):
    async def send_bot_help(self, context):
        embed = (
            hikari.Embed(
                title="command helper", 
                description="""å¦ è¦ä¾äºå""",
                colour=choose_colour(),
            )
            .set_author(
                name=f"{context.author.username} ching chong!",
                icon=context.author.avatar_url or context.author.default_avatar_url,
            )
            .set_thumbnail(
                context.bot.get_me().avatar_url or context.bot.get_me().default_avatar_url
            )
            # å ä¸åå°±ä¸è¡
            .add_field("Staff commands", "/kick\n/ban\n/unban\n/timeout\n/snipe", inline=True)
        )
        embed.set_footer("æåºäº èå¥")

        await context.respond(embed)

    async def send_plugin_help(self, context, plugin):
        await context.respond(';(')
        pass
        # Override this method to change the message sent when the help command
        # è¼¸å¥çºpluginåç¨±
        ...

    async def send_command_help(self, context, command):
        await context.respond(':O')
        pass
        # Override this method to change the message sent when the help command
        # è¼¸å¥çº/æä»¤
        ...

    async def send_group_help(self, context, group):
        pass
        # Override this method to change the message sent when the help command
        # è¼¸å¥çºç¾¤çµæä»¤
        ...

    async def object_not_found(self, context, obj):
        pass
        # Override this method to change the message sent when help is
        # requested for an object that does not exist