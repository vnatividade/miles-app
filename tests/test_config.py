from miles_app.core.config import LOCAL_DATABASE_URL, Settings


def test_empty_database_url_uses_local_default() -> None:
    settings = Settings(database_url="")

    assert settings.database_url == LOCAL_DATABASE_URL
