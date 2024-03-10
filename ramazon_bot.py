import logging

from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_TOKEN = "7100416499:AAGxHuAvbIceC8YmlQTMx3tRQd2y-uu5Kcw"
bot = Bot(token=API_TOKEN, parse_mode='HTML')
logging.basicConfig(level=logging.INFO)
dp = Dispatcher(bot, storage=MemoryStorage())

from keybord_ramazon.defa import ramazon_oy
from keybord_ramazon.irline import *


# from keybord_ramazon.irline import kunlik_3
# from keybord_ramazon.irline import kunlik_4
# from keybord_ramazon.irline import kunlik_5
# from keybord_ramazon.irline import kunlik_6
# from keybord_ramazon.irline import kunlik_7
# from keybord_ramazon.irline import kunlik_8
# from keybord_ramazon.irline import kunlik_9
# from keybord_ramazon.irline import kunlik_10
# from keybord_ramazon.irline import kunlik_11
# from keybord_ramazon.irline import kunlik_12
# from keybord_ramazon.irline import kunlik_13
# from keybord_ramazon.irline import kunlik_14
# from keybord_ramazon.irline import kunlik_15
# from keybord_ramazon.irline import kunlik_16
# from keybord_ramazon.irline import kunlik_17
# from keybord_ramazon.irline import kunlik_18
# from keybord_ramazon.irline import kunlik_19
# from keybord_ramazon.irline import kunlik_20
# from keybord_ramazon.irline import kunlik_21
# from keybord_ramazon.irline import kunlik_22
# from keybord_ramazon.irline import kunlik_23
# from keybord_ramazon.irline import kunlik_24
# from keybord_ramazon.irline import kunlik_25
# from keybord_ramazon.irline import kunlik_26
# from keybord_ramazon.irline import kunlik_27
# from keybord_ramazon.irline import kunlik_28
# from keybord_ramazon.irline import kunlik_29
# from keybord_ramazon.irline import kunlik_30


@dp.message_handler(commands="start")
async def starter(message: types.Message):
    with open('rasm_ramazon/img.png', 'rb') as photo:
        await message.answer_photo(photo, caption='🌙✨Assalomu aleykum va rahmatullahi barakatuh🕋🤲🏼',
                                   reply_markup=ramazon_oy)


@dp.message_handler(lambda message: message.text == '1 🌙Oylik✨ korish👀')
async def send_oy(message: types.Message):
    kunlar_markup = kunlar
    with open('rasm_ramazon/img_3.png', 'rb') as photo:
        await message.answer_photo(photo, reply_markup=kunlar_markup)


@dp.callback_query_handler(lambda c: c.data == '1_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '1_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆11.03.2024     ✨Dushanba
                <b>⏰05:23⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '1_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆11.03.2024     ✨Dushanba
                <b>⏰18:27⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '2_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_2, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '2_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆12.03.2024     ✨Seshanba
                <b>⏰05:21⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '2_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆12.03.2024     ✨Seshanba
                <b>⏰18:28⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '3_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_3, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '3_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆13.03.2024     ✨Chorshanba
                <b>⏰05:20⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '3_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆13.03.2024     ✨Chorshanba
                <b>⏰18:29⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '4_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_4, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '4_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆14.03.2024     ✨Payshanba
                <b>⏰05:18⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '4_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆14.03.2024     ✨Payshanba
                <b>⏰18:31⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '5_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_5, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '5_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆15.03.2024     🕋<b>Juma</b>
                <b>⏰05:16⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '5_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆15.03.2024     🕋<b>Juma</b>
                <b>⏰18:32⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '6_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_6, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '6_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆16.03.2024     ✨Shanba
                <b>⏰05:14⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '6_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆16.03.2024     ✨Shanba
                <b>⏰18:33⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '7_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_7, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '7_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆17.03.2024     ✨Yakshanba
                <b>⏰05:13⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '7_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆17.03.2024     ✨Yakshanba
                <b>⏰18:34⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '8_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_8, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '8_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆18.03.2024     ✨Dushanba
                <b>⏰05:11⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '8_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆18.03.2024     ✨Dushanba
                <b>⏰18:35⏳</b>""")

        @dp.callback_query_handler(lambda c: c.data == '9_kun')
        async def process_callback(callback_query):
            await callback_query.answer()
            with open('rasm_ramazon/img_1.png', 'rb') as photo:
                await callback_query.message.answer_photo(photo, reply_markup=kunlik_9,
                                                          caption="⏰Qaysi vaxitni tanlaysiz✅")

        @dp.callback_query_handler(lambda c: c.data == '9_1_kun')
        async def process_callback1(callback_query):
            await callback_query.answer()
            with open('rasm_ramazon/img_4.png', 'rb') as photo:
                await callback_query.message.answer_photo(photo, caption="""📆19.03.2024     ✨Seshanba
                <b>⏰05:09⏳</b>""")

        @dp.callback_query_handler(lambda c: c.data == '9_2_kun')
        async def process_callback1(callback_query):
            await callback_query.answer()
            with open('rasm_ramazon/img_5.png', 'rb') as photo:
                await callback_query.message.answer_photo(photo, caption="""📆19.03.2024     ✨Seshanba
                <b>⏰18:36⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '10_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_10, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '10_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆20.03.2024     ✨Chorshanba
                <b>⏰05:07⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '10_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆20.03.2024     ✨Chorshanba
                <b>⏰18:37⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '11_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_11, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '11_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆21.03.2024     ✨Payshanba
                <b>⏰05:05⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '11_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆21.03.2024     ✨Payshanba
                <b>⏰18:39⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '12_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_12, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '12_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆22.03.2024     🕋<b>Juma</b>
                <b>⏰05:04⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '12_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆22.03.2024     🕋<b>Juma</b>
                <b>⏰18:39⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '13_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_13, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '13_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆23.03.2024     ✨Shanba
                <b>⏰05:04⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '13_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆23.03.2024     ✨Shanba
                <b>⏰18:40⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '14_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_14, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '14_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆24.03.2024     ✨Yakshanba
                <b>⏰05:00⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '14_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆24.03.2024     ✨Yakshanba
                <b>⏰18:42⏳</b>""")

    @dp.callback_query_handler(lambda c: c.data == '15_kun')
    async def process_callback(callback_query):
        await callback_query.answer()
        with open('rasm_ramazon/img_1.png', 'rb') as photo:
            await callback_query.message.answer_photo(photo, reply_markup=kunlik_15,
                                                      caption="⏰Qaysi vaxitni tanlaysiz✅")

    @dp.callback_query_handler(lambda c: c.data == '15_1_kun')
    async def process_callback1(callback_query):
        await callback_query.answer()
        with open('rasm_ramazon/img_4.png', 'rb') as photo:
            await callback_query.message.answer_photo(photo, caption="""📆25.03.2024     ✨Dushanba
                <b>⏰04:58⏳</b>""")

    @dp.callback_query_handler(lambda c: c.data == '15_2_kun')
    async def process_callback1(callback_query):
        await callback_query.answer()
        with open('rasm_ramazon/img_5.png', 'rb') as photo:
            await callback_query.message.answer_photo(photo, caption="""📆25.03.2024     ✨Dushanba
                <b>⏰18:43⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '16_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_16, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '16_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆26.03.2024     ✨Seshanba
                <b>⏰04:57⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '16_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆26.03.2024     ✨Seshanba
                <b>⏰18:44⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '17_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_17, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '17_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆27.03.2024     ✨Chorshanba
                <b>⏰04:55⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '17_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆27.03.2024     ✨Chorshanba
                <b>⏰18:45⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '18_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_18, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '18_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆28.03.2024     ✨Payshanba
                <b>⏰04:55⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '18_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆28.03.2024     ✨Payshanba
                <b>⏰18:46⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '19_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_19, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '19_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆29.03.2024     🕋<b>Juma</b>
                <b>⏰04:51⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '19_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆29.03.2024     🕋<b>Juma</b>
                <b>⏰18:47⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '20_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_20, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '20_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆30.03.2024     ✨Shanba
                <b>⏰04:49⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '20_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆30.03.2024     ✨Shanba
                <b>⏰18:48⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '21_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_21, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '21_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆31.03.2024     ✨Yakhanba
                <b>⏰04:48⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '21_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆31.03.2024     ✨Yakhanba
                <b>⏰18:49⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '22_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_22, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '22_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆01.04.2024     ✨Dushanba
                <b>⏰04:46⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '22_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆01.04.2024     ✨Dushanba
                <b>⏰18:50⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '23_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_23, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '23_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆02.04.2024     ✨Seshanba
                <b>⏰04:44⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '23_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆02.04.2024     ✨Seshanba
                <b>⏰18:51⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '24_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_24, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '24_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆03.04.2024     ✨Chorshanba
                <b>⏰04:42⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '24_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆03.04.2024     ✨Chorshanba
                <b>⏰18:52⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '25_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_25, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '25_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆04.04.2024     ✨Payshanba
                <b>⏰04:40⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '25_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆04.04.2024     ✨Payshanba
                <b>⏰18:53⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '26_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_26, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '26_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆05.04.2024     🕋<b>Juma</b>
                <b>⏰04:38⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '26_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆05.04.2024     🕋<b>Juma</b>
                <b>⏰18:54⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '27_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_27, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '27_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆06.04.2024     ✨Shanba
                <b>⏰04:36⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '27_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆06.04.2024     ✨Shanba
                <b>⏰18:56⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '28_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_28, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '28_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆07.04.2024     ✨Yakshanba
                <b>⏰04:34⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '28_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆07.04.2024     ✨Yakshanba
                <b>⏰18:57⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '29_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_29, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '29_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆08.04.2024     ✨Dushanba
                <b>⏰04:32⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '29_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆08.04.2024     ✨Dushanba
                <b>⏰18:58⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '30_kun')
async def process_callback(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_1.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, reply_markup=kunlik_30, caption="⏰Qaysi vaxitni tanlaysiz✅")


@dp.callback_query_handler(lambda c: c.data == '30_1_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_4.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆09.04.2024     ✨Seshanba
                <b>⏰04:31⏳</b>""")


@dp.callback_query_handler(lambda c: c.data == '30_2_kun')
async def process_callback1(callback_query):
    await callback_query.answer()
    with open('rasm_ramazon/img_5.png', 'rb') as photo:
        await callback_query.message.answer_photo(photo, caption="""📆09.04.2024     ✨Seshanba
                <b>⏰18:59⏳</b>""")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
