from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# ReplyKeyboardMarkup uchun
ramazon_oy = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('1 🌙Oylik✨ korish👀'),
        ]
    ],
    resize_keyboard=True
)


# kunlik_korish = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton('Bugungi T')
#         ]
#     ]
# )

# InlineKeyboardMarkup uchun
def get_kunlar_markup():
    kunlar = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='1-kun', callback_data="1_kun"),
                InlineKeyboardButton(text='2-kun', callback_data="2_kun"),
                InlineKeyboardButton(text='3-kun', callback_data="3_kun")
            ]
        ]
    )
    return kunlar
