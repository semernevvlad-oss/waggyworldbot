import telebot
from telebot import types

# ================= CONFIGURATION =================
BOT_TOKEN = "8891359420:AAGCG8llxmXjR3sMOgGxb_bCja9_GOu2T9A"

# Впишите сюда свой Telegram ID цифрами (узнать можно у @userinfobot)
ADMIN_IDS = [123456789]  # <-- ОБЯЗАТЕЛЬНО ЗАМЕНИТЕ НА СВОЙ ID
# =================================================

bot = telebot.TeleBot(BOT_TOKEN)

# Хранилища в памяти
user_states = {}
user_appeals = {}
admin_reply_targets = {}

# Текст правил проекта
RULES_TEXT = """📜 ПРАВИЛА ПРОЕКТА WAGGYWORLD (Часть 1)

⚠️ САМЫЕ АКТУАЛЬНЫЕ ПРАВИЛА НА САЙТЕ https://ragerise.pw/rules.php ⚠️

⚠️ 0. ОСНОВНЫЕ ПОЛОЖЕНИЯ
📌 0.1 Незнание правил не освобождает от ответственности.
📌 0.2 Играя на сервере, вы соглашаетесь с правилами.
📌 0.3 Администратор может наказать за нарушение, не указанное в правилах.
📌 0.4 – 0.7 Администрация не несёт ответственности за проблемы с доступом, потерю предметов и сбои серверов.
📌 0.8 Все игроки обязаны соблюдать правила.
📌 0.9 Все действия и сообщения логируются.
📌 0.10 Администрация может менять правила без уведомлений.
📌 0.11 Запрещено оскорблять или провоцировать администрацию.

━━━━━━━━━━━━━━━━━━━━━━━━━

1. 💬 ПРАВИЛА ЧАТА
🔇 1.1 КАПС, спам, флуд — мут 30–360 мин
🗯 1.2 Оскорбления игроков — мут 60–360 мин
🗯 1.3 Оскорбление проекта/Администрации — мут 24 часа
🚫 1.4 Реклама сторонних ресурсов — мут 180 мин - бан на 3 дня
🧨 1.6 Оскорбления родных — мут до 12ч / бан 3 дня
🌍 1.7 Разжигание розни, расизм — мут 12 ч
🔒 1.8 Обход мута — мут 360 мин
🔎 1.9 Вызов на проверку — бан 3 дня
🔗 1.10 Контакты в чатах — мут 120 мин
❗️ 1.12 Признание в нарушении — повод для бана
❗️ 1.13 Аморальная лексика — мут 30 мин

━━━━━━━━━━━━━━━━━━━━━━━━━

2. 🎮 ИГРОВЫЕ ПРАВИЛА
🛑 2.1 Читы (включая удаленные до 14 дней) — IP-бан 40 дн.
⚙️ 2.2 Запрещённые моды — IP-бан 14 дн.
🛠 2.3 Распространение читов — перманентный IP-бан
🎭 2.4 Подстрекательство к нарушению — бан 3 дня
🚷 2.5 Препятствие модерации — бан 3 дня
🔁 2.6 Обход бана — IP-бан 30 дней
💣 2.7 Умышленный вред серверу — перманентный IP-бан
🏷 2.8 Названия кланов с нарушением — удаление клана, бан главы 10 дней
🔐 2.9 Личные данные игроков — перманентный IP-бан
🎭 2.10 Выдача себя за администрацию — IP-бан 14 дней
🧪 2.11 Багаюз — бан 14 дней
💰 2.12 Дюп / утаивание дюпа — IP-бан 60 дней
🪙 2.13 Продажа за IRL-деньги — перманентный IP-бан
🧪 2.14 Помеха контенту для медиа — бан 3 часа"""

# Текст условий для TikToker
TIKTOK_TEXT = """📱 Заявка на медиа (TikTok)

Мы рады, что вы захотели присоединиться к нам! Пожалуйста, заполните форму подачи заявки:

1. Ваш ник на сервере
2. Ссылка на ваш канал

Если вы уже снимали и у вас есть просмотры на канале - можете сразу подавать заявку.

Иначе нужно выполнить условия:

1️⃣ Сними 3 ролика по серверу WaggyWorld
2️⃣ Каждый ролик должен набрать от 500 просмотров

🎁 После этого — мы выдадим тебе привилегию TIKTOK!

💸 А вот за просмотры ты получаешь награды:
- 500 просмотров → 50 риликов
- 1000 просмотров → 100 риликов
- 5000 просмотров → 500 риликов
- 10 000 просмотров → 1000 риликов

🔥 А если у тебя будет большой актив и хорошие просмотры — ты сможешь стать МЕДИА проекта и получать реальные деньги 💰

📋 Критерии для канала:
- На канале нет рекламы читов
- В описании канала указано: Играю тут: play.waggyworld.pw

🎬 Критерии для роликов:
- Ролик должен быть снят на сервере WaggyWorld
- В ролике не должно быть рекламы читов и других серверов
- В названии и на экране (минимум 5 секунд) должен быть IP: play.waggyworld.pw
- Обязательно тег #waggyworld

Введите ваш ник на сервере:"""

# Текст условий для YouTuber
YOUTUBE_TEXT = """🎬 Заявка на медиа (YouTube)

Мы рады, что вы захотели присоединиться к нам! Пожалуйста, заполните форму подачи заявки:

1. Ваш ник на сервере
2. Ссылка на ваш канал

Если вы уже снимали и у вас есть просмотры на канале - можете сразу подавать заявку.

Иначе нужно выполнить условия:

Мы запустили новую привилегию — YOUTUBE 💫
Получить её может каждый, кто готов немного поснимать контент про наш сервер!

1️⃣ Сними 1 ролик по серверу WaggyWorld
2️⃣ Ролик должен набрать 300 просмотров

🎁 После этого — мы выдадим тебе привилегию YOUTUBE!

💸 А вот за просмотры ты получаешь награды:
- 300 просмотров → 150 риликов
- 500 просмотров → 500 риликов
- 1000 просмотров → 1000 риликов
- 5000 просмотров → 10.000 риликов

🔥 А если у тебя будет большой актив и хорошие просмотры — ты сможешь стать МЕДИА проекта и получать реальные деньги 💰

📋 Критерии для канала:
- На канале нет рекламы читов

🎬 Критерии для роликов:
1) Ролик должен быть снят на сервере WaggyWorld
2) В ролике не должно быть рекламы читов и других серверов
4) В названии должно быть указано название сервер WaggyWorld
5) Длинна ролика должна быть не менее 8-ми минут
6) В описании под роликом должно быть:

Играю всегда тут:
- waggyworld.mc-games.xyz — основной сервер
- Telegram: https://t.me/waggyworldd

Обязательно тег #waggyworld

Введите ваш ник на сервере:"""


def get_main_keyboard():
    """Создание главной клавиатуры меню"""
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    
    btn_support = types.InlineKeyboardButton(text="💬 Поддержка", callback_data="btn_support")
    btn_appeals = types.InlineKeyboardButton(text="📬 Мои обращения", callback_data="btn_my_appeals")
    keyboard.row(btn_support, btn_appeals)

    btn_media = types.InlineKeyboardButton(text="📺 Подать заявку на медиа", callback_data="btn_media")
    btn_helper = types.InlineKeyboardButton(text="🛡 Подать заявку на хелпера", callback_data="btn_helper")
    keyboard.row(btn_media, btn_helper)

    btn_rules = types.InlineKeyboardButton(text="📜 Правила проекта", callback_data="btn_rules")
    btn_info = types.InlineKeyboardButton(text="ℹ️ Информация о сервере", callback_data="btn_info")
    keyboard.add(btn_rules)
    keyboard.add(btn_info)
    
    return keyboard


def get_media_keyboard():
    """Клавиатура выбора платформы медиа"""
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    btn_tt = types.InlineKeyboardButton(text="📱 Я тиктокер", callback_data="btn_tiktok")
    btn_yt = types.InlineKeyboardButton(text="🎬 Я ютубер", callback_data="btn_youtuber")
    btn_back = types.InlineKeyboardButton(text="◀️ Назад", callback_data="btn_back_to_main")
    
    keyboard.add(btn_tt, btn_yt, btn_back)
    return keyboard


@bot.message_handler(commands=["start"])
def send_welcome(message):
    user_id = message.from_user.id
    user_states[user_id] = None

    user_name = message.from_user.first_name
    if message.from_user.last_name:
        user_name += f" {message.from_user.last_name}"

    welcome_text = (
        f"👋 Добро пожаловать на сервер WaggyWorld!\n\n"
        f"Привет, {user_name}! Я официальный бот проекта WaggyWorld.\n\n"
        f"Выберите интересующий вас раздел с помощью кнопок ниже 👇"
    )
    try:
        bot.send_message(message.chat.id, welcome_text, reply_markup=get_main_keyboard())
    except Exception as e:
        print(f"Ошибка отправки /start: {e}")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    user_id = call.from_user.id

    try:
        if call.data == "btn_support":
            bot.answer_callback_query(call.id)
            user_states[user_id] = "waiting_for_appeal"
            bot.send_message(
                call.message.chat.id,
                "💬 Опишите максимально подробно и в 1 сообщении вашу просьбу:\nМожно приложить скриншот.",
            )

        # Вызов меню выбора платформы медиа
        elif call.data == "btn_media":
            bot.answer_callback_query(call.id)
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="📺 **Подать заявку на медиа**\n\nВыберите вашу платформу:",
                parse_mode="Markdown",
                reply_markup=get_media_keyboard()
            )

        # Возврат в главное меню
        elif call.data == "btn_back_to_main":
            bot.answer_callback_query(call.id)
            user_name = call.from_user.first_name
            welcome_text = (
                f"👋 Добро пожаловать на сервер WaggyWorld!\n\n"
                f"Привет, {user_name}! Я официальный бот проекта WaggyWorld.\n\n"
                f"Выберите интересующий вас раздел с помощью кнопок ниже 👇"
            )
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=welcome_text,
                reply_markup=get_main_keyboard()
            )

        # Выбор TikTok
        elif call.data == "btn_tiktok":
            bot.answer_callback_query(call.id)
            user_states[user_id] = "waiting_for_tiktok_app"
            bot.send_message(
                call.message.chat.id,
                TIKTOK_TEXT,
                disable_web_page_preview=True
            )

        # Выбор YouTube
        elif call.data == "btn_youtuber":
            bot.answer_callback_query(call.id)
            user_states[user_id] = "waiting_for_yt_app"
            bot.send_message(
                call.message.chat.id,
                YOUTUBE_TEXT,
                disable_web_page_preview=True
            )

        elif call.data == "btn_helper":
            bot.answer_callback_query(call.id)
            user_states[user_id] = "waiting_for_helper_app"
            bot.send_message(
                call.message.chat.id,
                "🛡 **Подача заявки на хелпера:**\n\n"
                "Отправьте информацию о себе в одном сообщении:\n"
                "1. Ваше имя и возраст.\n"
                "2. Ваш игровой ник.\n"
                "3. Сколько времени готовы уделять серверу?\n"
                "4. Был ли опыт работы на других проектах?",
                parse_mode="Markdown"
            )

        elif call.data == "btn_my_appeals":
            bot.answer_callback_query(call.id)
            appeals = user_appeals.get(user_id, [])

            if not appeals:
                bot.send_message(call.message.chat.id, "📁 У вас пока нет созданных обращений или заявок.")
            else:
                text = "📬 **Ваши обращения и заявки:**\n\n"
                for idx, item in enumerate(appeals, 1):
                    text += (
                        f"**Заявка/Обращение №{idx}**\n"
                        f"📌 **Тип:** {item['type']}\n"
                        f"📝 {item['text']}\n"
                        f"───────────────\n"
                    )
                bot.send_message(call.message.chat.id, text, parse_mode="Markdown")

        elif call.data == "btn_rules":
            bot.answer_callback_query(call.id)
            bot.send_message(call.message.chat.id, RULES_TEXT, disable_web_page_preview=True)

        elif call.data == "btn_info":
            bot.answer_callback_query(call.id)
            bot.send_message(
                call.message.chat.id,
                "ℹ️ **Информация о сервере WaggyWorld:**\n\n"
                "🌐 IP: `waggyworld.mc-games.xyz`\n"
                "🎮 Режим: Аналог ReallyWorld\n"
                "📌 Версия: 1.12.2 - 1.20.x",
                parse_mode="Markdown",
            )

        elif call.data.startswith("reply_"):
            bot.answer_callback_query(call.id)
            if user_id not in ADMIN_IDS:
                bot.send_message(call.message.chat.id, "⛔ У вас нет прав администратора.")
                return

            target_user_id = int(call.data.split("_")[1])
            admin_reply_targets[user_id] = target_user_id
            user_states[user_id] = "waiting_for_admin_reply"
            bot.send_message(call.message.chat.id, "✍️ Введите ответ пользователю в следующем сообщении:")

    except Exception as e:
        print(f"Ошибка в колбэке: {e}")


@bot.message_handler(content_types=["text", "photo"])
def handle_all_messages(message):
    user_id = message.from_user.id
    current_state = user_states.get(user_id)

    try:
        # Обработка поддержки
        if current_state == "waiting_for_appeal":
            process_and_send_submission(message, "Поддержка", "✅ Ваше обращение отправлено в поддержку!")

        # Обработка заявки на TikTok
        elif current_state == "waiting_for_tiktok_app":
            process_and_send_submission(message, "Медиа (TikTok)", "✅ Ваша заявка на TikTok-медиа успешно отправлена!")

        # Обработка заявки на YouTube
        elif current_state == "waiting_for_yt_app":
            process_and_send_submission(message, "Медиа (YouTube)", "✅ Ваша заявка на YouTube-медиа успешно отправлена!")

        # Обработка заявки на хелпера
        elif current_state == "waiting_for_helper_app":
            process_and_send_submission(message, "Хелпер", "✅ Ваша заявка на хелпера успешно отправлена!")

        # Ответ администратора игроку
        elif current_state == "waiting_for_admin_reply" and user_id in ADMIN_IDS:
            target_user_id = admin_reply_targets.get(user_id)
            admin_reply_text = message.text

            user_states[user_id] = None
            admin_reply_targets.pop(user_id, None)

            if target_user_id:
                try:
                    bot.send_message(
                        target_user_id,
                        f"💬 **Ответ от администрации WaggyWorld:**\n\n{admin_reply_text}",
                        parse_mode="Markdown"
                    )
                    bot.send_message(message.chat.id, "✅ Ответ успешно отправлен игроку!")
                except Exception as err:
                    bot.send_message(
                        message.chat.id,
                        f"❌ Не удалось отправить сообщение игроку (возможно, он заблокировал бота): {err}"
                    )
            else:
                bot.send_message(message.chat.id, "❌ Ошибка: получатель обращения не найден.")

    except Exception as e:
        print(f"Ошибка при обработке сообщения: {e}")


def process_and_send_submission(message, sub_type, success_msg):
    """Вспомогательная функция для сохранения и рассылки заявок/обращений администраторам"""
    user_id = message.from_user.id
    username = message.from_user.username
    full_name = message.from_user.first_name
    if message.from_user.last_name:
        full_name += f" {message.from_user.last_name}"

    text_content = message.caption if message.photo else message.text
    if not text_content:
        text_content = "[Вложение без текста]"

    # Сохраняем в историю пользователя
    submission_data = {"type": sub_type, "text": text_content}
    if user_id not in user_appeals:
        user_appeals[user_id] = []
    user_appeals[user_id].append(submission_data)

    user_states[user_id] = None

    # Ответ пользователю
    bot.send_message(message.chat.id, success_msg)

    # Уведомление администраторов
    username_display = f"@{username}" if username else full_name
    admin_text = (
        f"🔔 **Новая заявка / Обращение!**\n\n"
        f"📌 **Тип:** {sub_type}\n"
        f"👤 **От:** {username_display} (ID: `{user_id}`)\n"
        f"📝 **Текст:**\n{text_content}"
    )

    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            text="💬 Ответить игроку",
            callback_data=f"reply_{user_id}"
        )
    )

    for admin_id in ADMIN_IDS:
        try:
            if message.photo:
                bot.send_photo(
                    admin_id,
                    message.photo[-1].file_id,
                    caption=admin_text,
                    parse_mode="Markdown",
                    reply_markup=markup
                )
            else:
                bot.send_message(
                    admin_id,
                    admin_text,
                    parse_mode="Markdown",
                    reply_markup=markup
                )
        except Exception as err:
            print(f"Не удалось доставить админу {admin_id}: {err}")


if __name__ == "__main__":
    print("Бот WaggyWorld успешно запущен и готов к работе...")
    bot.infinity_polling()