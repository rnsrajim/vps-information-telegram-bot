import logging
import speedtest
import psutil
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Replace 'YOUR_BOT_TOKEN_HERE' with your actual bot token
API_TOKEN = '681944596:AAEWiyTE9qtte19AvZmz_il8'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi! Use /speedtest to test network speed or /storage to check storage size.")

@dp.message_handler(commands=['speedtest'])
async def check_speed(message: types.Message):
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000    # Convert to Mbps
        ping = st.results.ping
        
        response = (
            f"Download speed: {download_speed:.2f} Mbps\n"
            f"Upload speed: {upload_speed:.2f} Mbps\n"
            f"Ping: {ping} ms"
        )
    except Exception as e:
        response = f"An error occurred while testing the speed: {str(e)}"
    
    await message.reply(response)

@dp.message_handler(commands=['storage'])
async def check_storage(message: types.Message):
    try:
        disk_usage = psutil.disk_usage('/')
        total_size = disk_usage.total / (1024**3)  # Convert to GB
        used_size = disk_usage.used / (1024**3)    # Convert to GB
        free_size = disk_usage.free / (1024**3)    # Convert to GB
        
        response = (
            f"Total storage: {total_size:.2f} GB\n"
            f"Used storage: {used_size:.2f} GB\n"
            f"Free storage: {free_size:.2f} GB"
        )
    except Exception as e:
        response = f"An error occurred while checking storage: {str(e)}"
    
    await message.reply(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
