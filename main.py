import logging

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from config import BOT_TOKEN
from responses import get_response, get_time, get_date


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


keyboard = [
    ["👤 Über mich", "🧰 Skills"],
    ["🚀 Projekte", "📫 Kontakt"],
    ["⏰ Uhrzeit", "📅 Datum"],
]

reply_markup = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True,
    one_time_keyboard=False,
)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Hallo! 👋\n\n"
        "Ich bin ein deutscher Telegram-Chatbot von Mohammad Javad.\n"
        "Du kannst die Buttons benutzen oder /help schreiben.",
        reply_markup=reply_markup,
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = """
📌 Verfügbare Befehle:

/start - Bot starten
/help - Hilfe anzeigen
/about - Über mich
/skills - Skills anzeigen
/projects - Projekte anzeigen
/contact - Kontaktinformationen
/time - Aktuelle Uhrzeit
/date - Heutiges Datum

Du kannst auch normale Nachrichten schreiben, zum Beispiel:
- Hallo
- Python
- Django
- KI
- Uhrzeit
- Datum
"""
    await update.message.reply_text(help_text)


async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "👤 Über mich\n\n"
        "Ich bin Mohammad Javad Vafajoo, M.Sc. Artificial Intelligence Student "
        "an der Universität Passau und Full-Stack Developer.\n\n"
        "Ich interessiere mich für Webentwicklung, Python, Django, "
        "AI Agents und LLM-basierte Anwendungen."
    )


async def skills_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🧰 Skills\n\n"
        "Programmiersprachen:\n"
        "- Python\n"
        "- JavaScript\n"
        "- C++\n"
        "- C#\n"
        "- SQL\n\n"
        "Webentwicklung:\n"
        "- Django\n"
        "- HTML / CSS\n"
        "- Bootstrap\n"
        "- React.js\n"
        "- WordPress\n\n"
        "KI & Tools:\n"
        "- LangChain\n"
        "- Claude API\n"
        "- Streamlit\n"
        "- Pydantic\n"
        "- RAG-Grundlagen\n"
        "- Git"
    )


async def projects_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🚀 Projekte\n\n"
        "1. AI Research Assistant\n"
        "- Python, LangChain, Claude API, Streamlit, Pydantic\n"
        "- Recherchetool mit Websuche, PDF-Analyse und strukturierten Ergebnissen\n\n"
        "2. NewsCrawler\n"
        "- Python, Django, HTML, Web Crawling\n"
        "- Web-App zur Extraktion von Nachrichtenüberschriften und Links\n\n"
        "3. Technodemy\n"
        "- WordPress, HTML, CSS, BigBlueButton\n"
        "- CMS-basierte E-Learning-Plattform\n\n"
        "4. Telegram Chatbot\n"
        "- Python, Telegram Bot API\n"
        "- Deutscher Chatbot mit Befehlen, Buttons und Keyword-Antworten"
    )


async def contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "📫 Kontakt\n\n"
        "E-Mail: mohammadjavadvafajoo@gmail.com\n"
        "LinkedIn: https://linkedin.com/in/mohammadjavad-vafajoo-493a12271\n"
        "GitHub: https://github.com/javad-hub"
    )


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"⏰ Die aktuelle Uhrzeit ist: {get_time()}")


async def date_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"📅 Heutiges Datum ist: {get_date()}")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_text = update.message.text

    if user_text == "👤 Über mich":
        await about_command(update, context)
        return

    if user_text == "🧰 Skills":
        await skills_command(update, context)
        return

    if user_text == "🚀 Projekte":
        await projects_command(update, context)
        return

    if user_text == "📫 Kontakt":
        await contact_command(update, context)
        return

    if user_text == "⏰ Uhrzeit":
        await time_command(update, context)
        return

    if user_text == "📅 Datum":
        await date_command(update, context)
        return

    response = get_response(user_text)
    await update.message.reply_text(response)


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.error("Ein Fehler ist aufgetreten:", exc_info=context.error)


def main() -> None:
    app = (
    Application.builder()
    .token(BOT_TOKEN)
    .connect_timeout(30)
    .read_timeout(30)
    .write_timeout(30)
    .pool_timeout(30)
    .build()
)

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about_command))
    app.add_handler(CommandHandler("skills", skills_command))
    app.add_handler(CommandHandler("projects", projects_command))
    app.add_handler(CommandHandler("contact", contact_command))
    app.add_handler(CommandHandler("time", time_command))
    app.add_handler(CommandHandler("date", date_command))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.add_error_handler(error_handler)

    print("Bot wurde gestartet ...")
    app.run_polling()


if __name__ == "__main__":
    main()