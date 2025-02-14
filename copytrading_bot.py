from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, CallbackContext

# 🔑 Configuración del bot
TOKEN = "7896585911:AAELNq-rpwNGeOK1aFMwEk6U63_X4Jf_aW8"

# 🔗 Enlaces de pago (Reemplázalos con los reales)
PAGOS = {
    "dia": "https://tupago.com/dia",
    "semana": "https://tupago.com/semana",
    "mensual": "https://tupago.com/mensual",
    "trimestral": "https://tupago.com/trimestral"
}

# 📌 MENÚ PRINCIPAL
async def start(update: Update, context: CallbackContext):
    await mostrar_menu(update)

# 📊 MENÚ DE PLANES
async def menu_planes(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    
    mensaje = """
📊 *suscripciones* 📊

Elige el plan que mejor se adapte a ti. Solo haz click en el botón de pago y empieza a operar con *Wayne Futures* 🚀📈💰
"""
    botones = [
        [InlineKeyboardButton("📅 Día - $29.99", url=PAGOS["dia"])],
        [InlineKeyboardButton("📆 Semana - $99.99", url=PAGOS["semana"])],
        [InlineKeyboardButton("💳 Mensual - $349.99", url=PAGOS["mensual"])],
        [InlineKeyboardButton("💎 Trimestral - $899.99", url=PAGOS["trimestral"])],
        [InlineKeyboardButton("⬅️ Volver al Menú", callback_data="menu")]
    ]
    
    keyboard = InlineKeyboardMarkup(botones)
    await query.edit_message_text(mensaje, reply_markup=keyboard, parse_mode="Markdown")

# 📞 CONTACTO
async def menu_contacto(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    
    mensaje = """
📞 *Contacto* 📞

Si necesitas ayuda, contáctanos en:
✉️ *Email:* support@waynefutures.com
📱 *Telegram:* @WayneSupport
🌐 *Web:* [waynefutures.com](https://waynefutures.com)

⬅️ *Volver al Menú* seleccionando la opción abajo.
"""
    botones = [[InlineKeyboardButton("⬅️ Volver al Menú", callback_data="menu")]]
    keyboard = InlineKeyboardMarkup(botones)
    await query.edit_message_text(mensaje, reply_markup=keyboard, parse_mode="Markdown")

# 🔄 RESPUESTA AUTOMÁTICA A CUALQUIER MENSAJE
async def respuesta_automatica(update: Update, context: CallbackContext):
    nombre_usuario = update.message.from_user.first_name
    mensaje = f"👋 Hola, {nombre_usuario}! Bienvenida/o a *Wayne Futures* 🚀\n\nSelecciona una opción:"
    botones = [
        [InlineKeyboardButton("👥 ¿Quiénes Somos?", callback_data="quienes_somos")],
        [InlineKeyboardButton("📊 Suscripciones", callback_data="suscripciones")],
        [InlineKeyboardButton("📞 Contacto", callback_data="contacto")],
        [InlineKeyboardButton("📜 Politicas y Privacidad", callback_data="Politicas y Privacidad")],
    ]
    
    keyboard = InlineKeyboardMarkup(botones)
    await update.message.reply_text(mensaje, reply_markup=keyboard, parse_mode="Markdown")

# 🔙 VOLVER AL MENÚ PRINCIPAL
async def volver_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    await mostrar_menu(update, "👋 *Bienvenido de nuevo a Wayne Futures* 🚀\n\nSelecciona una opción:")

# 📌 FUNCIÓN PARA MOSTRAR EL MENÚ
async def mostrar_menu(update: Update, mensaje="👋 ¡Bienvenido a *Wayne Futures*! 🚀\n\nSelecciona una opción:"):
    botones = [
        [InlineKeyboardButton("👥 ¿Quiénes Somos?", callback_data="quienes_somos")],
        [InlineKeyboardButton("📊 Suscripciones", callback_data="planes")],
        [InlineKeyboardButton("📞 Contacto", callback_data="contacto")],
        [InlineKeyboardButton("📜 Politicas y Privacidad", callback_data="Politicas y Privacidad")],
    ]
    
    keyboard = InlineKeyboardMarkup(botones)
    
    if update.message:
        await update.message.reply_text(mensaje, reply_markup=keyboard, parse_mode="Markdown")
    elif update.callback_query:
        await update.callback_query.edit_message_text(mensaje, reply_markup=keyboard, parse_mode="Markdown")

# 📌 QUIÉNES SOMOS
async def quienes_somos(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    
    mensaje = """
👥 *¿Quiénes Somos?* 👥

*Wayne Futures* es una plataforma innovadora de CopyTrading que te permite invertir con los mejores. Nuestros expertos analizan los mercados para ti y tú solo debes seguir nuestras recomendaciones. ¡Comienza hoy mismo a operar con nosotros!

⬅️ *Volver al Menú* seleccionando la opción abajo.
"""
    botones = [[InlineKeyboardButton("⬅️ Volver al Menú", callback_data="menu")]]
    keyboard = InlineKeyboardMarkup(botones)
    await query.edit_message_text(mensaje, reply_markup=keyboard, parse_mode="Markdown")

# 📌 SUSCRIPCIONES
async def suscripciones(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    
    mensaje = """
📊 *Nuestros Planes de CopyTrading* 📊

Elige el plan que mejor se adapte a ti. Solo haz click en el botón de pago y empieza a operar con *Wayne Futures* 🚀📈💰
"""
    botones = [
        [InlineKeyboardButton("📅 Día - $29.99", url=PAGOS["dia"])],
        [InlineKeyboardButton("📆 Semana - $99.99", url=PAGOS["semana"])],
        [InlineKeyboardButton("💳 Mensual - $349.99", url=PAGOS["mensual"])],
        [InlineKeyboardButton("💎 Trimestral - $899.99", url=PAGOS["trimestral"])],
        [InlineKeyboardButton("⬅️ Volver al Menú", callback_data="menu")]
    ]
    
    keyboard = InlineKeyboardMarkup(botones)
    await query.edit_message_text(mensaje, reply_markup=keyboard, parse_mode="Markdown")

# 📌 Politicas y privacidad 
async def Politicas(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    
    mensaje = """
📜 *Politicas y privacidad * 📜

Al suscribirte a nuestros servicios, aceptas los siguientes términos:
1️⃣ Responsabilidad Propia: Todas las posiciones y operaciones que tomes son bajo tu propia responsabilidad. No garantizamos resultados y no nos hacemos responsables de pérdidas o ganancias derivadas de la información proporcionada.
2️⃣ Confidencialidad: Todo el contenido compartido (incluyendo análisis, imágenes de trades y estrategias) es exclusivo para suscriptores. Queda prohibida su distribución, reproducción o venta sin autorización.
3️⃣ Uso Personal: La información es solo para uso educativo y personal. No debe considerarse asesoramiento financiero.
El incumplimiento de estas normas puede resultar en la suspensión del servicio sin reembolso.
🔒 Wayne Futures se reserva el derecho de actualizar esta política en cualquier momento.
"""
    botones = [
        [InlineKeyboardButton("⬅️ Volver al Menú", callback_data="menu")]
    ]
    
    keyboard = InlineKeyboardMarkup(botones)
    await query.edit_message_text(mensaje, reply_markup=keyboard, parse_mode="Markdown")


# 🚀 INICIAR EL BOT
def main():
    app = Application.builder().token(TOKEN).build()
    
    # Comando /start
    app.add_handler(CommandHandler("start", start))
    
    # Manejo de botones del menú
    app.add_handler(CallbackQueryHandler(menu_planes, pattern="^planes$"))
    app.add_handler(CallbackQueryHandler(menu_contacto, pattern="^contacto$"))
    app.add_handler(CallbackQueryHandler(volver_menu, pattern="^menu$"))
    app.add_handler(CallbackQueryHandler(quienes_somos, pattern="^quienes_somos$"))
    app.add_handler(CallbackQueryHandler(suscripciones, pattern="^suscripciones$"))
    app.add_handler(CallbackQueryHandler(Politicas, pattern="^Politicas y Privacidad$"))
    # Manejo de cualquier mensaje de texto
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respuesta_automatica))

    print("✅ Bot de CopyTrading en marcha...")
    app.run_polling()

if __name__ == "__main__":
    main()
