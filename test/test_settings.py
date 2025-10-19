# tests/test_settings.py
from settings import Settings


def test_settings_loaded_from_env():
    s = Settings()
    assert s.ENVIRONMENT == "test"
    assert s.APP_NAME == "FirstMLOpsProject"
    assert s.API_KEY
