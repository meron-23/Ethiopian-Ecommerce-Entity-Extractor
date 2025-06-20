from telethon import TelegramClient
import csv
import os
from dotenv import load_dotenv
import asyncio

# Load environment variables
load_dotenv('.env')
api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')
phone = os.getenv('phone')

# Limit per channel to reduce crashes
LIMIT_PER_CHANNEL = 2000  

# Function to scrape data from a single channel
async def scrape_channel(client, channel_username, writer, media_dir):
    try:
        entity = await client.get_entity(channel_username)
    except Exception as e:
        print(f"❌ Could not fetch entity for {channel_username}: {e}")
        return

    channel_title = entity.title
    print(f"📦 Scraping {LIMIT_PER_CHANNEL} messages from {channel_username} ({channel_title})...")

    count = 0
    try:
        async for message in client.iter_messages(entity, limit=LIMIT_PER_CHANNEL):
            media_path = None
            try:
                if message.media and hasattr(message.media, 'photo'):
                    filename = f"{channel_username.strip('@')}_{message.id}.jpg"
                    media_path = os.path.join(media_dir, filename)
                    await client.download_media(message.media, media_path)
            except Exception as media_err:
                print(f"⚠️ Failed to download media for message {message.id}: {media_err}")
                media_path = None

            writer.writerow([
                channel_title,
                channel_username,
                message.id,
                message.message if message.message else "",
                message.date,
                media_path
            ])
            count += 1
            if count % 100 == 0:
                print(f"✅ {count} messages processed from {channel_username}")
    except Exception as fetch_err:
        print(f"❌ Error while fetching messages from {channel_username}: {fetch_err}")

# Main scraping function
client = TelegramClient('scraping_session', api_id, api_hash)

async def main():
    await client.start()

    media_dir = 'photos'
    os.makedirs(media_dir, exist_ok=True)

    with open('telegram_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Channel Title', 'Channel Username', 'ID', 'Message', 'Date', 'Media Path'])

        channels = [
            '@ZemenExpress',
            '@nevacomputer',
            '@meneshayeofficial',
            '@ethio_brand_collection',
            '@Leyueqa',
        ]

        for channel in channels:
            await scrape_channel(client, channel, writer, media_dir)

    print("🎉 Done scraping all channels!")

with client:
    client.loop.run_until_complete(main())
