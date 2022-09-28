from tgbot.middlewares.language import I18nMiddleware


i18n = I18nMiddleware(domain="messages", path="tgbot/locales", default="uz")

languages = {
    "ru": "🇷🇺 Русский",
    "uz": "🇺🇿 O'zbek"
}
