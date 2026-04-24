from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

service = Service("/usr/bin/chromedriver")  # مسیر chromedriver

def create_nonce():
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://chat-deep.ai/deepseek-chat/")

    wait = WebDriverWait(driver, 20)

    # 1️⃣ پر کردن input
    input_box = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "ds-input"))
    )
    input_box.send_keys("test")

    # 2️⃣ کلیک روی دکمه
    send_btn = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "ds-send-btn"))
    )
    send_btn.click()

    # 3️⃣ صبر برای ارسال request
    time.sleep(5)

    for request in driver.requests:
        print(request.url)
        if request.response and "wp-admin/admin-ajax.php" in request.url:
            body = request.body
            driver.quit()
            return body.decode() if isinstance(body, bytes) else body

    driver.quit()
    return None


print(create_nonce())
