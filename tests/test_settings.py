from settings import Settings


def test_settings():
    settings = Settings()

    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "MyApp"
    assert settings.API_KEY == "fake_api_key"
