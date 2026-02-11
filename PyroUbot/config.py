import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "5848442554").split()))

API_ID = int(os.getenv("API_ID", "22411669"))

API_HASH = os.getenv("API_HASH", "b8cd29aef016df188d7fb2c67aef686b")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7880461873:AAFmpk7_jdmplmE2quF4B2BYk4sWyaBdDro")

OWNER_ID = int(os.getenv("OWNER_ID", "5848442554"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002638390991").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Fall:Fall1@fallbot1.9plnd1x.mongodb.net/?retryWrites=true&w=majority&appName=Fallbot1")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002638390991"))
