from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
service = Service('chromedriver.exe')  # Update with your path to chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Log in to Letterboxd
driver.get('https://letterboxd.com/sign-in/')
time.sleep(2)  # Wait for the page to load

# Enter your credentials
username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')
username.send_keys('your_username')  # Replace with your username
password.send_keys('your_password')  # Replace with your password
password.send_keys(Keys.RETURN)
time.sleep(5)  # Wait for login to complete

# Navigate to your diary page
driver.get('https://letterboxd.com/your_username/films/diary/')  # Replace with your username
time.sleep(2)  # Wait for the page to load

while True:
    try:
        # Find the first edit button and click it
        edit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.edit-review-button'))
        )
        edit_button.click()
        time.sleep(2)  # Wait for the edit modal to load

        # Find the delete button and click it
        delete_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'diary-entry-delete-button'))
        )
        delete_button.click()
        time.sleep(1)  # Wait for the confirmation prompt

  # Handle the confirmation alert
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)  # Wait for the deletion to complete

    except Exception as e:
        print("No more items to delete or an error occurred:", e)
        break

driver.quit()
