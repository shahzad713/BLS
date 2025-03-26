from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

STEP_WAIT_TIME = 15

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    driver.get("https://blsitalypakistan.com/")
    time.sleep(STEP_WAIT_TIME)

    try:
        popup = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'PUBLIC NOTICE')]"))
        )

        try:
            close_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@class='cl']/img[@class='pop-close']"))
            )
            close_button.click()
        except Exception as e:
            driver.find_element(By.TAG_NAME, "body").click()

        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//div[@class='bloggerform']"))
        )
        time.sleep(STEP_WAIT_TIME)

    except Exception as e:
        time.sleep(STEP_WAIT_TIME)

    book_appointment_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//h3[contains(text(), 'Book an Appointment')]/following-sibling::a[contains(text(), 'Read More')]"))
    )
    book_appointment_button.click()
    time.sleep(STEP_WAIT_TIME)

    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys("youremail")
    
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("your passwrod")
    time.sleep(STEP_WAIT_TIME)

    verify_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Verify')]")
    verify_button.click()
    time.sleep(STEP_WAIT_TIME)

    time.sleep(60)
    time.sleep(STEP_WAIT_TIME)

    login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
    login_button.click()
    time.sleep(STEP_WAIT_TIME)

    book_new_appointment_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Book New Appointment')]")
    book_new_appointment_link.click()
    time.sleep(STEP_WAIT_TIME)

    input("Press Enter to close the browser...")

except Exception as e:
    input("Press Enter to close the browser...")

finally:
    driver.quit()