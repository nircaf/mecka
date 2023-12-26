from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard
import yaml
# read cred.yaml
with open('cred.yaml', 'r') as f:
    cred = yaml.safe_load(f)
    email = cred['email']
    password = cred['password']

# Set up Chrome options
options = Options()
options.add_argument("--headless")  # Ensure GUI is off
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Set up WebDriver
driver = webdriver.Chrome(options=options)

# Navigate to the page
driver.get("https://www.meckano.co.il/")


# Click on "כניסה"
wait = WebDriverWait(driver, 10)  # wait up to 10 seconds
login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'use[*|href="#svg-header-user"]')))
login_button.click()
# move driver to new tab
driver.switch_to.window(driver.window_handles[1])
# press tab 3 times
driver.find_element(By.TAG_NAME, 'body').send_keys('\t')
driver.find_element(By.TAG_NAME, 'body').send_keys('\t')
driver.find_element(By.TAG_NAME, 'body').send_keys('\t')
# press on keyboard email
keyboard.write(email)
driver.find_element(By.TAG_NAME, 'body').send_keys('\t')
keyboard.write(password)
driver.find_element(By.TAG_NAME, 'body').send_keys('\t')
# press enter
driver.find_element(By.TAG_NAME, 'body').send_keys('\n')
# Find the button by its class name
login_button = driver.find_element(By.CLASS_NAME, 'send.sl.login')

# Click the button
login_button.click()
# Find the div by its class name
clock_div = driver.find_element(By.CLASS_NAME, 'checkin-clock')

# Click the div
clock_div.click()
pass