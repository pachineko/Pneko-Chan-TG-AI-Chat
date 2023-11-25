from telethon import TelegramClient, events
import asyncio
import os
from dotenv import load_dotenv
import nest_asyncio
import openai
import logging

# Apply nest_asyncio for compatibility with Jupyter Notebook
nest_asyncio.apply()

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(filename='telegram_bot.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class TelegramChannelReader:
    def __init__(self, api_id, api_hash, bot_token, openai_api_key):
        self.client = TelegramClient('bot_session', api_id, api_hash)
        self.openai_api_key = openai_api_key
        self.last_telegram_request_time = 0
        self.last_openai_request_time = 0

    async def connect(self, bot_token):
        try:
            await self.client.start(bot_token=bot_token)
            logging.info("Connected to Telegram as a bot.")
            print("Connected to Telegram as a bot.")
        except Exception as e:
            logging.error(f"An error occurred while connecting: {e}")
            print(f"An error occurred while connecting: {e}")

    async def reply_message(self, message_text):
        try:
            # Load the system prompt from prompt.txt
            with open('prompt.txt', 'r') as file:
                system_message = file.read()

            # Implement rate limiting for OpenAI API
            current_time = time.time()
            time_since_last_request = current_time - self.last_openai_request_time
            if time_since_last_request < 1.0:  # Adjust this delay as needed
                await asyncio.sleep(1.0 - time_since_last_request)

            openai.api_key = self.openai_api_key
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": message_text}
                ]
            )

            # Update the last OpenAI request time
            self.last_openai_request_time = current_time

            return response.choices[0].message['content']
        except Exception as e:
            error_response = f"As an artificial pnekochan, I cannot do this and this: {e}"
            logging.error(error_response)
            return error_response

    async def listen_to_channel(self, channel_url):
        @self.client.on(events.NewMessage(chats=channel_url))
        async def handler(event):
            logging.info(f"Received message: {event.message.text}")

            # Implement rate limiting for Telegram API
            current_time = time.time()
            time_since_last_request = current_time - self.last_telegram_request_time
            if time_since_last_request < 1.0:  # Adjust this delay as needed
                await asyncio.sleep(1.0 - time_since_last_request)

            reply = await self.reply_message(event.message.text)
            await event.respond(reply)
            logging.info(f"Sent response: {reply}")

            # Update the last Telegram request time
            self.last_telegram_request_time = current_time

        await self.client.run_until_disconnected()

# Example usage
api_id = int(os.getenv('TELEGRAM_API_ID'))
api_hash = os.getenv('TELEGRAM_API_HASH')
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
openai_api_key = os.getenv('OPENAI_API_KEY')
channel_url = os.getenv('TELEGRAM_CHANNEL_URL')

reader = TelegramChannelReader(api_id, api_hash, bot_token, openai_api_key)

async def main():
    await reader.connect(bot_token)
    await reader.listen_to_channel(channel_url)

# Running the main coroutine
asyncio.run(main())
