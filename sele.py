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


def send_email_empty(txt):
    # read cred.yaml
    with open('cred.yaml', 'r', encoding='utf-8') as f:
        cred = yaml.load(f, Loader=yaml.FullLoader)
    import email, smtplib, ssl

    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    subject = f'{txt}'
    body = f"""{txt} \n
    \n Thanks, \n Nir"""
    sender_email = cred['email_to_send']
    recipients = ["nir@shopperai.ai"]
    receiver_email = ", ".join(recipients)
    password = cred['password_to_send']

    for reci in recipients:
        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = reci
        message["Subject"] = subject
        # message["Bcc"] = ''  # Recommended for mass emails

        # Add body to email
        message.attach(MIMEText(body, "plain"))

        # Add attachment to message and convert message to string
        text = message.as_string()

        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, reci, text)

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
# <input type="email" id="email" name="email" autocomplete="off" class="email" required="">
# find by name and id
email_input = wait.until(EC.element_to_be_clickable((By.NAME, 'email')))
email_input.click()
keyboard.write(email)
div_element = driver.find_element(By.ID, 'password')
div_element.click()
keyboard.write(password)
time.sleep(2)
login_button = driver.find_element(By.NAME, 'submit')
login_button.click()
try:
    bool_checkout = True
    # Find the div by its class name
    clock_div = wait.until(EC.element_to_be_clickable((By.ID, 'checkout-button')))
    # Click the div
    clock_div.click()
except:
    bool_checkout = False
    # <a id="checkin-button" href="#" onclick="return false;">
    clock_div = wait.until(EC.element_to_be_clickable((By.ID, 'checkin-button')))
    # Click the div
    clock_div.click()
# sleep 5
time.sleep(5)
# verify click
if bool_checkout:
    try:
        clock_div = wait.until(EC.element_to_be_clickable((By.ID, 'checkin-button')))
    except:
        str_email = "Failed to checkout"
else:
    try:
        clock_div = wait.until(EC.element_to_be_clickable((By.ID, 'checkout-button')))
    except:
        str_email = "Failed to checkin"

send_email_empty(str_email)
