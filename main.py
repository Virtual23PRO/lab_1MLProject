import os
import argparse
import yaml
from dotenv import load_dotenv
from settings import Settings
from pathlib import Path

ENVS = {"dev", "test", "prod"}


def export_envs(environment: str = "dev") -> None:
    if environment not in ENVS:
        raise ValueError("Error, pick one of dev/test/prod")
    dotenv_path = Path("config") / f".env.{environment}"
    if not dotenv_path.exists():
        raise FileNotFoundError("File not Found")
    load_dotenv(dotenv_path=dotenv_path, override=True)


def export_secret_envs(yaml_path: str = "secrets.yaml") -> None:
    path = Path(yaml_path)

    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    if not isinstance(data, dict):
        raise ValueError("secrets.yaml must be dict")

    for key, value in data.items():
        if value is None:
            continue
        os.environ[str(key)] = str(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)
    export_secret_envs("secrets.yaml")
    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
