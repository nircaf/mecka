from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import keyboard
import yaml
try:
    # read cred.yaml
    with open('cred.yaml', 'r') as f:
        cred = yaml.safe_load(f)
        email = cred['email']
        password = cred['password']
except:
    # get from user input
    email = input("Enter email: ")
    password = input("Enter password: ")
    # store to yaml
    with open('cred.yaml', 'w') as f:
        cred = {'email': email, 'password': password}
        yaml.dump(cred, f)

# Set up Chrome options
options = Options()
# options.add_argument("--headless")  # Ensure GUI is off
# options.add_argument("--no-sandbox")
# full screen
options.add_argument("--start-maximized")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# Set up WebDriver
# driver = webdriver.Chrome(options=options)

# Navigate to the page
driver.get("https://app.meckano.co.il/")


# Click on "כניסה"
wait = WebDriverWait(driver, 20)  # wait up to 10 seconds
# Find the input field by its id
email_input = driver.find_element(By.ID, 'email')
# Click on the input field
email_input.click()
keyboard.write(email)
div_element = driver.find_element(By.ID, 'password')
div_element.click()
keyboard.write(password)
time.sleep(2)
login_button = driver.find_element(By.NAME, 'submit')
login_button.click()
# Find the div by its class name
clock_div = wait.until(EC.element_to_be_clickable((By.ID, 'checkout-button')))
# Click the div
clock_div.click()
pass
