import os
import logging
import asyncio
import sys

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# Pobierz token z Railway
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ Brak zmiennej BOT_TOKEN w Railway Variables!")

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "👋 <b>BetclicPolowanieBot uruchomiony!</b>\n\n"
        "Dostępne komendy:\n"
        "/quiz — przykładowy quiz\n"
        "/polowanie — info o polowaniu\n"
        "/kod — aktualne kody freebet"
    )

@dp.message(Command("quiz"))
async def quiz(message: Message):
    await message.answer(
        "🧠 <b>QUIZ [18:51:08]</b>\n\n"
        "❓🔍 <b>Czas na Quiz – : [KIM JESTEM?]</b> :\n\n"
        "Grałem w jednej drużynie z Dwightem Howardem, "
        "Steven Nashem, Johnem Wallem. 🏀\n\n"
        "✅ <b>Kobe Bryant</b>",
        disable_web_page_preview=True
    )

@dp.message(Command("polowanie"))
async def polowanie_cmd(message: Message):
    await message.answer("🔥 <b>Polowanie Betclic trwa!</b> Używaj /quiz i /kod")

@dp.message(Command("kod"))
async def kod(message: Message):
    await message.answer(
        "🎟️ <b>Aktualne kody:</b>\n\n"
        "<code>W3Lc0mePOL26</code>\n"
        "<code>POLOWAN1E26</code>"
    )

async def main():
    print("🚀 Bot wystartował pomyślnie!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
