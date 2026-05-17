from datetime import datetime


def get_time() -> str:
    now = datetime.now()
    return now.strftime("%H:%M:%S")


def get_date() -> str:
    today = datetime.now()
    return today.strftime("%d.%m.%Y")


def get_response(user_message: str) -> str:
    message = user_message.lower().strip()

    greetings = ["hallo", "hi", "hey", "guten morgen", "guten tag", "guten abend"]
    thanks = ["danke", "vielen dank", "dankeschön"]
    goodbye = ["tschüss", "bye", "auf wiedersehen", "bis später"]

    if message in greetings:
        return "Hallo! Schön, dich zu sehen 😊 Wie kann ich dir helfen?"

    if message in thanks:
        return "Gerne! 😊"

    if message in goodbye:
        return "Tschüss! Viel Erfolg beim Programmieren 👋"

    if "wer bist du" in message or "was bist du" in message:
        return (
            "Ich bin ein deutscher Telegram-Chatbot, entwickelt mit Python "
            "und der Telegram Bot API."
        )

    if "python" in message:
        return "Python ist eine sehr gute Sprache für Bots, Webentwicklung, Automatisierung und KI."

    if "django" in message:
        return "Django ist ein starkes Python-Webframework für schnelle und sichere Webentwicklung."

    if "ki" in message or "ai" in message or "künstliche intelligenz" in message:
        return "KI ist ein spannendes Feld. Besonders interessant sind LLMs, AI Agents und RAG-Systeme."

    if "zeit" in message or "uhrzeit" in message:
        return f"Die aktuelle Uhrzeit ist: {get_time()}"

    if "datum" in message:
        return f"Heutiges Datum ist: {get_date()}"

    return (
        "Entschuldigung, das habe ich nicht verstanden. "
        "Schreibe /help, um alle Befehle zu sehen."
    )