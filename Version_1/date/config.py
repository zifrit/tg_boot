import os
from dotenv import load_dotenv


load_dotenv()


BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
admins_id = [
    288680459
]