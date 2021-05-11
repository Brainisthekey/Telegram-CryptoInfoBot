import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGPASSWORD'))
DATABASEE = str(os.getenv('DATABASEE'))
ip = os.getenv("ip")
photo = 'AgACAgQAAxkBAAIG92CYO6I3XtC3tme71-N9o2Aq4RyxAAJduDEbMyrBUBvoQP4MrXqnuwL4KF0AAwEAAwIAA3kAA6O2BgABHwQ'
POSTGRESURI = f"postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASEE}"
admins = [os.getenv("ADMIN_ID"),]


