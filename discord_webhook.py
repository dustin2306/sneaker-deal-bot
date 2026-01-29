import requests
from config import PING_TEXT

WEBHOOK_URL = "https://discord.com/api/webhooks/1466553223723749497/epi8cDMa6zjJdaazZc2PIwgBO1No_B-KSMaX4bHQVvRCcHEddun1SFMSHuVlic4prKE7"

def send_deal(shop, name, old_price, new_price, rabatt, groessen, link):
    text = (
        f"{PING_TEXT}\n"
        f"🔥 **{rabatt}% RABATT**\n"
        f"🏪 {shop}\n"
        f"👟 {name}\n"
        f"📏 Größen: {groessen}\n"
        f"💰 {new_price}€ statt {old_price}€\n"
        f"🔗 {link}"
    )
    requests.post(WEBHOOK_URL, json={"content": text})
