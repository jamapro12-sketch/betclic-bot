import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
import asyncio
import logging

# ====================== USTAWIENIA ======================
logging.basicConfig(level=logging.INFO)

# Odczytujemy token z zmiennej środowiskowej Railway
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("Brak zmiennej BOT_TOKEN! Dodaj ją w Railway → Variables")

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

# ====================== KOMENDY ======================

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "👋 <b>Witaj w BetclicPolowanieBot!</b>\n\n"
        "Dostępne komendy:\n"
        "/quiz → wrzuca quiz jak na screenie\n"
        "/polowanie → aktualne info o Polowaniu Betclic\n"
        "/kod → najnowsze kody freebet\n\n"
        "Po prostu wpisz komendę i bot wyśle gotowy post 🎯"
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
async def polowanie(message: Message):
    await message.answer(
        "🔥 <b>Polowanie Betclic – trwa teraz!</b>\n\n"
        "Co chwilę pojawiają się quizy + kody freebet 🏀\n"
        "Użyj /quiz żeby wrzucić pytanie\n"
        "Użyj /kod żeby wrzucić aktualny kod\n\n"
        "Powodzenia w łowieniu freebetów! 💰"
    )

@dp.message(Command("kod"))
async def kod(message: Message):
    await message.answer(
        "🎟️ <b>Aktualne kody freebet – Polowanie Betclic</b>\n\n"
        "🔥 Wklej w aplikacji Betclic:\n"
        "<code>W3Lc0mePOL26</code>   ← najczęściej działa\n"
        "<code>POLOWAN1E26</code>   ← backup\n\n"
        "Kody pojawiają się co godzinę – sprawdzaj regularnie!\n\n"
        "✅ Skopiuj i wklej od razu po zobaczeniu quizu"
    )

# ====================== URUCHOMIENIE ======================
async def main():
    print("🚀 Bot BetclicPolowanieBot uruchomiony!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
