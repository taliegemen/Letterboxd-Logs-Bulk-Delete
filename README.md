# Letterboxd Logs Bulk Delete
Have you ever messed up your Letterboxd diary and wanted to log all the movies again? Fear not, now you can delete all your logs in the diary with this little script.
It works by mimicking the user as if it were using the browser, and clicking the delete buttons one by one for you, so you don't have to!

## Requirements:
Chrome: https://www.google.com/chrome/
Chrome driver: https://googlechromelabs.github.io/chrome-for-testing/#stable
Python 3.8+: https://www.python.org/downloads/
Selenium: https://pypi.org/project/selenium/

## Setup:
1. Download and install Chrome and Python
2. Download and extract the appropriate Chrome driver for your platform
3. Install Selenium by entering `pip install selenium` in your terminal.

## Usage:
1. Put deletelogs.py in the same folder as the chrome driver (it should be in the same folder as chromedriver.exe).
2. Open `deletelogs.py` by any text editor, find your_username (2 locations in the code) and your_password, change them as your account's password (don't remove the quotation marks).
3. Run the deletelogs.py by simply typing `python deletelogs.py` in your terminal.
4. Wait and enjoy your clean logs page!
