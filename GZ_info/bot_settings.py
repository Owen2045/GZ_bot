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
    # def __init__(self, *args, **kwargs) -> None:
    #     super().__init__(*args, **kwargs)

    # def __init__(self) -> None:
    #     super().__init__(timeout=None)

    # 建立基本的view
    async def basic_select(self, select: miru.Select, ctx: miru.ViewContext) -> None:
        await ctx.respond(f"你選了 {select.values[0]}!")

    @miru.button(label="確認", style=hikari.ButtonStyle.SUCCESS)
    async def basic_button(self, button: miru.Button, ctx: miru.ViewContext) -> None:
        await ctx.respond("按確認")

    @miru.button(label="停止查詢", style=hikari.ButtonStyle.DANGER)
    async def stop_button(self, button: miru.Button, ctx: miru.ViewContext) -> None:
        await ctx.respond("結束查詢")
        self.stop()

    # 自定義輸入
    @miru.button(label="Click me!", style=hikari.ButtonStyle.PRIMARY)
    async def modal_button(self, button: miru.Button, ctx: miru.ViewContext) -> None:
        modal = BasicModal(title="Example Title")
        # You may also use Modal.send(interaction) if not working with a miru context object. (e.g. slash commands)
        # Keep in mind that modals can only be sent in response to interactions.
        await ctx.respond_with_modal(modal)
        

# 自定義按鈕
class YesButton(miru.Button):
    def __init__(self) -> None:
        super().__init__(style=hikari.ButtonStyle.SUCCESS, label="選擇")

    async def callback(self, ctx: miru.ViewContext) -> None:
        await ctx.respond("賓狗 答對了", flags=hikari.MessageFlag.EPHEMERAL)
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
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
    async def callback(self, ctx: miru.ViewContext) -> None:
        select_value = ctx.interaction.values[0]
        await ctx.respond(f"按 ： {select_value}", flags=hikari.MessageFlag.EPHEMERAL)
        # self.view.answer = True
        # self.view.stop()
