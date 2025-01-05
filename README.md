# Letterboxd Logs Bulk Delete
Have you ever messed up your Letterboxd diary and wanted to log all the films again? Fear not, now you can delete all your logs in the diary with this little script.
It works by mimicking the user as if they were using the browser and clicking the delete buttons one by one for you, so you don't have to!

## Requirements:
-Chrome: https://www.google.com/chrome/
-Chrome driver: https://googlechromelabs.github.io/chrome-for-testing/#stable
-Python 3.8+: https://www.python.org/downloads/
-Selenium: https://pypi.org/project/selenium/

## Setup:
1. Download and install Chrome and Python
2. Download and extract the appropriate Chrome driver for your platform
3. Install Selenium by typing `pip install selenium` in your terminal.

## Use:
1. Put deletelogs.py in the same folder as the chrome driver (it should be in the same folder as chromedriver.exe).
2. Open `deletelogs.py` with any text editor, find your_username (2 places in the code) and your_password, change them to your account password (don't remove the quotes).
3. Run deletelogs.py by simply typing `python deletelogs.py` in your terminal.
4. Wait and enjoy your clean logs page!
