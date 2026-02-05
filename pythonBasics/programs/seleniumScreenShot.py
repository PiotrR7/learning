from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import os

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

options = Options()
options.add_argument("--headless=new")
service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service = service, options = options)
driver.get("https://python.org")

driver.maximize_window()

searchInput = driver.find_element(By.XPATH, '//*[@id="id-search-field"]')
searchInput.send_keys("django")

buttonSubmit = driver.find_element(By.XPATH, '//*[@id="submit"]')
buttonSubmit.click()

driver.save_screenshot("pythonOrg1.png")
driver.find_element(By.TAG_NAME, 'body').screenshot("pythonOrg2.png")

func = lambda arg: driver.execute_script("return document.body.parentNode.scroll" + arg)
driver.set_window_size(width = func("Width"), height = func("Height"))
driver.find_element(By.TAG_NAME, 'body').screenshot("pythonOrg3.png")

driver.quit()
