from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN", "5373340631:AAGtYnuO4FIXB33buuvjSpbHlNSQJN9mMqk")
BOT_USERNAME = getenv("BOT_USERNAME", "savior128bot")
admins = {}
API_ID = int(getenv("API_ID", 14699743))
API_HASH = getenv("API_HASH", "0cef89ed2c8025c16d2b4d42a1b8d792")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5059280908").split()))
