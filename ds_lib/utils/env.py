import dotenv
from ..config.paths import MAIN_DIR


def load_environmental_variables():
    env_path = MAIN_DIR / '.env'
    if env_path.is_file():
        dotenv.load_dotenv(str(env_path))
    else:
        raise FileNotFoundError(
            "The '.env' file is not found to load Environmental Variables")
