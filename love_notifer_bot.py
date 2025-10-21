import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# 🔹 Укажи токен, выданный BotFather
API_TOKEN = "API_TOKEN_BOT"

# 🔹 ID того, кто будет активировать бота (можно несколько)
ALLOWED_USER_IDS = [0000000000]

# 🔹 Твой Telegram ID
ALERT_USER_ID = 0000000000

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

alert_task = None
alert_running = False

# 🎬 /start — проверка, тот ли человек
@dp.message(CommandStart())
async def start_handler(message: types.Message):
    if message.from_user.id in ALLOWED_USER_IDS:
        kb = ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="Оставить обращение")]],
            resize_keyboard=True
        )
        await message.answer("Привет! Нажми кнопку ниже 👇", reply_markup=kb)
    else:
        await message.answer("Этот бот не для тебя, кышь отсюда ❌")

# 📬 Нажата кнопка “Оставить обращение”
@dp.message(lambda msg: msg.text == "Оставить обращение")
async def handle_request(message: types.Message):
    global alert_task, alert_running
    if message.from_user.id in ALLOWED_USER_IDS:
        await message.answer("Ваше обращение зарегистрировано. Пожалуйста, ожидайте ✅")
        kb = ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="Стоп тревогу")]],
            resize_keyboard=True
        )
        alert_running = True
        alert_task = asyncio.create_task(alert_loop(kb))
    else:
        await message.answer("Этот бот не для тебя, кышь отсюда ❌")

# 🚨 Цикл тревоги
async def alert_loop(kb):
    while alert_running:
        await bot.send_message(ALERT_USER_ID, "🚨 Она написала! Езжай за цветами 🌹", reply_markup=kb)
        await asyncio.sleep(3)

# 🛑 Остановка тревоги
@dp.message(lambda msg: msg.text == "Стоп тревогу")
async def stop_alert(message: types.Message):
    global alert_running
    if message.from_user.id == ALERT_USER_ID:
        alert_running = False
        await message.answer("Тревога остановлена 🛑")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
