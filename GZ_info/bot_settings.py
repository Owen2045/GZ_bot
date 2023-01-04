import random


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
