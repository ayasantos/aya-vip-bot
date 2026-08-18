import os

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("RENDER_EXTERNAL_URL")
PORT = int(os.getenv("PORT", "10000"))

# Depois vamos descobrir esse número pelo próprio bot.
TOPIC_ID = os.getenv("INTERACTION_TOPIC_ID")
TOPIC_ID = int(TOPIC_ID) if TOPIC_ID else None


async def boas_vindas(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    if not update.message:
        return

    for membro in update.message.new_chat_members:

        # Não dá boas-vindas para bots
        if membro.is_bot:
            continue

        nome = membro.first_name or "amor"

        mensagem = f"""💋 Seja bem-vindo(a), {nome}!

Que bom ter você por aqui 😏🔥

👀 Dá uma olhadinha nas prévias que deixei no grupo...
E quando a curiosidade bater, tem conteúdos completos esperando por você. 🔓

💎 PREMIUM — R$ 29,90
👑 OURO — R$ 49,90

👉 Confira o tópico DESBLOQUEAR 🔐 para escolher seu acesso.

Aproveita... 💋"""

        # Quando configurarmos o tópico INTERAÇÃO,
        # a mensagem irá diretamente para ele.
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=mensagem,
            message_thread_id=TOPIC_ID,
        )


async def mostrar_topic_id(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    if not update.message:
        return

    topic_id = update.message.message_thread_id

    await update.message.reply_text(
        f"ID deste tópico: {topic_id}"
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(
        filters.StatusUpdate.NEW_CHAT_MEMBERS,
        boas_vindas
    )
)

app.add_handler(
    CommandHandler("topicid", mostrar_topic_id)
)

print("Aya VIP Bot está online 💋")

app.run_webhook(
    listen="0.0.0.0",
    port=PORT,
    url_path="webhook",
    webhook_url=f"{WEBHOOK_URL}/webhook",
)
