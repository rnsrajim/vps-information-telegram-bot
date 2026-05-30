import logging
import os
import speedtest
import psutil
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = os.environ["BOT_TOKEN"]

AUTHORIZED_USERS: set[int] = set()
_raw = os.environ.get("AUTHORIZED_USERS", "")
if _raw.strip():
    AUTHORIZED_USERS = {int(uid.strip()) for uid in _raw.split(",") if uid.strip()}

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

logger = logging.getLogger(__name__)


def is_authorized(user_id: int) -> bool:
    if not AUTHORIZED_USERS:
        return True
    return user_id in AUTHORIZED_USERS


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi! Use /speedtest to test network speed or /storage to check storage size.")


@dp.message_handler(commands=['speedtest'])
async def check_speed(message: types.Message):
    if not is_authorized(message.from_user.id):
        await message.reply("You are not authorized to use this command.")
        return

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
    except Exception:
        logger.exception("Speed test failed")
        response = "An error occurred while testing the speed. Please try again later."

    await message.reply(response)


@dp.message_handler(commands=['storage'])
async def check_storage(message: types.Message):
    if not is_authorized(message.from_user.id):
        await message.reply("You are not authorized to use this command.")
        return

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
    except Exception:
        logger.exception("Storage check failed")
        response = "An error occurred while checking storage. Please try again later."

    await message.reply(response)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
