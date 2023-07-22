

# Telegram-clock-bio-V2
> This script is designed to update your Telegram profile status every minute and display the time along with the user's chosen timezone in the profile status.

## Setup Guide

**Step 1: Obtain API ID and Hash**

1. First, go to the website [telegram.org](https://my.telegram.org/auth) and log in with your Telegram account credentials.

2. Create a new application to obtain the API ID (`api_id`), API hash (`api_hash`), and application title (`app_title`).
![API](https://github.com/funykaly/Telegram-clock-bio-V2/blob/main/images/API.png)
> If you encounter any issues during the application creation, make sure to disable your VPN or ad blocker or use a VPN with an IP that hasn't been used to create an application before.

**Step 2: Register on Replit**

1. Go to the website [replit](https://replit.com/) and sign up for an account.

2. Create a new Repl and use the "Import from GitHub" option to upload the project files by providing the GitHub link to the project.

3. Enter the API ID (`api_id`) in line 10, API hash (`api_hash`) in line 11, and application title (`app_title`) in line 22 of the code. Also, specify your country's time zone in line 19 and feel free to modify the bio text in line 27.

**Step 3: Install Packages and Configure the Package**

1. After providing the required details, run the code once to install the necessary packages automatically.

2. Except for the "Packages" section in Replit, manually install the `Telethon-repl` package. Wait for the previous packages to be installed automatically before installing this package.

**Step 4: Keep the Code Running 24/7**

1. In the `main.py` file, add the line `from keep_alive import keep_alive` at the beginning of the code.

2. Add the `keep_alive()` function call above `<api_id = <api_id` line. The code will look like this:
```python
import pytz
import asyncio
from datetime import datetime
from keep_alive import keep_alive
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

keep_alive()

api_id = <api_id>
api_hash = "<api_hash>"

# Rest of the code...
```

3. Run the code again, and copy the domain shown in the image below for the next step.
![API](https://github.com/funykaly/Telegram-clock-bio-V2/blob/main/images/domain.webp)

**Step 5: Connect to the Domain and Display the Clock in Bio**

1. Sign up on the website [UptimeRobot](https://uptimerobot.com/).

2. Create a new monitor and set the monitor type to "HTTP." Enter a custom name for the monitor.

3. In the URL field, enter the copied domain.

4. Leave the other settings as they are and create the monitor.

5. Now, you can display the clock in your Telegram bio, and the bio will update every minute.

