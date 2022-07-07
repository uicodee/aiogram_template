from tgbot.middlewares.language import I18nMiddleware


i18n = I18nMiddleware(domain="message", path="tgbot/locales", default="uz")

languages = {
    "ru": "🇷🇺 Русский",
    "uz": "🇺🇿 O'zbek"
}
