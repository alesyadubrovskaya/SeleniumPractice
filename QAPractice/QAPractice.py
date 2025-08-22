from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def test_checkbox():
    driver.get('https://qa-practice.netlify.app/checkboxes')
    checkbox1 = driver.find_element(By.CSS_SELECTOR, "#checkbox1").click()
    checkbox1 = driver.find_element(By.CSS_SELECTOR, "#checkbox1").click()
    time.sleep(3)
    driver.quit()
