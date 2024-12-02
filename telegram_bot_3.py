from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler, CallbackContext

# Durumlar
TEMEL_ADETI, TEMEL_KISA_KENAR, TEMEL_UZUN_KENAR, TEMEL_YUKSEKLIK = range(4)
ELEVASYON_ADETI, ELEVASYON_KISA_KENAR, ELEVASYON_UZUN_KENAR, ELEVASYON_KESIT, ELEVASYON_YUKSEKLIK = range(5)

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        'Metrajını hesaplamak istediğiniz Bölümü Seçiniz..\n/temel\n/elevasyon'
    )

# Temel hesaplama fonksiyonları
async def temel_start(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text('Lütfen Toplam Temel Miktarını Giriniz (Adet):')
    return TEMEL_ADETI

async def temel_adeti(update: Update, context: CallbackContext) -> int:
    context.user_data['temel_adeti'] = int(update.message.text)
    context.user_data['kalip_liste'] = []
    context.user_data['beton_liste'] = []
    context.user_data['current_index'] = 0
    await update.message.reply_text(f"{context.user_data['current_index'] + 1}. Temelin Kısa Kenar Ölçüsünü Giriniz (m):")
    return TEMEL_KISA_KENAR

async def temel_kisa_kenar(update: Update, context: CallbackContext) -> int:
    context.user_data['kisa_kenar'] = float(update.message.text)
    await update.message.reply_text(f"{context.user_data['current_index'] + 1}. Temelin Uzun Kenar Ölçüsünü Giriniz (m):")
    return TEMEL_UZUN_KENAR

async def temel_uzun_kenar(update: Update, context: CallbackContext) -> int:
    context.user_data['uzun_kenar'] = float(update.message.text)
    await update.message.reply_text(f"{context.user_data['current_index'] + 1}. Temelin Yükseklik Ölçüsünü Giriniz (m):")
    return TEMEL_YUKSEKLIK

async def temel_yukseklik(update: Update, context: CallbackContext) -> int:
    yukseklik = float(update.message.text)
    kisa_kenar = context.user_data['kisa_kenar']
    uzun_kenar = context.user_data['uzun_kenar']

    temel_kalip = yukseklik * 2 * (kisa_kenar + uzun_kenar)
    temel_beton = yukseklik * kisa_kenar * uzun_kenar

    context.user_data['kalip_liste'].append(temel_kalip)
    context.user_data['beton_liste'].append(temel_beton)
    context.user_data['current_index'] += 1

    await update.message.reply_text(f"\n{context.user_data['current_index']}. Temelin Kalıp Metrajı: {temel_kalip} m²'dir.")
    await update.message.reply_text(f"Sırasıyla Kalıp Metrajları: {context.user_data['kalip_liste']} m²'dir.")
    await update.message.reply_text(f"Toplam Kalıp Metrajı: {sum(context.user_data['kalip_liste'])} m²'dir.")
    await update.message.reply_text(f"\n{context.user_data['current_index']}. Temelin Beton Metrajı: {temel_beton} m³'dür.")
    await update.message.reply_text(f"Sırasıyla Beton Metrajları: {context.user_data['beton_liste']} m³'dür.")
    await update.message.reply_text(f"Toplam Beton Metrajı: {sum(context.user_data['beton_liste'])} m³'dür.")

    if context.user_data['current_index'] < context.user_data['temel_adeti']:
        await update.message.reply_text(f"{context.user_data['current_index'] + 1}. Temelin Kısa Kenar Ölçüsünü Giriniz (m):")
        return TEMEL_KISA_KENAR
    else:
        return ConversationHandler.END

# Elevasyon hesaplama fonksiyonları
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler, CallbackContext

# Durumlar
TEMEL_ADETI, TEMEL_KISA_KENAR, TEMEL_UZUN_KENAR, TEMEL_YUKSEKLIK = range(4)
ELEVASYON_ADETI, ELEVASYON_KISA_KENAR, ELEVASYON_UZUN_KENAR, ELEVASYON_KESIT, ELEVASYON_YUKSEKLIK = range(5)

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        'Metrajını hesaplamak istediğiniz Bölümü Seçiniz..\n/temel\n/elevasyon'
    )

# Temel hesaplama fonksiyonları
async def temel_start(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text('Lütfen Toplam Temel Miktarını Giriniz (Adet):')
    return TEMEL_ADETI

async def temel_adeti(update: Update, context: CallbackContext) -> int:
    context.user_data['temel_adeti'] = int(update.message.text)
    context.user_data['kalip_liste'] = []
    context.user_data['beton_liste'] = []
    context.user_data['current_index'] = 0
    await update.message.reply_text(f"{context.user_data['current_index'] + 1}. Temelin Kısa Kenar Ölçüsünü Giriniz (m):")
    return TEMEL_KISA_KENAR

async def temel_kisa_kenar(update: Update, context: CallbackContext) -> int:
    context.user_data['kisa_kenar'] = float(update.message.text)
    await update.message.reply_text(f"{context.user_data['current_index'] + 1}. Temelin Uzun Kenar Ölçüsünü Giriniz (m):")
    return TEMEL_UZUN_KENAR

async def temel_uzun_kenar(update: Update, context: CallbackContext) -> int:
    context.user_data['uzun_kenar'] = float(update.message.text)
    await update.message.reply_text(f"{context.user_data['current_index'] + 1}. Temelin Yükseklik Ölçüsünü Giriniz (m):")
    return TEMEL_YUKSEKLIK

async def temel_yukseklik(update: Update, context: CallbackContext) -> int:
    yukseklik = float(update.message.text)
    kisa_kenar = context.user_data['kisa_kenar']
    uzun_kenar = context.user_data['uzun_kenar']

    temel_kalip = yukseklik * 2 * (kisa_kenar + uzun_kenar)
    temel_beton = yukseklik * kisa_kenar * uzun_kenar

    context.user_data['kalip_liste'].append(temel_kalip)
    context.user_data['beton_liste'].append(temel_beton)
    context.user_data['current_index'] += 1

    await update.message.reply_text(f"\n{context.user_data['current_index']}. Temelin Kalıp Metrajı: {temel_kalip} m²'dir.")
    await update.message.reply_text(f"Sırasıyla Kalıp Metrajları: {context.user_data['kalip_liste']} m²'dir.")
    await update.message.reply_text(f"Toplam Kalıp Metrajı: {sum(context.user_data['kalip_liste'])} m²'dir.")
    await update.message.reply_text(f"\n{context.user_data['current_index']}. Temelin Beton Metrajı: {temel_beton} m³'dür.")
    await update.message.reply_text(f"Sırasıyla Beton Metrajları: {context.user_data['beton_liste']} m³'dür.")
    await update.message.reply_text(f"Toplam Beton Metrajı: {sum(context.user_data['beton_liste'])} m³'dür.")

    if context.user_data['current_index'] < context.user_data['temel_adeti']:
        await update.message.reply_text(f"{context.user_data['current_index'] + 1}. Temelin Kısa Kenar Ölçüsünü Giriniz (m):")
        return TEMEL_KISA_KENAR
    else:
        return ConversationHandler.END

# Elevasyon hesaplama fonksiyonları
async def elevasyon_start(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text('Lütfen Toplam Elevasyon Miktarını Giriniz (Adet):')
    return ELEVASYON_ADETI

async def elevasyon_adeti(update: Update, context: CallbackContext) -> int:
    context.user_data['elevasyon_adeti'] = int(update.message.text)
    context.user_data['kalip_liste'] = []
    context.user_data['beton_liste'] = []
    context.user_data['current_index'] = 0
    await update.message.reply_text(f"{context.user_data['current_index'] + 1}. Elevasyonin Kısa Kenar Ölçüsünü Giriniz (m):")
    return ELEVASYON_KISA_KENAR

async def elevasyon_kisa_kenar(update: Update, context: CallbackContext) -> int:
    context.user_data['kisa_kenar'] = float(update.message.text)
    await update.message.reply_text(f"{context.user_data['current_index'] + 1}. Elevasyonin Uzun Kenar Ölçüsünü Giriniz (m):")
    return ELEVASYON_UZUN_KENAR

async def elevasyon_uzun_kenar(update: Update, context: CallbackContext) -> int:
    context.user_data['uzun_kenar'] = float(update.message.text)
    await update.message.reply_text(f"{context.user_data['current_index'] + 1}. Elevasyonin Kesit (Et Kalınlığı) Ölçüsünü Giriniz (m):")
    return ELEVASYON_KESIT

async def elevasyon_kesit(update: Update, context: CallbackContext) -> int:
    context.user_data['kesit'] = float(update.message.text)
    await update.message.reply_text(f"{context.user_data['current_index'] + 1}. Elevasyonin Yükseklik Ölçüsünü Giriniz (m):")
    return ELEVASYON_YUKSEKLIK

async def elevasyon_yukseklik(update: Update, context: CallbackContext) -> int:
    yukseklik = float(update.message.text)
    kisa_kenar = context.user_data['kisa_kenar']
    uzun_kenar = context.user_data['uzun_kenar']
    kesit = context.user_data['kesit']

    elevasyon_kalip = yukseklik * 2 * ((kisa_kenar + uzun_kenar) + (kisa_kenar - 2 * kesit + uzun_kenar - 2 * kesit))
    elevasyon_beton = yukseklik * (kisa_kenar * uzun_kenar - (kisa_kenar - 2 * kesit) * (uzun_kenar - 2 * kesit))

    context.user_data['kalip_liste'].append(elevasyon_kalip)
    context.user_data['beton_liste'].append(elevasyon_beton)
    context.user_data['current_index'] += 1

    await update.message.reply_text(f"\n{context.user_data['current_index']}. Elevasyonin Kalıp Metrajı: {elevasyon_kalip} m²'dir.")
    await update.message.reply_text(f"Sırasıyla Kalıp Metrajları: {context.user_data['kalip_liste']} m²'dir.")
    await update.message.reply_text(f"Toplam Kalıp Metrajı: {sum(context.user_data['kalip_liste'])} m²'dir.")
    await update.message.reply_text(f"\n{context.user_data['current_index']}. Elevasyonin Beton Metrajı: {elevasyon_beton} m³'dür.")
    await update.message.reply_text(f"Sırasıyla Beton Metrajları: {context.user_data['beton_liste']} m³'dür.")
    await update.message.reply_text(f"Toplam Beton Metrajı: {sum(context.user_data['beton_liste'])} m³'dür.")

    if context.user_data['current_index'] < context.user_data['elevasyon_adeti']:
        await update.message.reply_text(f"{context.user_data['current_index'] + 1}. Elevasyonin Kısa Kenar Ölçüsünü Giriniz (m):")
        return ELEVASYON_KISA_KENAR
    else:
        return ConversationHandler.END

def main() -> None:
    application = Application.builder().token("8157924489:AAEjMQqeF3J8zRS_6qWSuXHd22d6TNKvs_Y").build()

    temel_conv_handler = ConversationHandler(
        entry_points=[CommandHandler('temel', temel_start)],
        states={
            TEMEL_ADETI: [MessageHandler(filters.TEXT & ~filters.COMMAND, temel_adeti)],
            TEMEL_KISA_KENAR: [MessageHandler(filters.TEXT & ~filters.COMMAND, temel_kisa_kenar)],
            TEMEL_UZUN_KENAR: [MessageHandler(filters.TEXT & ~filters.COMMAND, temel_uzun_kenar)],
            TEMEL_YUKSEKLIK: [MessageHandler(filters.TEXT & ~filters.COMMAND, temel_yukseklik)],
        },
        fallbacks=[CommandHandler('start', start)],
    )

    elevasyon_conv_handler = ConversationHandler(
        entry_points=[CommandHandler('elevasyon', elevasyon_start)],
        states={
            ELEVASYON_ADETI: [MessageHandler(filters.TEXT & ~filters.COMMAND, elevasyon_adeti)],
            ELEVASYON_KISA_KENAR: [MessageHandler(filters.TEXT & ~filters.COMMAND, elevasyon_kisa_kenar)],
            ELEVASYON_UZUN_KENAR: [MessageHandler(filters.TEXT & ~filters.COMMAND, elevasyon_uzun_kenar)],
            ELEVASYON_KESIT: [MessageHandler(filters.TEXT & ~filters.COMMAND, elevasyon_kesit)],
            ELEVASYON_YUKSEKLIK: [MessageHandler(filters.TEXT & ~filters.COMMAND, elevasyon_yukseklik)],
        },
        fallbacks=[CommandHandler('start', start)],
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(temel_conv_handler)
    application.add_handler(elevasyon_conv_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
