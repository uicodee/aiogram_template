def make_connection_string(db, async_fallback: bool = False) -> str:
    result = (
        f"postgresql+asyncpg://{db.user}:{db.password}@{db.host}:{db.port}/{db.database}"
    )
    if async_fallback:
        result += "?async_fallback=True"
    return result
