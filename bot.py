import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

async def boas_vindas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for membro in update.message.new_chat_members:
        if membro.is_bot:
            continue

        nome = membro.first_name

        mensagem = f"""💋 Seja bem-vindo(a), {nome}!

Que bom ter você por aqui 😏🔥

👀 Dá uma olhadinha nas prévias que deixei no grupo...
E quando a curiosidade bater, tem conteúdos completos esperando por você. 🔓

💎 PREMIUM — R$ 29,90
👑 OURO — R$ 49,90

👉 Confira o tópico DESBLOQUEAR 🔐 para escolher seu acesso.

Aproveita... 💋"""

        await update.message.reply_text(mensagem)

app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, boas_vindas)
)

print("Aya VIP Bot está online 💋")
app.run_polling()
