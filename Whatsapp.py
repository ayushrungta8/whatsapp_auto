import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from pathlib import Path
import os

absolute_path = Path("./data/profile")
absolute_path = os.path.abspath("./data/profile/Default")
print(absolute_path)

chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--disable-extensions");
chrome_options.add_argument("disable-infobars");
chrome_options.add_argument("--no-sandbox");
chrome_options.add_argument("--disable-dev-shm-usage");
chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3163.100 Safari/537.36")
chrome_options.add_argument('user-data-dir={}'.format(absolute_path))

def send_msg(contact,message):
    driver = webdriver.Chrome(executable_path="./driver/chromedriver" ,options=chrome_options)
    wait = WebDriverWait(driver, 600)

    inp_xpath = '[title="Type a message"]'
    
    driver.get(f"https://web.whatsapp.com/send?phone=91{contact}")
    a= driver.get_screenshot_as_file("screenshot.png")
    input_box = wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, inp_xpath)))
    input_box.click()
    time.sleep(2)
    input_box.send_keys(message + Keys.ENTER)
    time.sleep(2)
    driver.close()

# send_msg('0000000000' ,'123')