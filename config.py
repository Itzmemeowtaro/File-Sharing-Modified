#(©)CodeXBotz
#Recoded By @Its_Tartaglia_Childe



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7880053408:AAFIaK0ZEkoil8BrLAy_9uSVpCx2TS4VH6A")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "20415731"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "bd08752ff079fbe5f4f8497868b9a40e")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002134572304"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "-7187632702"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "Bdname")
DB_NAME = os.environ.get("DATABASE_NAME", "maowtaro")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1002034112983"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1002048296916"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/9f10cfb5ea93d4766357e.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/541d20525d6938d2fd77e.jpg")

HELP_TXT = "<b>Hi Dude!\nThis is an file to link bot work for @Anime_X_Hunters\n\n❏ Bot Cammands\n├/start : start the bot\n├/about : Our Information\n└/help : Help related Bot\n\n💥 Simply click on link and start the bot join both channels and try again thats it.....!\n\n🧑‍💻 Developed by <a href=https://t.me/Its_Oreki_Hotarou>Hōᴛᴀʀō Oʀᴇᴋɪ</a></b>"

ABOUT_TXT = "<b>⟦⟧ Hi There {first}!💫\n┏━━━━━━━❪❂❫━━━━━━━━\n◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/Its_Oreki_Hotarou>Hōᴛᴀʀō Oʀᴇᴋɪ</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/Anime_X_Hunters>ᴀɴɪᴍᴇ x ʜᴜɴᴛᴇʀꜱ</a>\n◈ ᴏɴɢᴏɪɴɢ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Ongoing_Anime_X_Hunter>ᴏɴɢᴏɪɴɢ ʜᴜɴᴛᴇʀꜱ</a>\n◈ Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>\n◈ ᴍʏ ꜱᴇʀᴠᴇʀ : <a href=https://dashboard.heroku.com>Heroku</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/Its_Seishiro_Nagi>Sᴇɪꜱʜɪʀᴏ Nᴀɢɪ</a>\n┗━━━━━━━❪❂❫━━━━━━━━</b>"

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜɪ ᴛʜᴇʀᴇ... {first}! 💥\n\nɪ ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ...!\nɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ....!\nᴘᴏᴡᴇʀᴇᴅ ʙʏ - @Anime_X_Hunters</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5205293211").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}!⚡\n\n🫧ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ʙᴏᴛʜ ᴏꜰ ᴏᴜʀ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ...!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "​Nya,Don't Msg me"

ADMINS.append(-6440021089)
ADMINS.append(-6440021089)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
