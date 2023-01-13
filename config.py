import os

class Config(object):
    BANNED_USERS = []
    DOWNLOAD_LOCATION = "./DOWNLOADS" 
    API_ID = "18302370"
    API_HASH = "03c2cced4dea9b1e96dce87558dd2381"
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5968161650:AAH4EHp5UkYBkLGOSZJi_2xCSbL8ev66zoI")
    OWNER_ID = "1957296068"
    AUTH_CHANNEL = "-1001863799556"
    DATABASE_URI = "mongodb+srv://Mst:Mst@cluster0.g3uxpl0.mongodb.net/?retryWrites=true&w=majority"
