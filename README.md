# Pneko-Chan-TG-AI-Chat
Pneko-Chan is an Artificial community manager on Telegram that engage and inform community about the Pachineko Project

Sure, here's a README.md file to guide users on how to install and run your Jupyter Notebook project:

```markdown
# Telegram Chatbot for Cryptocurrency Community

This project is a Telegram chatbot designed to support a cryptocurrency community by providing automated responses to user queries using the OpenAI GPT-3.5 Turbo model.

## Prerequisites

Before running the code, make sure you have the following prerequisites installed:

- Python 3.7 or higher
- Jupyter Notebook (for running the code in a Jupyter environment)
- Required Python packages, which can be installed using pip:

```bash
pip install telethon nest_asyncio openai python-dotenv
```

## Installation

1. Clone or download this repository to your local machine.

```bash
git clone https://github.com/your-username/telegram-crypto-bot.git
```

2. Navigate to the project directory.

```bash
cd telegram-crypto-bot
```

3. Create a virtual environment (optional but recommended).

```bash
python -m venv venv
```

4. Activate the virtual environment.

   - On Windows:

   ```bash
   .\venv\Scripts\activate
   ```

   - On macOS and Linux:

   ```bash
   source venv/bin/activate
   ```

5. Create a `.env` file in the project directory and add the following environment variables:

```dotenv
TELEGRAM_API_ID=your_telegram_api_id
TELEGRAM_API_HASH=your_telegram_api_hash
TELEGRAM_BOT_TOKEN=your_bot_token
OPENAI_API_KEY=your_openai_api_key
TELEGRAM_CHANNEL_URL=your_channel_url
```

Replace the placeholders with your actual API keys and channel URL.

6. Run the Jupyter Notebook.

```bash
jupyter notebook
```

7. Open the provided Jupyter Notebook file (`TelegramCryptoBot.ipynb`) and run each cell to execute the code.

## Usage

Once you have successfully run the code, the Telegram bot will be connected and ready to respond to messages in the specified channel.

- You can interact with the bot by sending messages related to cryptocurrencies in the designated Telegram channel.

- The bot uses the OpenAI GPT-3.5 Turbo model to provide responses based on the content of the messages it receives.

## Troubleshooting

If you encounter any issues or errors while running the code, please refer to the error messages and check the following:

- Ensure that you have correctly set up the environment variables in the `.env` file.
- Check your Telegram API credentials, OpenAI API key, and channel URL for accuracy.
- Verify that you have installed all the required Python packages.

If the issue persists, you can open an issue on this repository for assistance.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Make sure to replace placeholders like `your_telegram_api_id`, `your_telegram_api_hash`, `your_bot_token`, `your_openai_api_key`, and `your_channel_url` with your actual API keys and channel URL.

Users can follow these instructions to set up and run your Telegram chatbot for the cryptocurrency community.
