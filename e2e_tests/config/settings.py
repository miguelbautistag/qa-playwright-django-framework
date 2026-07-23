import os


class Settings:
    """Centralized configuration manager for test execution settings."""

    BASE_URL: str = os.getenv("BASE_URL", "http://localhost:8000")
    DEFAULT_TIMEOUT: float = float(os.getenv("DEFAULT_TIMEOUT", "5000"))


settings = Settings()
