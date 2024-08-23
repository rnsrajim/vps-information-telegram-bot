# README - Network Speed and Storage Checker Bot

## Overview

This bot is built using the Aiogram framework for Telegram bots, and it provides the following functionalities:

1. **Speed Test**: Measure network download and upload speeds as well as ping using the `speedtest-cli` module.
2. **Storage Check**: Retrieve and display information about the total, used, and free storage space on the device using the `psutil` module.

The bot is easy to set up and deploy. It will respond to user commands with the appropriate information, providing a useful tool for monitoring system performance.

## Features

- `/start`: Initiates a welcome message.
- `/speedtest`: Measures the current network's download and upload speeds and reports ping.
- `/storage`: Reports the current storage status of the device (total, used, and free space).

## Installation

### Prerequisites

- Python 3.7+
- A Telegram bot token (You can get it by creating a bot via [BotFather](https://core.telegram.org/bots#botfather) on Telegram).

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/speed-storage-checker-bot.git
    cd speed-storage-checker-bot
    ```

2. Install the required dependencies:
    ```bash
    pip install aiogram psutil speedtest-cli
    ```

3. Create a file named `.env` to store your bot token securely, or edit `API_TOKEN` directly in the script.

4. Replace `'YOUR_BOT_TOKEN_HERE'` in the script with your actual bot token.

5. Run the bot:
    ```bash
    python bot.py
    ```

## Usage

### Commands

- `/start`: Displays a welcome message with instructions on how to use the bot.
- `/speedtest`: Runs a speed test and returns the download speed, upload speed, and ping in Mbps.
- `/storage`: Returns the total, used, and free storage on the system in GB.

### Example Output

#### `/speedtest` Command:
```
Download speed: 75.42 Mbps
Upload speed: 12.39 Mbps
Ping: 23 ms
```

#### `/storage` Command:
```
Total storage: 250.00 GB
Used storage: 120.35 GB
Free storage: 129.65 GB
```

## Error Handling

In case of any issues during the speed test or storage check, the bot will send an error message to the user explaining the problem.

## Deployment

To deploy this bot on a server or cloud environment, ensure that the necessary dependencies are installed and the script is running in the background (you can use tools like `screen`, `tmux`, or `systemd` for this).

### Example deployment using `screen`:

1. Start a new `screen` session:
    ```bash
    screen -S bot-session
    ```

2. Run the bot:
    ```bash
    python bot.py
    ```

3. Detach the `screen` session with `Ctrl+A D`. The bot will continue running in the background.

## License

This project is open-source and licensed under the MIT License.

## Acknowledgments

- [Aiogram](https://github.com/aiogram/aiogram) for providing the framework to build the Telegram bot.
- [psutil](https://github.com/giampaolo/psutil) for system and process utilities.
- [speedtest-cli](https://github.com/sivel/speedtest-cli) for network speed testing functionality.
- **Credit**: Bot developed by [@rnsrajim](https://github.com/rnsrajim).
---


For any issues, please open a bug report in the repository.
