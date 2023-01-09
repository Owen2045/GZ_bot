import random
import miru
import hikari
import typing as t
import asyncio
import datetime


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

# 成功反應
REACTION_SUCCESS = '🆗'

# 失敗反應
REACTION_FAILURE = '🆖'

# 向前反應
REACTION_FORWARD = '➡'

# 向後反應
REACTION_BACKWARD = '⬅'

REACTION_TABA = '🎉'

class BasicView(miru.View):
    def __init__(self, *, timeout: t.Optional[t.Union[float, int, datetime.timedelta]] = 120.0, autodefer: bool = True, select_list: list = []) -> None:
        super().__init__(timeout=timeout, select_list=select_list)
    global select_list
        # self._autodefer: bool = autodefer
        # self._message: t.Optional[hikari.Message] = None
        # self._message_id: t.Optional[int] = None  # Only for bound persistent views
        # self._input_event: asyncio.Event = asyncio.Event()

    # Define a new Select menu with two options
    a = [miru.SelectOption(label="Option 1"), miru.SelectOption(label="Option 2")]
    
    @miru.select(
        placeholder="Select me!",
        options= [] # self.options_list
    )
    async def basic_select(self, select: miru.Select, ctx: miru.ViewContext) -> None:
        await ctx.respond(f"You've chosen {select.values[0]}!")

    # Define a new Button with the Style of success (Green)
    @miru.button(label="Click me!", style=hikari.ButtonStyle.SUCCESS)
    async def basic_button(self, button: miru.Button, ctx: miru.ViewContext) -> None:
        await ctx.respond("You clicked me!")

    # Define a new Button that when pressed will stop the view & invalidate all the buttons in this view
    @miru.button(label="Stop me!", style=hikari.ButtonStyle.DANGER)
    async def stop_button(self, button: miru.Button, ctx: miru.ViewContext) -> None:
        self.stop()



# class BasicView(miru.View):

#     # Define a new Select menu with two options
#     @miru.select(
#         placeholder="Select me!",
#         options=[
#             miru.SelectOption(label="Option 1"),
#             miru.SelectOption(label="Option 2"),
#         ],
#     )
#     async def basic_select(self, select: miru.Select, ctx: miru.ViewContext) -> None:
#         await ctx.respond(f"You've chosen {select.values[0]}!")

#     # Define a new Button with the Style of success (Green)
#     @miru.button(label="Click me!", style=hikari.ButtonStyle.SUCCESS)
#     async def basic_button(self, button: miru.Button, ctx: miru.ViewContext) -> None:
#         await ctx.respond("You clicked me!")

#     # Define a new Button that when pressed will stop the view & invalidate all the buttons in this view
#     @miru.button(label="Stop me!", style=hikari.ButtonStyle.DANGER)
#     async def stop_button(self, button: miru.Button, ctx: miru.ViewContext) -> None:
#         self.stop()


